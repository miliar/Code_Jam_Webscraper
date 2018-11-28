#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef pair< double, double > point;
#define x first
#define y second

const int MAXN = 105;

point a[MAXN], b[MAXN];

double getarea( int x1, int x2, int y1, int y2 ) {
  double area = 0;
  for( int i = x1; i+1 < x2; ++i ) {
    double dx = fabs( a[i+1].x - a[i].x );
    double dy = fabs( a[i+1].y - a[i].y );
    area += min( a[i].y, a[i+1].y )*dx + (dx*dy/2.0);
  }
  for( int i = y1; i+1 < y2; ++i ) {
    double dx = fabs( b[i+1].x - b[i].x );
    double dy = fabs( b[i+1].y - b[i].y );
    area -= min( b[i].y, b[i+1].y )*dx + (dx*dy/2.0);
  }
  return area;
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int w, l, u, g;
    scanf( "%d %d %d %d", &w, &l, &u, &g );

    for( int i = 0; i < l; ++i )
      scanf( "%lf %lf", &b[i].x, &b[i].y );
    for( int i = 0; i < u; ++i )
      scanf( "%lf %lf", &a[i].x, &a[i].y );
    
    printf( "Case #%d:\n", c );
    
    double area = getarea( 0, u, 0, l ) / g;
 
    int cl = 0, cr = 0;
    for( int i = 0; i < g-1; ++i ) {
      double lo = a[cr].x, hi = w;
      
      for( int it = 0; it < 50; ++it ) {
	double mid = ( lo+hi )/2;
	
	int pl = cl, pr = cr;
	while( a[pr].x <= mid ) pr++;
	while( b[pl].x <= mid ) pl++;

	point tmpr = a[pr], tmpl = b[pl];
	double drx = a[pr].x - a[pr-1].x;
	double dry = a[pr].y - a[pr-1].y;
	double dlx = b[pl].x - b[pl-1].x;
	double dly = b[pl].y - b[pl-1].y;

	a[pr] = point( mid, a[pr-1].y + (mid-a[pr-1].x)*dry/drx );
	b[pl] = point( mid, b[pl-1].y + (mid-b[pl-1].x)*dly/dlx );

	if( getarea( cr, pr+1, cl, pl+1 ) <= area ) lo = mid; else
	  hi = mid;
	a[pr] = tmpr, b[pl] = tmpl;
      }
      
      double mid = ( lo+hi )/2;
      
      int pl = cl, pr = cr;
      while( a[pr].x <= mid ) pr++;
      while( b[pl].x <= mid ) pl++;

      double drx = a[pr].x - a[pr-1].x;
      double dry = a[pr].y - a[pr-1].y;
      double dlx = b[pl].x - b[pl-1].x;
      double dly = b[pl].y - b[pl-1].y;
      
      a[pr-1] = point( mid, a[pr-1].y + (mid-a[pr-1].x)*dry/drx );
      b[pl-1] = point( mid, b[pl-1].y + (mid-b[pl-1].x)*dly/dlx );
	
      cl = pl-1, cr = pr-1;
      printf( "%lf\n", mid );
    }
  }
  return 0;
}
