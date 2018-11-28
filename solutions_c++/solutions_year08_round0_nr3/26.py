/** OK, 17.7.2008 */

#include <stdio.h>
#include <string.h>
#include <math.h>

const double PI = 3.14159265358979323846;

double f, R, t, r, g;

double Rtf;     // R-t-f
double RtfRtf;  // Rtf * Rtf
double size;    // square size (g - 2f)
double full;    // full square area (size^2)
double step;    // square step (g + 2r)
double origin;  // 1st square origin (r + f)

double segArea ( double chord )   // radius = Rtf
{
  return( RtfRtf * asin( 0.5 * chord / Rtf ) - 0.25 * chord * sqrt( 4.0 * RtfRtf - chord * chord ) );
}

inline bool isInside ( double x, double y )
{
  return( x * x + y * y < RtfRtf );
}

inline double leg ( double x )
{
  return( sqrt( RtfRtf - x * x ) );
}

inline double dist ( double x1, double y1, double x2, double y2 )
{
  x1 -= x2;
  y1 -= y2;
  return sqrt( x1 * x1 + y1 * y1 );
}

bool readInstance ( void )
{
  if ( scanf( "%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g ) != 5 )
    return false;

  Rtf = R - t - f;
  RtfRtf = Rtf * Rtf;
  size = g - f - f;
  full = size * size;
  step = g + r + r;
  origin = r + f;

  return true;
}

void solveInstance ( int order )
{
  double area = 0.0;   // healthy area
  if ( size > 0.0 )
  {
    double x, y, x1, y1, x2, y2;

    for ( y = origin; isInside( origin, y ); y += step )
      for ( x = origin; isInside( x, y ); x += step )
        if ( isInside( x + size, y + size ) )
          area += full;
        else
          if ( isInside( x + size, y ) )
            if ( isInside( x, y + size ) )
            {                               // cut the UR corner
              x1 = leg( y + size );
              y1 = leg( x + size );
              area += (full - 0.5 * (x + size - x1) * (y + size - y1) + segArea( dist( x1, y + size, x + size, y1 ) ) );
            }
            else
            {                               // cut the bottom
              y1 = leg( x );
              y2 = leg( x + size );
              area += (0.5 * size * (y1 - y + y2 - y) + segArea( dist( x, y1, x + size, y2 ) ) );
            }
          else
            if ( isInside( x, y + size ) )
            {                               // cut the right wall
              x1 = leg( y );
              x2 = leg( y + size );
              area += (0.5 * size * (x1 - x + x2 - x) + segArea( dist( x1, y, x2, y + size ) ) );
            }
            else
            {                               // only the LL corner
              x1 = leg( y );
              y1 = leg( x );
              area += (0.5 * (x1 - x) * (y1 - y) + segArea( dist( x1, y, x, y1 ) ) );
            }
  }

  printf( "Case #%d: %.6f\n", order, 1.0 - (4.0 * area) / (PI * R * R) );
  fflush( stdout );
}

int main ( void )
{
  int n;
  if ( scanf( "%d", &n ) != 1 ||
       n < 1 ) return 1;

  for ( int i = 0; i++ < n; )
  {
    if ( !readInstance() ) return 1;
    solveInstance( i );
  }

  return 0;
}
