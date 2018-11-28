#include <cstdio>
#include <cstring>

using namespace std;

const int MaxN = 10003;
const int INF = 1000000000;

int dp[ 103 ][ 103 ];
int a[ MaxN ];
int b[ MaxN ];
int c[ MaxN ];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    memset( c, 0, sizeof( c ) );
    int n, q;
    scanf( "%d %d", &n, &q );
    a[0] = 0, a[q+1] = n+1;
    for( int i = 1; i <= q; ++i )
      scanf( "%d", a + i );
    q += 2;

    memset( dp, 63, sizeof( dp ) );
    for( int i = 0; i < q; ++i )
      dp[i][i+1] = 0;
    for( int k = 2; k < q; ++k )
      for( int i = 0; i+k < q; ++i ) {
	int j = i+k;
	for( int l = i+1; l < j; ++l )
	  dp[i][j] <?= ( dp[i][l]+dp[l][j] );
	dp[i][j] += ( a[j]-a[i]-2 );
      }
    printf( "Case #%d: %d\n", d, dp[0][q-1] );
  }
  return 0;
}
