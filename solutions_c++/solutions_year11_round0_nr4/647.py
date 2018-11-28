#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long double ldouble;

int T, N;
int a[ 1001 ];

ldouble d[ 1001 ];
ldouble dp[ 1001 ];
ldouble p[ 1001 ][ 1001 ];

int main( void )
{
  d[0] = 1.0;
  d[1] = 0.0;

  for( int i = 2; i <= 1000; ++i ) {
    d[i] = 1.0; ldouble f = 1.0;
    for( int j = 1; j <= i; ++j ) {
      f /= ldouble( j );
      d[i] -= d[i-j] * f;
    }
  }
  
  for( int i = 1; i <= 1000; ++i ) {
    ldouble f = 1.0;
    for( int j = 1; j <= i; ++j ) {
      f /= ldouble( j );
      p[i][j] = d[i-j] * f;
    }
  }

  for( int i = 1; i <= 1000; ++i ) {
    for( int j = 1; j < i; ++j ) {
      dp[i] += p[i][j] * dp[i-j];
    }
    dp[i] = ( dp[i] + 1.0 ) / ( 1.0 - d[i] );
  }


  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );

    int n = N;

    for( int i = 0; i < N; ++i ) {
      scanf( "%d", a+i ); --a[i];
      if( a[i] == i ) --n;
    }

    printf( "Case #%d: ", tc );
    printf( "%.6Lf\n", dp[n] );
  }

  return 0;
}
