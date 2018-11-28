/* standard includes {{{ */
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <complex>

#include <iostream>
#include <sstream>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/* }}} */

/* defines: REP, FOR, FORD, FORE, FORER, CLEAR, SIZE {{{ */
#define REP(i,n) for (__typeof(n) i=0; i<(n); ++i)
#define FOR(i,a,b) for (__typeof(b) i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (__typeof(a) i=(a); i>=(b); --i)
#define FORE(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define FORER(it,c) for (__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define CLEAR(t,v) memset((t),v,sizeof(t))
#define SIZE(c) ((int)((c).size()))
/* }}} */

/* porovnavanie v realnej aritmetike s presnostou EPS */
#define EPS 1e-10
#define LT(a, b) ((a)+EPS<(b)) /* a < b */
#define GT(a, b) LT(b, a) /* a > b */
#define LQ(a, b) (!GT(a, b)) /* a <= b */
#define GQ(a, b) (!LT(a, b)) /* a >= b */
#define EQ(a, b) (LQ(a, b) && GQ(a, b)) /* a == b */

inline double incir(double x, double y, double R)
{
	return LT(x*x+y*y,R*R);
}

double coo(double x, double y, double R)
{
	if (!incir(x, y, R)) return 0.0;

	double x2 = sqrt(R*R - y*y), dx=x2-x;
	double y2 = sqrt(R*R - x*x), dy=y2-y;

	double phi = asin(y2/R) - acos(x2/R);
	double sc = phi*R*R/2;
//	printf("sc=%.10f\n", sc);

	double a = sqrt(dx*dx+dy*dy)/2;
	double sT = a*sqrt(R*R-a*a);
	double st = dx*dy/2;
//	printf("sT=%.10f\n", sT);
//	printf("st=%.10f\n", st);

//	printf("coo(x=%.6f, y=%.6f, R=%.6f): sc=%.6f, sT=%.6f, st=%.6f; %.6f\n", x, y, R, sc, sT, st, sc-sT+st);

	return sc-sT+st;
}

double soo(double x, double y, double R, double g)
{
	if (!incir(x,y,R)) return 0.0;
	if (incir(x+g,y+g,R)) return g*g;
	return coo(x, y, R) - coo(x+g, y, R) - coo(x, y+g, R);
}

double moo(double R, double r, double g)
{
	if (LQ(g,0.0)) return 0.0;
	if (GQ(r,R)) return 0.0;

//	printf("soo(r,r)=%.10f\n", soo(r,r,R,g));
//	printf("coo(0,0,R)=%.10f\n", coo(0,0,R));
//	exit(0);

	double a=0;
	int x=0, y=0;
	while (LT(r+(g+2*r)*y,R))
	{
		while (LT(r+(g+2*r)*x,R))
		{
			a += soo(r+(g+2*r)*x, r+(g+2*r)*y, R, g);
			x++;
		}
		x=0; y++;
	}
	return a;
}

int main(void)
{
	int cas;
	scanf("%d ", &cas);

	REP(ca,cas)
	{
		double f, R, t, r, g;
		scanf("%lf %lf %lf %lf %lf ", &f, &R, &t, &r, &g);

		double s=moo(R-t-f, r+f, g-2*f);
		double S=M_PI*R*R/4;
//		printf("s=%.10f S=%.10f\n", s, S);
		printf("Case #%d: %.6lf\n", ca+1, 1.0-s/S);
	}

	return 0;
}
