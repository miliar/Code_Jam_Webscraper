#include <algorithm>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

int dp[1001][100];
char buff[128];

const int inf = 1000000;

int main( void ) {
   int T;
   scanf( "%d", &T );

   for( int tt = 1; tt <= T; ++tt ) {
      int S;
      scanf( "%d", &S ); gets( buff );
      map<string, int> M;
      
      for( int j = 0; j < S; ++j ) {
         gets( buff );
         M[ string(buff) ] = j;
         dp[0][j] = 0;
      }

      int Q;
      scanf( "%d", &Q ); gets( buff );      

      for( int i = 0; i < Q; ++i ) {
         gets( buff );
         int x = M[ string(buff) ];

         int best = inf;
         for( int j = 0; j < S; ++j )
            best = min( best, dp[i][j] );

         for( int j = 0; j < S; ++j )
            if( j == x ) 
               dp[i+1][j] = inf;
            else
               dp[i+1][j] = min( dp[i][j], best + 1 );
      }

      int ret = inf;
      for( int j = 0; j < S; ++j )
         ret = min( ret, dp[Q][j] );

      printf( "Case #%d: %d\n", tt, ret );
   }
   return 0;
}
