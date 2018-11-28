#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int dp[101][101];
int a[101], c[3];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int cn = 1; cn <= t; ++cn ) {
    int n, s, p;
    scanf( "%d %d %d", &n, &s, &p );
    for( int i = 0; i < n; ++i )
      scanf( "%d", a+i );
    
    memset( dp, 0, sizeof( dp ) );
    for( int i = 0; i < n; ++i )
      for( int j = 0; j <= i; ++j ) {
        int c = ( (a[i]+2)/3 ) >= p;
        int d = ( 1 + ((a[i]+1)/3) ) >= p;
        if( a[i] <= 1 ) d = 0;
        dp[i+1][j] = max( dp[i+1][j], dp[i][j] + c );
        dp[i+1][j+1] = max( dp[i+1][j+1], dp[i][j] + d  );
      }
        
    printf( "Case #%d: %d\n", cn, dp[n][s] );
  }
  return 0;
}
