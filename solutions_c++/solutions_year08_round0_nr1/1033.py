#include <cstdio>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <string>
using namespace std;

const int NULA = 0;
const int MAXSERVER = 102;
const int MAXQUERY = 1002;

int dp[ MAXQUERY ][ MAXSERVER ];
string server[ MAXSERVER ];
string query[ MAXQUERY ];
int s, q;

void clear( void ) { 
  memset( dp, 1, sizeof( dp ) ); 
  memset( dp[ 0 ], 0, sizeof( dp[ 0 ] ) );
}

void read( void ) {
  static char buff[ 1025 ];

  scanf( "%d%*c", &s );
  for( int i = 0; i < s; ++i ) {
    fgets( buff, sizeof( buff ), stdin );
    server[ i ] = buff;
  }

  scanf( "%d%*c", &q );
  for( int i = 0; i < q; ++i ) {
    fgets( buff, sizeof( buff ), stdin );
    query[ i ] = buff;
  }
}

void solve( void ) {
  for( int i = 1; i <= q; ++i )
    for( int j = 0; j < s; ++j ) {
      if( query[ i - 1 ] == server[ j ] ) continue;
      for( int k = 0; k < s; ++k )
        dp[ i ][ j ] = min( dp[ i-1 ][ k ] + ( j != k ), dp[ i ][ j ] );
    }
  nth_element( dp[q], dp[q], dp[q]+s );
}

int main( void ) {
  double start = clock();
  int numcases;
  scanf( "%d", &numcases );
  for( int Case = 0; Case < numcases; ++Case ) {
    start = clock();

    clear();
    read();
    
    solve();
    printf( "Case #%d: %d\n", Case + 1, dp[q][0] );
    fprintf( stderr, "Case #%d: %d; %.3lfs (%.3lfs)\n", Case + 1, dp[q][0], ( clock() - start ) / CLK_TCK, clock() / (double)CLK_TCK );
  }
  
  return NULA;
}
