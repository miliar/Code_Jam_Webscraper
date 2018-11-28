#include <cstdio>

#include <algorithm>
using namespace std;

int n;
int type[101];
int pos[101];
int dp[101];
int prev[101];

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      scanf( "%d", &n );
      for( int i = 1; i <= n; ++i ) {
         char c;
         scanf( " %c %d", &c, &pos[i] );
         type[i] = (c == 'O');
      }
      pos[0] = 1;

      for( int i = 1; i <= n; ++i ) {
         prev[i] = 0;
         for( int j = 1; j < i; ++j )
            if( type[i] == type[j] )
               prev[i] = j;
      }

      dp[0] = 0;
      for( int i = 1; i <= n; ++i ) {
         if( i == 0 || type[i] == type[i-1] ) {
            dp[i] = dp[i-1] + abs( pos[i] - pos[i-1] ) + 1;
         } else {
            dp[i] = max( dp[i-1], dp[prev[i]] + abs( pos[i] - pos[prev[i]] ) ) + 1;
         }
      }
      printf( "Case #%d: %d\n", t, dp[n] );
   }
   return 0;
}

