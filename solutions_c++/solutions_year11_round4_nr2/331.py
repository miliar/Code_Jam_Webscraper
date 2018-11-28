#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

inline bool eq( double a, double b ) {
  return ( fabs( a - b ) <= 1e-9 );
}

int T, R, C, D;
char m[ 505 ][ 505 ];

double dsum[ 505 ][ 505 ];
double pxsum[ 505 ][ 505 ];
double pysum[ 505 ][ 505 ];

inline double nsum( int x, int y, int a, double s[ 505 ][ 505 ] ) {
  double ret = s[x+a-1][y+a-1];
  if( x ) ret -= s[x-1][y+a-1];
  if( y ) ret -= s[x+a-1][y-1];
  if( x && y ) ret += s[x-1][y-1];
  return ret;
}

inline double sum( int x, int y, int a, double s[ 505 ][ 505 ] ) {
  double ret = nsum( x, y, a, s );
  ret -= nsum( x, y, 1, s );
  ret -= nsum( x+a-1, y, 1, s );
  ret -= nsum( x, y+a-1, 1, s );
  ret -= nsum( x+a-1, y+a-1, 1, s );
  return ret;
}

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%d%d", &R, &C, &D );

    for( int i = 0; i < R; ++i )
      scanf( "%s", m[i] );

    for( int i = 0; i < R; ++i ) {
      for( int j = 0; j < C; ++j ) {
	dsum[i][j] = m[i][j]-'0'+D;
	pxsum[i][j] = ( 0.5+i )*double( m[i][j]-'0'+D );
	pysum[i][j] = ( 0.5+j )*double( m[i][j]-'0'+D );

	if( i ) {
	  dsum[i][j] += dsum[i-1][j];
	  pxsum[i][j] += pxsum[i-1][j];
	  pysum[i][j] += pysum[i-1][j];
	}
	
	if( j ) {
	  dsum[i][j] += dsum[i][j-1];
	  pxsum[i][j] += pxsum[i][j-1];
	  pysum[i][j] += pysum[i][j-1];
	}
	
	if( i && j ) {
	  dsum[i][j] -= dsum[i-1][j-1];
	  pxsum[i][j] -= pxsum[i-1][j-1];
	  pysum[i][j] -= pysum[i-1][j-1];
	}
      }
    }

    int Sol = 0;

    for( int i = 0; i < R; ++i ) {
      for( int j = 0; j < C; ++j ) {
	for( int k = 3; i+k <= R && j+k <= C; ++k ) {
	  double mx = 0.5*k + i;
	  double my = 0.5*k + j;
	  double sx = sum( i, j, k, pxsum ) - mx*sum( i, j, k, dsum );
	  double sy = sum( i, j, k, pysum ) - my*sum( i, j, k, dsum );
	  if( eq( sx, 0.0 ) && eq( sy, 0.0 ) )
	    Sol = max( Sol, k );
	}
      }
    }

    printf( "Case #%d: ", tc );
    if( Sol ) printf( "%d\n", Sol );
    else printf( "IMPOSSIBLE\n" );
  }

  return 0;
}
