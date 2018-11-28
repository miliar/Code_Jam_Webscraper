#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>

using namespace std;

const int n = 100;

int a[105], c[105];
int r[105][105][105];
queue< int > Q;

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int cc = 1; cc <= t; ++cc ) {
    memset( r, 0, sizeof( r ) );
    while( !Q.empty() ) Q.pop();
    
    int q;
    scanf( "%d", &q );
    for( int i = 0; i < q; ++i ) {
      char s[10];
      scanf( " %s %d", s, a+i );
      c[i] = ( s[0] == 'O' );
    }

    int ans = -1;
    Q.push( 0 ), Q.push( 1 ), Q.push( 1 );
    r[0][1][1] = 1;
    while( !Q.empty() ) {
      int p = Q.front(); Q.pop();
      int x = Q.front(); Q.pop();
      int y = Q.front(); Q.pop();

      if( p == q ) { ans = r[p][x][y]-1; break; }
      for( int i = -1; i <= 1; ++i ) {
	int X = x+i;
	if( X < 1 || X > n ) continue;
	for( int j = -1; j <= 1; ++j ) {
	  int Y = y+j;
	  if( Y < 1 || Y > n ) continue;
	  
	  int P = p;
	  if( c[p] == 0 && a[p] == x && a[p] == X ) P++;
	  if( c[p] == 1 && a[p] == y && a[p] == Y ) P++;
	  if( r[P][X][Y] == 0 ) {
	    Q.push( P ), Q.push( X ), Q.push( Y );
	    r[P][X][Y] = r[p][x][y] + 1;
	  }
	}
      }
    }

    printf( "Case #%d: %d\n", cc, ans );
  }
  return 0;
}
