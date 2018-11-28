#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long llint;

const int MAXN = 404;
const int inf = 1000000000;

int d[MAXN][MAXN];
int e[MAXN][MAXN];
llint f[MAXN];

int ans, n, m;

void go( int x, int dd, llint s, llint m ) {
  if( d[x][1] == 1 ) {
    int cnt = 0;
    for( int i = 0; i < n; ++i )
      if( m&(1LL<<i) ) cnt++;
    if( cnt > ans ) ans = cnt;
    return;
  }

  for( int i = 0; i < n; ++i )
    if( e[x][i] && dd-1 == d[i][1] ) {
      llint ss = s|(1LL<<i);
      llint mm = m|f[i];
      mm &= ~ss;
      go( i, dd-1, ss, mm );
    }
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    scanf( "%d %d", &n, &m );
    memset( d, 63, sizeof( d ) );
    memset( e, 0, sizeof( e ) );

    for( int i = 0; i < m; ++i ) {
      int a, b;
      scanf( "%d,%d", &a, &b );
      d[a][b] = d[b][a] = 1;
      e[a][b] = e[b][a] = 1;
    }
    for( int i = 0; i < n; ++i )
      d[i][i] = 0;

    for( int k = 0; k < n; ++k )
      for( int i = 0; i < n; ++i )
	for( int j = 0; j < n; ++j )
	  d[i][j] = min( d[i][j], d[i][k] + d[k][j] );
    
    for( int i = 0; i < n; ++i ) {
      f[i] = 0;
      for( int j = 0; j < n; ++j )
	if( e[i][j] ) f[i] |= (1LL<<j);
    }

    ans = 0;
    go( 0, d[0][1], (1<<0), f[0] );

    printf( "Case #%d: %d %d\n", c, d[0][1]-1, ans );
  }
  return 0;
}
