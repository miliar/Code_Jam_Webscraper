#include <cstdio>

int R, C;
char g[55][55];

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      scanf( "%d %d", &R, &C );
      for( int i = 0; i < R; ++i )
         scanf( "%s", g[i] );

      for( int i = 0; i+1 < R; ++i )
         for( int j = 0; j+1 < C; ++j )
            if( g[i][j] == '#' && g[i+1][j] == '#' && g[i][j+1] == '#' && g[i+1][j+1] == '#' ) {
               g[i][j] = '/';
               g[i][j+1] = '\\';
               g[i+1][j] = '\\';
               g[i+1][j+1] = '/';
            }

      int ok = 1;
      for( int i = 0; i < R; ++i )
         for( int j = 0; j < C; ++j )
            if( g[i][j] == '#' ) ok = 0;

      printf( "Case #%d:\n", t );
      if( ok ) {
         for( int i = 0; i < R; ++i ) puts( g[i] );
      } else {
         puts( "Impossible" );
      }
   }
   return 0;
}

