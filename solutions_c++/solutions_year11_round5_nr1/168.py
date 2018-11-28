//Grzegorz Prusak
#include <iostream>
#include <cmath>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

#define SQR(a) ((a)*(a))
#define ABS(a) ((a)>0?(a):-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a>b)?(a):(b))

template<typename T> inline T abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T min(T a, T b){ return a<b ? a : b; }
template<typename T> inline T max(T a, T b){ return a>b ? a : b; }
template<typename T> inline void checkmin(T &a, T b){ if(a>b) a=b; }
template<typename T> inline void checkmax(T &a, T b){ if(a<b) a=b; }
template<typename T> inline void swap(T &a, T &b){ T c=a; a=b; b=c; }

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

const long double inf = 1./0.;

typedef Point<int> Pi;
typedef Point<long double> Pd;

long double cross(Pd a, Pd b, Pd c, Pd d)
{
	long double f = (d-c).vec_mult(a-c)/(d-c).vec_mult(a-b);
	long double g = (b-a).vec_mult(d-a)/(b-a).vec_mult(d-c);
	return 0<=f && f<=1 && 0<=g && g<=1 ? f : inf;
}

Pd U[1010],L[1010];
long double S[3000];

long double e = 1e-14;

int quadratic(long double A, long double B, long double C, long double &x1, long double &x2)
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
	long double D = SQR(B)-4*A*C;
	if(D<0) return 0;
	D = sqrt(D);
	x1 = (-B-D)/(2*A);
	x2 = (-B+D)/(2*A);
	return D>0 ? 2 : 1;
}

int main()
{
	int Q; scanf("%d",&Q); FOR(q,1,Q)
	{
		int w,l,u,g; scanf("%d%d%d%d",&w,&l,&u,&g);
		REP(i,l) scanf("%Lf%Lf",&L[i].x,&L[i].y);
		REP(i,u) scanf("%Lf%Lf",&U[i].x,&U[i].y);
		int s=0;
		Pd up(-1,0),lp(-1,0); int ui=0,li=0;
		REP(x,w+1)
		{
			long double c1 = (x-lp.x)/(L[li].x-lp.x);
			long double c2 = (x-up.x)/(U[ui].x-up.x);
			//printf("c1=%lf; c2=%lf\n",c1,c2);
			S[s++] = ((1-c2)*up.y+c2*U[ui].y) - ((1-c1)*lp.y+c1*L[li].y);
			//printf("y=%lf\n",S[s-1]);
			if(x>=L[li].x) lp = L[li++];
			if(x>=U[ui].x) up = U[ui++];
		}
		
		printf("Case #%d:\n",q);
		long double f = 0; REP(i,s-1) f += S[i]+S[i+1];
		//printf("f=%lf\n",f);
		f /= g; g--; int i=0; long double acc = 0; 
		REP(i,s)
		{
			long double x0 = 1;
			acc += S[i]+S[i+1];
			while(acc>f && g)
			{
				acc -= f; g--;
				long double l = 0, h = x0;
				while(h-l>1e-7)
				{
					long double m = (l+h)/2;
					if((S[i+1]*(2-m)+S[i]*m)*m>acc) h = m; else l = m; 
				}
				x0 = (h+l)/2;
				printf("%.7Lf\n",i+1-x0);
			}
			/*while(acc>=f && g)
			{
				acc -= f; g--;//printf("acc=%lf\n",acc);
				if(abs(S[i]-S[i+1])<e) x0 = acc/S[i];
				else
				{
					long double a1,a2;
					int n = quadratic(S[i]-S[i+1],2*S[i+1],-acc,a1,a2);
					//printf("a1=%lf; a2=%lf\n",a1,a2);
					x0 = 0<=a1 && a1<=1 ? a1 : a2;
				}
				printf("%.7Lf\n",i+1-x0);
			}*/
		}
	}
	return 0;
}

