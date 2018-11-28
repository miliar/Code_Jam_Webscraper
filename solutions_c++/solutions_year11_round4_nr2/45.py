#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long llint;

const int MAXN = 505;

llint ax[MAXN][MAXN];
llint ay[MAXN][MAXN];
llint am[MAXN][MAXN];

llint sx[MAXN][MAXN];
llint sy[MAXN][MAXN];
llint s[MAXN][MAXN];
char str[MAXN];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n, m, d;
    scanf( "%d %d %d", &n, &m, &d );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", str );
      for( int j = 0; j < m; ++j ) {
	s[i][j] = d + ( str[j] - '0' );
	sx[i][j] = i*s[i][j], sy[i][j] = j*s[i][j];
	ax[i][j] = sx[i][j], ay[i][j] = sy[i][j], am[i][j] = s[i][j];

	if( i > 0 ) {
	  s[i][j] += s[i-1][j];
	  sx[i][j] += sx[i-1][j];
	  sy[i][j] += sy[i-1][j];
	}
	
	if( j > 0 ) {
	  s[i][j] += s[i][j-1];
	  sx[i][j] += sx[i][j-1];
	  sy[i][j] += sy[i][j-1];
	}
	
	if( i > 0 && j > 0 ) {
	  s[i][j] -= s[i-1][j-1];
	  sx[i][j] -= sx[i-1][j-1];
	  sy[i][j] -= sy[i-1][j-1];
	}
      }
    }
    
    int ans = -1;
    for( int k = min( n, m ); k >= 3 && ans == -1; --k )
      for( int i = 0; i+k <= n; ++i )
	for( int j = 0; j+k <= m; ++j ) {
	  llint px = sx[i+k-1][j+k-1], py = sy[i+k-1][j+k-1], pm = s[i+k-1][j+k-1];
	  if( i > 0 ) {
	    px -= sx[i-1][j+k-1];
	    py -= sy[i-1][j+k-1];
	    pm -= s[i-1][j+k-1];
	  }
	  if( j > 0 ) {
	    px -= sx[i+k-1][j-1];
	    py -= sy[i+k-1][j-1];
	    pm -= s[i+k-1][j-1];
	  }
	  if( i > 0 && j > 0 ) {
	    px += sx[i-1][j-1];
	    py += sy[i-1][j-1];
	    pm += s[i-1][j-1];
	  }

	  px -= ax[i][j] + ax[i+k-1][j] + ax[i][j+k-1] + ax[i+k-1][j+k-1];
	  py -= ay[i][j] + ay[i+k-1][j] + ay[i][j+k-1] + ay[i+k-1][j+k-1];
	  pm -= am[i][j] + am[i+k-1][j] + am[i][j+k-1] + am[i+k-1][j+k-1];

	  // printf( "%d %d %d, %lld %lld %lld\n", i, j, k, px, py, pm );
	  if( 2*px == pm*(i+i+k-1) && 2*py == pm*(j+j+k-1) ) { ans = k; break; }
	}

    printf( "Case #%d: ", c );
    if( ans == -1 ) puts( "IMPOSSIBLE" ); else
      printf( "%d\n", ans );
  }
  return 0;
}
