#include <cstdio>
#include <cstring>

#include <vector>
#include <algorithm>

using namespace std;

int T, N, S, p;
int t[ 105 ];

int dp[ 105 ][ 105 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%d%d", &N, &S, &p );

    for( int i = 0; i < N; ++i )
      scanf( "%d", &t[i] );

    memset( dp, 0, sizeof dp );

    for( int i = 1; i <= N; ++i ) {
      int max0, max1;

      if( t[i - 1] % 3 == 0 ) {
	max0 = t[i - 1] / 3;
	max1 = ( t[i - 1] == 0 ) ? 0 : max0 + 1;
      }
      else {
	max0 = t[i - 1] / 3 + 1;
	max1 = max0 + 1;
      }

      for( int j = 0; j <= S; ++j ) {
	dp[i][j] = dp[i - 1][j] + ( max0 >= p );

	if( j != 0 ) {
	  if( t[i - 1] % 3 == 0 ) 
	    dp[i][j] = max( dp[i][j], dp[i - 1][j - 1] + ( max1 >= p ) );
	  if( t[i - 1] % 3 == 2 )
	    dp[i][j] = max( dp[i][j], dp[i - 1][j - 1] + ( max1 >= p ) );
	}
      }
    }

    printf( "Case #%d: %d\n", tc, dp[N][S] );
  }

  return 0;
}
