#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int dp[1005][1005];

int solve( int a, int b, int c ) {
  if( a*c >= b ) return 0;
  if( dp[a][b] != -1 ) return dp[a][b];
  int ans = 10000000;
  for( int i = a+1; i*c <= b+c-1; ++i )
    ans = min( ans, 1 + max( solve( a, i, c ), solve( i, b, c ) ) );
  return dp[a][b] = ans;
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int w = 1; w <= t; ++w ) {
    int l, p, c;
    scanf( "%d %d %d", &l, &p, &c );
    memset( dp, -1, sizeof( dp ) );
    int ans = solve( l, p, c );
    printf( "Case #%d: %d\n", w, ans );
  }
  return 0;
}
