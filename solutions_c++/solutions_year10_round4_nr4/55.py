#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

// {{{ gprintf for debugging
bool gprintf(int debug,const char *format,...) {
	if(DBG & debug) {
		va_list	listpointer;

		va_start(listpointer, format);
		vfprintf(stderr,format,listpointer);
		va_end(listpointer);

		return true;
	}
	else
		return false;
}
// }}}

double get_area(double x1,double y1,double x2,double y2,double r1,double r2) {
	double	a1,a2;
	double	ta1,ta2;
	double	th1,th2;
	double	x,d,h;

	d = hypot(y2 - y1,x2 - x1);
	x = (r1 * r1 - r2 * r2 + d * d) / (2 * d);
	h = sqrt(r1 * r1 - x * x);

	th1 = atan2(h,x);
	th2 = atan2(h,d - x);

	ta1 = 0.5 * h * x;
	ta2 = 0.5 * h * (d - x);

	a1 = 0.5 * th1 * r1 * r1;
	a2 = 0.5 * th2 * r2 * r2;

	a1 -= ta1;
	a2 -= ta2;

	return 2 * (a1 + a2);
}

int main()
{
	int	T,cs;
	double	p1x,p1y,p2x,p2y;
	double	x,y;
	int	N,M;
	int	i,j;

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&N,&M);

		assert(N== 2);

		scanf("%lf %lf",&p1x,&p1y);
		scanf("%lf %lf",&p2x,&p2y);

		printf("Case #%d:",cs);

		while(M--) {
			scanf("%lf %lf",&x,&y);

			printf(" %.7lf",get_area(p1x,p1y,p2x,p2y,hypot(y - p1y,x - p1x),hypot(y - p2y,x - p2x)));
		}

		printf("\n");
	}

	return 0;
}
