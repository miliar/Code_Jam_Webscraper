//Grzegorz Prusak
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

#define REP(i,n)    for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)

#define SQR(a) ((a)*(a))
#define ABS(a) ((a)>0?(a):-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a>b)?(a):(b))

template<typename T> inline T sqr(T a){ return a*a; }
template<typename T> inline T abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T min(T a, T b){ return a<b ? a : b; }
template<typename T> inline T max(T a, T b){ return a>b ? a : b; }
template<typename T> inline void checkmin(T &a, T b){ if(a>b) a=b; }
template<typename T> inline void checkmax(T &a, T b){ if(a<b) a=b; }

typedef long long LL;
typedef unsigned long UL;
typedef unsigned long long ULL;

double inf = 1./0.;

template<typename T> struct Point
{
	Point(){} Point(T _x, T _y) : x(_x), y(_y) {} T x,y;
	Point & operator+=(const Point &b){ x+=b.x; y+=b.y; return *this; }
	Point & operator-=(const Point &b){ x-=b.x; y-=b.y; return *this; }
	Point & operator*=(T f){ x*=f; y*=f; return *this; }
	Point & operator/=(T f){ x/=f; y/=f; return *this; }
	Point operator+(const Point &b) const { return Point(x+b.x,y+b.y); } 
	Point operator-(const Point &b) const { return Point(x-b.x,y-b.y); }
	Point operator*(T f) const { return Point(x*f,y*f); }
	Point operator/(T f) const { return Point(x/f,y/f); }
	friend Point operator*(T f, const Point &p){ return Point(f*p.x,f*p.y); }
	T operator*(const Point &b) const { return x*b.x+y*b.y; }
	T vec_mult(const Point &b) const { return x*b.y-y*b.x; }
	
	T sqr() const { return x*x+y*y; }
	Point operator-() const { return Point(-x,-y); }
};

template<typename T> struct Circle
/* Circle primitive */
{
	Circle(const Point<T> &_pos, T _rad) : pos(_pos), rad(_rad) {}
	Circle(){} Circle(T _x, T _y, T _rad) : pos(_x,_y), rad(_rad) {} Point<T> pos; T rad;
	Circle operator+(const Point<T> &p) const { return Circle(pos+p,rad); }
};

template<typename T> struct Rect
{
	Rect(const Point<T> &_a, const Point<T> &_b) : a(_a), b(_b) {}
	Rect(){} Rect(T _x0, T _y0, T _x1, T _y1) : a(_x0,_y0), b(_x1,_y1) {} Point<T> a,b;
	Rect cut(const Rect &r) const { return Rect(max(a.x,r.a.x),max(a.y,r.a.y),min(b.x,r.b.x),min(b.y,r.b.y)); }
	Rect operator+(const Point<T> &p) const { return Rect(a+p,b+p); }
	T width () const { return b.x-a.x; }
	T height() const { return b.y-a.y; }
};

//////////////////////////////////////////////

typedef Point<double> Pd;
typedef Circle<double> Cd;

double cross(Pd a, Pd b, Pd c, Pd d)
{
	double f = (d-c).vec_mult(a-c)/(d-c).vec_mult(a-b);
	double g = (b-a).vec_mult(d-a)/(b-a).vec_mult(d-c);
	return 0<=f && f<=1 && 0<=g && g<=1 ? f : inf;
}

int quadratic(double A, double B, double C, double &x1, double &x2)
/*
	solves quadratic equation: Ax^2+Bx+C = 0
	A,B,C are input coefficient
	A is assumed to be different than 0
	x1,x2 are output references where the solutions are stored
	result is the number of solutions - belongs to {0,1,2}
	if result<1 then x1 is undefined
	if result<2 then x2 is undefined
*/
{
	double D = SQR(B)-4*A*C;
	if(D<0) return 0;
	D = sqrt(D);
	x1 = (-B-D)/(2*A);
	x2 = (-B+D)/(2*A);
	return D>0 ? 2 : 1;
}

int cross(const Cd &a, const Cd &b, Pd &p1, Pd &p2)
/*
	finds the crossings of circle a and b
	a,b are the input circles
	a's center is assumed to be different than b's center
	p1,p2 are the output references where crossing points are stored
	result is the number of solutions - belongs to {0,1,2}
	if result<1 then p1 is not set
	if result<2 then p2 is not set
*/
{
	/*
		(x-x0)^2+(y-y0)^2 = r0^2
		(x-x1)^2+(y-y1)^2 = r1^2

		-2(x0-x1)x+(x0^2-x1^2) -2(y0-y1)y+(y0^2-y1^2) = (r0^2-r1^2)
		A = 2(x0-x1)
		B = 2(y0-y1)
		C = (r0^2-r1^2)-(x0^2-x1^2)-(y0^2-y1^2)
		Ax+By+C = 0

		(x0,y0)!=(x1,y1)  =>  A!=0 || B!=0
		
		if(B!=0) 
		{
			y = (-A/B)x+(-C/B)
			c1 = -A/B
			c0 = -C/B-y0
			(x-x0)^2+(c1*x+c0)^2 = r0^2
			(1+c1^2)x^2 +2(c1*c0-x0)x +(x0^2+c0^2-r0^2) = 0
		}

		if(A!=0)
		{
			x = (-B/A)y+(-C/A)
			c1 = -B/A
			c0 = -C/A-x0
			(y-y0)^2+(c1*y+c0)^2 = r0^2
			(1+c1^2)y^2 +2(c1*c0-y0)y +(y0^2+c0^2-r0^2) = 0
		}
	*/
	double A = 2*(a.pos.x-b.pos.x);
	double B = 2*(a.pos.y-b.pos.y);
	double C = (SQR(a.rad)-SQR(b.rad))-(SQR(a.pos.x)-SQR(b.pos.x))-(SQR(a.pos.y)-SQR(b.pos.y));
	if(abs(B)>abs(A))
	{
		double c1 = -A/B;
		double c0 = -C/B-a.pos.y;
		double sx0,sx1;
		int count = quadratic(1+SQR(c1),2*(c1*c0-a.pos.x),SQR(a.pos.x)+SQR(c0)-SQR(a.rad),sx0,sx1);
		if(count>0) p1 = Pd(sx0,c1*sx0+c0+a.pos.y);
		if(count>1) p2 = Pd(sx1,c1*sx1+c0+a.pos.y);
		return count;
	}
	else
	{
		double c1 = -B/A;
		double c0 = -C/A-a.pos.x;
		double sy0,sy1;
		int count = quadratic(1+SQR(c1),2*(c1*c0-a.pos.y),SQR(a.pos.y)+SQR(c0)-SQR(a.rad),sy0,sy1);
		if(count>0) p1 = Pd(c1*sy0+c0+a.pos.x,sy0);
		if(count>1) p2 = Pd(c1*sy1+c0+a.pos.x,sy1);
		return count;
	}
}

int cross(Cd C, Pd A, Pd B, Pd &p1, Pd &p2)
{
	C.pos -= A;
	B -= A;
	double c = C.pos.sqr()-sqr(C.rad);
	double b = -2*B*C.pos;
	double a = B.sqr();
	double v1,v2;
	int count = quadratic(a,b,c,v1,v2);
	if(count>0) p1 = A+B*v1;
	if(count>1) p2 = A+B*v2;
	return count;
}

//////////////////////////////////////////////

int INF = 2000000000;


enum { N_max = 2000 };

struct S
{
	int i;
	Cd C;
	bool operator<(const S &s) const { return C.rad>s.C.rad; }
	static bool cmp(const S &a, const S &b){ return a.i<b.i; }
};

S st[N_max];

int lc;
Pd l[N_max*N_max*3];

int N,W,L;

int I;

bool in(Pd A)
{
	if(!(0<=A.x && A.x<=W && 0<=A.y && A.y<=L)) return 0;
	REP(i,I) if((st[i].C.pos-A).sqr()<sqr(st[i].C.rad*2/2.1)) return 0;
	return 1;
}


void make(Cd C, Pd A, Pd B)
{
	Pd p1,p2;
	int c = cross(C,A,B,p1,p2);
	//printf("count=%d; %lf %lf; %lf %lf\n",c,p1.x,p1.y,p2.x,p2.y);
	if(c>=1 && in(p1)) l[lc++] = p1;
	if(c>=2 && in(p2)) l[lc++] = p2;
}

int main()
{
	int T; scanf("%d",&T);
	FOR(_,1,T)
	{
		scanf("%d%d%d",&N,&W,&L);
		REP(i,N){ st[i].i = i; int r; scanf("%d",&r); st[i].C.rad = r*2.1; }
		std::sort(st,st+N);
		lc = 0;
		l[lc++] = Pd(0,0);
		for(I=0; I<N; I++)
		{
			//REP(k,lc) printf("{%lf %lf} ",l[k].x,l[k].y); puts("");
			while(!in(l[lc-1])) lc--; st[I].C.pos = l[--lc];
			REP(j,I)
			{
				Pd p1,p2;
				int c = cross(st[j].C,st[I].C,p1,p2);
				//printf("CC=%d\n",c);
				if(c>=1 && in(p1)) l[lc++] = p1;
				if(c>=2 && in(p2)) l[lc++] = p2;
			}
			make(st[I].C,Pd(0,0),Pd(W,0));
			make(st[I].C,Pd(0,0),Pd(0,L));
			make(st[I].C,Pd(W,0),Pd(W,L));
			make(st[I].C,Pd(0,L),Pd(W,L));
		}
		std::sort(st,st+N,S::cmp);
		printf("Case #%d: ",_);
		REP(i,N) printf("%.4lf %.4lf ",st[i].C.pos.x,st[i].C.pos.y); puts("");
	}

	return 0;
}

