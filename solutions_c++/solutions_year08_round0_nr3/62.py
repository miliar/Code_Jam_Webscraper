// the intarea functions are from http://www.boulder.swri.edu/~buie/idl/downloads/custom/32bit/pixwt.c
#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

/* To compile, link, and use:
     cc -K pic -G -I /opt/local/rsi/idl/external -c pixwt.c
     cc -G -o pixwt pixwt.o

     linkimage,'PIXWT','/gryll/data1/buie/idl/Custom/pixwt',1,'pixwt', $
        max_args=5,min_args=5

     After this statement is executed, pixwt will be drawn from the custom
     routine and not the IDL pixwt.pro file.
*/

/* compute the area within an arc of a circle.  The arc is defined by
 * the two points (x,y0) and (x,y1) in the following manner:  The circle
 * is of radius r and is positioned at the origin.  The origin and each
 * individual point define a line which intersect the circle at some
 * point.  The angle between these two points on the circle measured
 * from y0 to y1 defines the sides of a wedge of the circle.  The area
 * returned is the area of this wedge.  If the area is traversed clockwise
 * the the area is negative, otherwise it is positive. */

static double arc (double x, double y0, double y1, double r)

//double   x;      /* X coordinate of the two points. */
//double   y0;     /* Y coordinate of the first point. */
//double   y1;     /* Y coordinate of the second point. */
//double   r;      /* radius of the circle. */

{
   return( 0.5 * r*r * (atan( y1/x) - atan( y0/x) ) );
}

/* compute the area of a triangle defined by the origin and two points,
 * (x,y0) and (x,y1).  This is a signed area.  If y1 > y0 then the area
 * will be positive, otherwise it will be negative.
 */

static double chord (double x, double y0, double y1)

//double   x;      /* X coordinate of the two points. */
//double   y0;     /* Y coordinate of the first point. */
//double   y1;     /* Y coordinate of the second point. */

{
   return( 0.5 * x * (y1-y0) );
}

/* Compute the area of intersection between a triangle and a circle.
 * The circle is centered at the origin and has a radius of r.  The
 * triangle has verticies at the origin and at (x,y0) and (x,y1).
 * This is a signed area.  The path is traversed from y0 to y1.  If
 * this path takes you clockwise the area will be negative.
 */

static double oneside (double x, double y0, double y1, double r)

//double   x;      /* X coordinate of the two points. */
//double   y0,y1;  /* Y coordinates of the two points. */
//double   r;      /* radius of the circle */

{
double   yh;

   if (x == 0) return(0);
   else if ( fabs(x) >=  r ) return( arc(x,y0,y1,r) ); 
   else {
      yh = sqrt(r*r-x*x);
      if (y0 <= -yh) {
         if (y1 <= -yh) return( arc(x,y0,y1,r) );
         else if (y1 <= yh) return( arc(x,y0,-yh,r) + chord(x,-yh,y1) );
         else return( arc(x,y0,-yh,r) + chord(x,-yh,yh)
                                      + arc(x,yh,y1,r) ); }
      else if (y0 < yh) {
         if (y1 < -yh) return( chord(x,y0,-yh) + arc(x,-yh,y1,r) );
         else if (y1 <= yh) return( chord(x,y0,y1) );
         else return( chord(x,y0,yh) + arc(x,yh,y1,r) ); }
      else {
         if (y1<-yh) return( arc(x,y0,yh,r) + chord(x,yh,-yh)
                                            + arc(x,-yh,y1,r) );
         else if (y1 < yh) return( arc(x,y0,yh,r) + chord(x,yh,y1) );
         else return( arc(x,y0,y1,r) ); }
   }
}

/* Compute the area of overlap between a circle and a rectangle. */

double intarea (double xc, double yc, double r, double x0, double x1, double y0, double y1)

//double   xc,yc;   /* Center of the circle. */
//double   r;       /* Radius of the circle. */
//double   x0,y0;   /* Corner of the rectangle. */
//double   x1,y1;   /* Opposite corner of the rectangle. */

{

x0 -= xc;   y0 -= yc;  /* Shift the objects so that circle is at the orgin. */
x1 -= xc;   y1 -= yc;

return( oneside(x1,y0,y1,r) + oneside(y1,-x1,-x0,r)
        + oneside(-x0,-y1,-y0,r) + oneside(-y0,x0,x1,r) );

}

int main()
{
	int N;
	scanf("%d", &N);
	for (int nn = 0; nn < N; ++nn) {
		double f, R, t, r, g;
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		double allArea = M_PI * R*R;
		double safeArea = 0.0;
		if (R-t-f <= 0.0 || g <= f*2.0) {
			printf("Case #%d: 1.000000\n", nn+1);
			continue;
		}
		for (double y = r; y <= R; y += g+2*r) {
			for (double x = r; x <= R; x += g+2*r) {
				safeArea += intarea(0.0, 0.0, R-t-f, x+f, x+g-f, y+f, y+g-f);
				//printf("(%0.2lf,%0.2lf) => %lf (%lf %lf %lf %lf %lf)\n", x, y, intarea(0.0, 0.0, R-t-f, x+f, x+g-f, y+f, y+g-f), R-t-f, x+f, x+g-f, y+f, y+g-f);
			}
		}
		safeArea *= 4.0;
		printf("Case #%d: %0.7lf\n", nn+1, 1.0 - safeArea/allArea);
	}
	return 0;
}
