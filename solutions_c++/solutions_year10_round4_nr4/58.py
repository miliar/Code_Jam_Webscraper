#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "D-small-attempt0"

template <typename T> struct Point {
	T x,y;
	Point(T _x=0,T _y=0) : x(_x),y(_y) {}
	void read();
	void swap() { swap(x,y); }
	double len() const;
	Point<double> asDouble() { return Point<double>(x,y); }
	Point<T> norm() const;
	Point<T> ort() const { return Point<T>(y,-x); }
};
template<> void Point<int>::read() { scanf("%d%d",&x,&y); }
template<> void Point<double>::read() { scanf("%lf%lf",&x,&y); }
template <typename T> Point<T> operator- (const Point<T> &a) { return Point<T>(-a.x,-a.y); }
template <typename T> Point<T> operator+ (const Point<T> &a, const Point<T> &b) { return Point<T>(a.x+b.x,a.y+b.y); }
template <typename T> Point<T> operator- (const Point<T> &a, const Point<T> &b) { return Point<T>(a.x-b.x,a.y-b.y); }
template <typename T> Point<T> operator* (const T a, const Point<T> &b) { return Point<T>(a*b.x,a*b.y); }
template <typename T> Point<T> operator* (const Point<T> &b, const T a) { return Point<T>(a*b.x,a*b.y); }
template <typename T> Point<T> operator/ (const Point<T> &b, const T a) { return Point<T>(b.x/a,b.y/a); }
template <typename T> T operator* (const Point<T> &a, const Point<T> &b) { return a.x*b.x+a.y*b.y; }
template <typename T> T operator^ (const Point<T> &a, const Point<T> &b) { return a.x*b.y-a.y*b.x; }
template <typename T> double Point<T>::len() const { return sqrt((double)((*this)*(*this))); }
template <typename T> Point<T> Point<T>::norm() const { return (*this)/len(); }
template <typename T> bool operator< (const Point<T> &a, const Point<T> &b) { return a.x<b.x || a.x==b.x && a.y<b.y; }
bool operator== (const Point<int> &a, const Point<int> &b) { return a.x==b.x && a.y==b.y; }
bool operator!= (const Point<int> &a, const Point<int> &b) { return a.x!=b.x || a.y!=b.y; }
int sign(int x) { if (x==0) return 0; if (x>0) return +1; else return -1; }
int sign(double x) { if (fabs(x)<eps) return 0; if (x>0) return +1; else return -1; }
template<typename T> T sqr(T x) { return x*x; }
typedef Point<double> DPnt;
typedef Point<int> IPnt;
const DPnt INFDPnt(1.0e30,1.0e30);

struct Circle {
	double x,y,r;
	Circle(double _x=0,double _y=0,double _r=0): x(_x),y(_y),r(_r) {}
	DPnt center() const { return DPnt(x,y); }
	int compareTo(const Circle &other) {
		int c1=sign(x-other.x); if (c1!=0) return c1;
		int c2=sign(y-other.y); if (c2!=0) return c2;
		return sign(r-other.r);
	}
};

double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}

int getIntersect(const Circle &A,const Circle &B,DPnt &P,DPnt &Q)
{
	double X1=A.x,Y1=A.y,X2=B.x,Y2=B.y;
	double R1=A.r,R2=B.r;
	double dst=dist(X1,Y1,X2,Y2);
	if (dst>R1+R2+eps || dst<fabs(R1-R2)-eps) return 0;
	if (dst<=eps) return 0;
	//(x-X1)^2+(y-Y1)^2=sqr(R1)=x^2-2*X1*x+X1^2+y^2-2*Y1*y+Y1^2 (1)
	//(x-X2)^2+(y-Y2)^2=sqr(R2)=x^2-2*X2*x+X2^2+y^2-2*Y2*y+Y2^2 (2)
	//(2)-(1):  sqr(R2)-sqr(R1)=2*(X1-X2)*x+2*(Y1-Y2)*y+sqr(X2)-sqr(X1)+sqr(Y2)-sqr(Y1)
	//	 :  (X1-X2)*x+(Y1-Y2)*y-(sqr(X1)-sqr(X2)+sqr(Y1)-sqr(Y2)-sqr(R1)+sqr(R2))/2.0;
	double a=X1-X2;
	double b=Y1-Y2;
	double c=-(a*(X1+X2)+b*(Y1+Y2)-sqr(R1)+sqr(R2))/2.0;
	double CX=X1,CY=Y1;
	//ax+by+c=0
	//(+by+c+aCX)^2+(ay-aCY)^2=(aR)^2
	double x1,y1,x2,y2;
	if (fabs(a)>fabs(b)) {
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) return 0;
		if (delta<0) delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);x2=(-c-b*y2)/a;
		P.x=x1;P.y=y1;
		Q.x=x2;Q.y=y2;
	} else {
		swap(a,b);swap(CX,CY);
		double A=sqr(a)+sqr(b);
		double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
		double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
		double delta=sqr(B)-4*A*C;
		if (delta<-eps) return 0;
		if (delta<0) delta=0;
		delta=sqrt(delta);
		y1=(-B+delta)/(2*A);x1=(-c-b*y1)/a;
		y2=(-B-delta)/(2*A);x2=(-c-b*y2)/a;
		swap(x1,y1);swap(x2,y2);
		swap(a,b);swap(CX,CY);
		P.x=x1;P.y=y1;
		Q.x=x2;Q.y=y2;
	}
	return 2;
}

double cross(const DPnt &a,const DPnt &b,const DPnt &c)
{ return (b-a)^(c-a); }

double psDistance(const DPnt &p,const DPnt &a,const DPnt &b)
{
	double sab=sqr(a.x-b.x)+sqr(a.y-b.y);
	double spa=sqr(p.x-a.x)+sqr(p.y-a.y);
	double spb=sqr(p.x-b.x)+sqr(p.y-b.y);
	if (fabs(spa-spb)<=sab)
		return fabs(cross(p,a,b))/sqrt(sab);
	else
		return sqrt(min(spa,spb));
}
#define N 5555
int n,m;
DPnt a[N];
double rad[N];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		fprintf(stderr,"Test #%d\n",tst+1);

		scanf("%d%d",&n,&m);
		REP(i,n)
			a[i].read();
		printf("Case #%d:",tst+1);
		REP(step,m)
		{
			DPnt center;
			center.read();
			REP(i,n)
				rad[i] = (a[i]-center).len();
			DPnt p1,p2;
			int cnt = getIntersect(Circle(a[0].x,a[0].y,rad[0]),Circle(a[1].x,a[1].y,rad[1]),p1,p2);
			double res;
			if (cnt<2)
			{
				res = 0;
				if ((a[0]-a[1]).len() < max(rad[0],rad[1])+eps)
					res = pi*sqr(min(rad[0],rad[1]));
			}
			else
			{
				res=0;
				REP(i,2)
				{
					DPnt q1 = p1-a[i], q2 = p2-a[i];
					double ang = atan2(q1.y,q1.x)-atan2(q2.y,q2.x);
					while (ang < 0) ang+=2*pi;
					while (ang >= 2*pi) ang-=2*pi;
					ang = min(ang,2*pi-ang);
					if (cross(p1,p2,a[i])*cross(p1,p2,a[1-i]) > 0 && psDistance(a[i],p1,p2)<psDistance(a[1-i],p1,p2))
						ang = 2*pi-ang;
					res += sqr(rad[i])*(ang-sin(ang))/2;
				}
			}
			printf(" %.8lf",res);
		}
		printf("\n");
	}
	return 0;
}