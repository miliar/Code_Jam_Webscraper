#include <cstdio>

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      int n, m = 0;
      scanf( "%d", &n );
      for( int i = 1; i <= n; ++i ) {
         int x;
         scanf( "%d", &x );
         if( x != i ) ++m;
      }
      printf( "Case #%d: %lf\n", t, m <= 1 ? 0.0 : 1.0*m );
   }

   return 0;
}

