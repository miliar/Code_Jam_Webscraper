#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int mini[11][1024];
int cost[11][1024];

const int oo = 1000000000;

void init( int lo, int hi, int depth ) {
   if( lo+1 == hi ) return;
   
   int mid = (lo+hi)/2;
   
   init( lo, mid, depth+1 );
   init( mid, hi, depth+1 );
   
   mini[depth][lo] = min( mini[depth+1][lo], mini[depth+1][mid] );
}

int memo[11][1024][11];

int rec( int lo, int hi, int depth, int skip ) {
   if( skip > mini[depth][lo] ) return oo;
   if( lo+1 == hi ) return 0;
   
   int &ret = memo[depth][lo][skip];
   if( ret >= 0 ) return ret;
   
   int mid = (lo+hi)/2;

   ret = min( cost[depth][lo] + rec( lo, mid, depth+1, skip ) + rec( mid, hi, depth+1, skip ),
              rec( lo, mid, depth+1, skip+1 ) + rec( mid, hi, depth+1, skip+1 ) );
   
   return ret;
} 

int main( void ) {
   int T;
   scanf( "%d", &T );
   for( int tt = 1; tt <= T; ++tt ) {
      int P;
      scanf( "%d", &P );
      for( int i = 0; i < (1<<P); ++i ) 
         scanf( "%d", &mini[P][i] );
      
      for( int d = P-1; d >= 0; --d ) 
         for( int i = 0; i < (1<<P); i += (1<<(P-d)) )
            scanf( "%d", &cost[d][i] );

      init( 0, (1<<P), 0 );

      memset( memo, -1, sizeof memo );
      printf( "Case #%d: %d\n", tt, rec( 0, (1<<P), 0, 0 ) );
   }

   return 0;
}
