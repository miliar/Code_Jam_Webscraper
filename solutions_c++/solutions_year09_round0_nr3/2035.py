#include <cstring>
#include <cstdio>

#define mod 10000

char msg[] = "welcome to code jam";
char s[501];

int n, m, dp[501][30];

int rek( int i, int j ) {
   if( j == 0 ) return 1;
   if( i == 0 ) return 0;

   if( dp[i][j] != -1 ) return dp[i][j];

   int &ref = dp[i][j];
   ref = rek( i-1, j );

   if( s[i-1] == msg[j-1] ) ref += rek( i-1, j-1 );

   ref %= mod;

   return ref;
}


int solve() {
   fgets( s, 501, stdin );
   n = strlen( s );
   
   memset( dp, -1, sizeof dp );

   return rek( n, m );
}

int main(void) {
   m = strlen( msg );

   int T;
   scanf( "%d\n", &T );
   for( int i = 0; i < T; ++i )
      printf( "Case #%d: %04d\n", i+1, solve() );
   return 0;
}
