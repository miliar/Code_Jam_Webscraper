#include <cstdio>

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      int xor_all = 0;
      int sum_all = 0;
      int best = 1000000000;

      int n;
      scanf( "%d", &n );
      for( ; n > 0; --n ) {
         int x;
         scanf( "%d", &x );
         xor_all ^= x;
         sum_all += x;
         if( x < best ) best = x;
      }

      printf( "Case #%d: ", t );
      if( xor_all != 0 ) {
         puts( "NO" );
      } else {
         printf( "%d\n", sum_all - best );
      }
   }
   return 0;
}

