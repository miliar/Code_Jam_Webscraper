#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <list>

using namespace std;

const int MaxN = 520;
const int inf = 1000000000;

struct Fenwick {
  int L[ MaxN ][ MaxN ];
  int N;
  Fenwick() {};
  void init( int n ) {
    N = n;
    for( int i = 0; i <= n; ++i )
      for( int j = 0; j <= n; ++j )
	L[i][j] = 0;
  }
  void add( int x, int y ) {
    for( ++x; x <= N; x += x&-x )
      for( int Y = y+1; Y <= N; Y += Y&-Y )
	L[x][Y]++;
  }
  int sumk( int x, int y ) {
    int r = 0;
    for( ++x; x; x -= x&-x )
      for( int Y = y+1; Y; Y -= Y&-Y )
	r += L[x][Y];
    return r;
  }
  int sum( int x, int y, int k ) {
    --x, --y;
    return sumk( x+k, y+k ) - sumk( x+k, y ) - sumk( x, y+k ) + sumk( x, y );
  }
};

int a[ MaxN ][ MaxN ];
int dp[ MaxN ][ MaxN ];
int ans[ MaxN ];

Fenwick L;

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n, m, x;
    scanf( "%d %d", &n, &m );
    for( int i = 0; i < n; ++i ) {
      char s[130];
      scanf( "%s", s );
      for( int j = 0; j < m; j += 4 ) {
	if( isdigit( s[j/4] ) ) x = s[j/4]-'0'; else
	  x = s[j/4]-'A' + 10;
	for( int k = 3; k >= 0; --k )
	  a[i][j+3-k] = (x>>k)&1;
      }
    }

    for( int i = 0; i <= n; ++i )
      for( int j = 0; j <= m; ++j )
	dp[i][j] = -inf;

    for( int i = n-1; i >= 0; --i )
      for( int j = m-1; j >= 0; --j ) {
	if( a[i][j] != a[i+1][j] && a[i][j] != a[i][j+1] && a[i][j] == a[i+1][j+1] )
	  dp[i][j] = min( min( dp[i+1][j], dp[i][j+1] ), dp[i+1][j+1] ) + 1;
	dp[i][j] = max( dp[i][j], 1 );
      }
    
    L.init( max( n, m ) );
    memset( ans, 0, sizeof( ans ) );
    
    for( int k = min( n, m ); k >= 2; --k )
      for( int i = 0; i+k <= n; ++i )
	for( int j = 0; j+k <= m; ++j )
	  if( dp[i][j] >= k && L.sum( i, j, k ) == 0 ) {
	    ans[k]++;
	    for( int x = 0; x < k; ++x )
	      for( int y = 0; y < k; ++y )
		L.add( i+x, j+y );
	  }
    
    ans[1] += n*m - L.sumk( n-1, m-1 );
    int sum = 0;
    for( int i = 1; i <= n; ++i )
      if( ans[i] ) sum++;

    printf( "Case #%d: %d\n", c, sum );
    for( int i = n; i >= 1; --i )
      if( ans[i] ) printf( "%d %d\n", i, ans[i] );
  }
  return 0;
}
