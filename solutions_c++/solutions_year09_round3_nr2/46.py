#include <cstdio>
#include <cmath>

using namespace std;

int n, x, y, z;
int vx, vy, vz;

inline double sqr( double x ) { return x*x; }
inline double get( double t ) { return sqr( ( x+vx*t )/n )+sqr( ( y+vy*t )/n )+sqr( ( z+vz*t )/n ); }

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    scanf( "%d", &n );
    x = y = z = vx = vy = vz = 0;
    for( int i = 0; i < n; ++i ) {
      int X, Y, Z, Vx, Vy, Vz;
      scanf( "%d %d %d %d %d %d", &X, &Y, &Z, &Vx, &Vy, &Vz );
      x += X, y += Y, z += Z;
      vx += Vx, vy += Vy, vz += Vz;
    }

    double lo = 0, hi = 1e20;
    for( int it = 0; it < 10000; ++it ) {
      double m1 = lo + ( hi-lo )/3.0;
      double m2 = hi - ( hi-lo )/3.0;
      if( get( m1 ) > get( m2 ) ) lo = m1; else
	hi = m2;
    }

    printf( "Case #%d: %.8lf %.8lf\n", d, sqrt( get( lo ) ), lo );
  }
  return 0;
}
