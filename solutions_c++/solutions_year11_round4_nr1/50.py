#include <cstdio>
#include <algorithm>

using namespace std;

typedef pair< int, int > par;
#define x first
#define y second

par f[1005];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int x, s, r, t, n;
    scanf( "%d %d %d %d %d", &x, &s, &r, &t, &n );

    int tot = x;
    for( int i = 0; i < n; ++i ) {
      int a, b, w;
      scanf( "%d %d %d", &a, &b, &w );
      f[i] = par( w, b-a );
      tot -= b-a;
    }
    f[n++] = par( 0, tot );
    sort( f, f + n );

    double T = t;
    double ans = 0;
    for( int i = 0; i < n; ++i )
      if( (r+f[i].x)*T >= f[i].y ) {
	double q = double(f[i].y)/(r+f[i].x);
	ans += q, T -= q;
      } else {
	double z = (r+f[i].x)*T;
	ans += T + (double(f[i].y-z)/(s+f[i].x)), T = 0;
      }
    printf( "Case #%d: %.8lf\n", c, ans );
  }
  return 0;
}
