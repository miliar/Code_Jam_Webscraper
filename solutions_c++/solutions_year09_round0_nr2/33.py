#include <cstdio>
#include <cstring>

int R, C;
int h[100][100];
char next;
char a[100][100]; 

const int dr[4] = { -1, 0, 0, 1 };
const int dc[4] = { 0, -1, 1, 0 }; 

char rec( int r, int c ) {
   if( a[r][c] ) return a[r][c];

   int _r = r, _c = c;
   for( int d = 0; d < 4; ++d ) {
      int rr = r + dr[d];
      int cc = c + dc[d];
      if( rr < 0 || rr >= R ) continue;
      if( cc < 0 || cc >= C ) continue;

      if( h[rr][cc] < h[_r][_c] ) { _r = rr; _c = cc; }
   }
   if( _r == r && _c == c ) return a[r][c] = next++;
   return a[r][c] = rec( _r, _c );
}

int main( void ) {
   int T;
   scanf( "%d", &T );
   for( int tt = 1; tt <= T; ++tt ) {
      scanf( "%d%d", &R, &C );
      for( int r = 0; r < R; ++r ) 
         for( int c = 0; c < C; ++c ) 
            scanf( "%d", &h[r][c] );

      memset( a, 0, sizeof a );
      next = 'a';
      
      printf( "Case #%d:\n", tt );
      for( int r = 0; r < R; ++r ) { 
         for( int c = 0; c < C; ++c ) {
            if( c ) printf( " " );
            printf( "%c", rec( r, c ) );
         }
         printf( "\n" );
      }
   }
   return 0;
}
