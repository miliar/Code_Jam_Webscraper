#include <cstdio>
#include <cstring>

const int dx[] = { 0, 1, 1, 0 };
const int dy[] = { 0, 0, 1, 1 };

int T, R, C;
char m[ 100 ][ 100 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%d", &R, &C );

    for( int i = 0; i < R; ++i ) {
      scanf( "%s", m[i] );
    }

    for( int i = 0; i < R-1; ++i ) {
      for( int j = 0; j < C-1; ++j ) {
	bool ok = 1;

	for( int d = 0; d < 4; ++d ) {
	  if( m[i+dx[d]][j+dy[d]] != '#' ) ok = 0;
	}

	if( ok ) {
	  m[i][j] = '/';
	  m[i+1][j] = '\\';
	  m[i+1][j+1] = '/';
	  m[i][j+1] = '\\';
	}
      }
    }

    bool done = 1;
    
    for( int i = 0; i < R; ++i ) {
      for( int j = 0; j < C; ++j ) {
	if( m[i][j] == '#' ) done = 0;
      }
    }

    printf( "Case #%d:\n", tc );

    if( !done ) printf( "Impossible\n" );

    else for( int i = 0; i < R; ++i )
      printf( "%s\n", m[i] );

  }

  return 0;
}

