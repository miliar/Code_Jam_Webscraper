#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int mat[111][111];

int main( void ) {
  int tc; scanf( "%d", &tc );
  for( int t = 1; t <= tc; ++t ) {
    int n; scanf( "%d", &n );
    memset( mat, 0, sizeof mat );
    for( int i = 0; i < n; ++i ) {
      int x1, y1; scanf( "%d %d", &x1, &y1 );
      int x2, y2; scanf( "%d %d", &x2, &y2 );
      for( int x = x1; x <= x2; ++x )
        for( int y = y1; y <= y2; ++y )
          mat[x][y] = 1;
    }

    int ans = 0;
    for( ; ; ++ans ) {
      bool ok = false;
      for( int i = 100; i >= 1; --i )
        for( int j = 100; j >= 1; --j ) {
          if( mat[i][j] ) ok = true;
          if( mat[i-1][j] + mat[i][j-1] == 0 ) mat[i][j] = 0;
          if( mat[i-1][j] + mat[i][j-1] == 2 ) mat[i][j] = 1;
        }
      if( !ok ) break;
    }

    printf( "Case #%d: %d\n", t, ans );
  }
  return 0;
}

