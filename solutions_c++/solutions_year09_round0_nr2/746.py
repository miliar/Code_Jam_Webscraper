#include <cstdio>
#include <cstring>

using namespace std;

const int MaxN = 105;

int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };

char r[ MaxN ][ MaxN ];
int a[ MaxN ][ MaxN ];
int n, m, cnt;

char solve( int x, int y ) {
  if( r[x][y] != -1 ) return r[x][y];
  
  int i = x, j = y;
  for( int d = 0; d < 4; ++d ) {
    int X = x+dx[d], Y = y+dy[d];
    if( X < 0 || X >= n || Y < 0 || Y >= m ) continue;
    if( a[X][Y] < a[i][j] ) i = X, j = Y;
  }
  if( i == x && j == y ) return r[x][y] = 'a' + cnt++;
  return r[x][y] = solve( i, j );
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 0; c < t; ++c ) {
    scanf( "%d %d", &n, &m );
    for( int i = 0; i < n; ++i )
      for( int j = 0; j < m; ++j )
	scanf( "%d", a[i] + j );

    cnt = 0;
    memset( r, -1, sizeof( r ) );
    for( int i = 0; i < n; ++i )
      for( int j = 0; j < m; ++j )
	solve( i, j );

    printf( "Case #%d:\n", c+1 );
    for( int i = 0; i < n; ++i ) {
      for( int j = 0; j < m; ++j ) {
	if( j ) putchar( ' ' );
	putchar( r[i][j] );
      }
      putchar( '\n' );
    }
  }
  return 0;
}
