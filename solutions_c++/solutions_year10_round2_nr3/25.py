#include <cstdio>

#define MAX 500
#define MOD 100003

int memo[2][MAX+1][MAX+1];
int dp[MAX+1][MAX+1];

int rec( int next, int must, int size ) {
   if( size == 0 ) return must == 1;
   if( next == 1 ) return 0;
   if( next == must ) return rec( next-1, size, size-1 );

   int &ret = memo[next][must][size];
   if( ret >= 0 ) return ret;

   ret = rec( next-1, must, size ) + rec( next-1, must, size-1 );
   if( ret >= MOD ) ret -= MOD;
   
   return ret;
}

int main( void ) {
   int curr = 0, prev = 1;
   memo[curr][1][0] = 1;
   for( int next = 2; next <= MAX; ++next ) {
      curr ^= 1;
      prev ^= 1;
      for( int must = 1; must <= next; ++must ) 
         for( int size = 0; size < next; ++size ) {
            if( size == 0 ) memo[curr][must][size] = must == 1;
            else if( next == must ) memo[curr][must][size] = memo[prev][size][size-1];
            else {
               memo[curr][must][size] = memo[prev][must][size] + memo[prev][must][size-1];
               if( memo[curr][must][size] >= MOD ) memo[curr][must][size] -= MOD;
            }
         }

      for( int size = 0; size < next; ++size ) dp[next][size] = memo[curr][next][size];
   }

   int T;
   scanf( "%d", &T );
   for( int tt = 1; tt <= T; ++tt ) {
      int n;
      scanf( "%d", &n );
      int ret = 0;
      for( int size = 1; size <= n-1; ++size ) {
         ret += dp[n][size];
         if( ret >= MOD ) ret -= MOD;
      }
      printf( "Case #%d: %d\n", tt, ret );
   }

   return 0;
}
