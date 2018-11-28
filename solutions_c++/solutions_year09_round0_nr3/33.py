#include <cstdio>

int dp[20];
char buff[512];
char *a = "#welcome to code jam";

int main( void ) {
   int T;
   scanf( "%d", &T ); gets( buff );
   for( int tt = 1; tt <= T; ++tt ) {
      gets( buff );
 
      dp[0] = 1;
      for( int i = 1; i < 20; ++i ) dp[i] = 0;

      for( char *p = buff; *p; ++p )
         for( int i = 19; i > 0; --i )
            dp[i] = (dp[i] + dp[i-1] * (*p == a[i])) % 10000;

      printf( "Case #%d: %04d\n", tt, dp[19] );
   }
   return 0;
}
