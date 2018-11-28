#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int oo = 1000000000;

struct chick {
   int x, v;
} a[50];
int N, K, B, T;

int memo[51][51];

int rec( int i, int k ) {
   if( k == 0 ) return 0;
   if( i < 0 ) return oo;
   
   int &ret = memo[i][k];
   if( ret != -1 ) return ret;

   ret = oo;
   if( a[i].x + a[i].v*T >= B ) ret = min( ret, rec( i-1, k-1 ) );
   else ret = min( ret, k + rec( i-1, k ) );
   return ret;
}

int main( void ) {
   int C;
   scanf( "%d", &C );
   for( int cc = 1; cc <= C; ++cc ) {
      scanf( "%d%d%d%d", &N, &K, &B, &T );
      for( int i = 0; i < N; ++i ) scanf( "%d", &a[i].x );
      for( int i = 0; i < N; ++i ) scanf( "%d", &a[i].v );
      memset( memo, -1, sizeof memo );

      int ret = rec( N-1, K );
      if( ret == oo ) printf( "Case #%d: IMPOSSIBLE\n", cc, ret );
      else printf( "Case #%d: %d\n", cc, ret );
   }
   return 0;
}
 
