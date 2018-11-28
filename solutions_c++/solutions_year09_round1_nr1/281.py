#include <cstdio>
#include <sstream>
#include <cstring>
#include <ctime>
using namespace std;
const int NULA = 0;
const int MAXN = 30000200;
const int MAXB = 11;

int dp[ MAXN ][ MAXB ];
bool bio[ MAXN ][ MAXB ];
int base, n;
char buff[ 100 ];
int A[ MAXB ];

inline int convert( int x ) {
  register int ret = 0;
  while( x ) {
    ret += ( x%base ) * ( x%base );
    x /= base;
  }
  return ret;
}

int solve( int x ) {
  if( x == 1 ) return 1;
  if( dp[x][base] != -1 ) return dp[x][base];
  if( bio[x][base] ) return 0;
  bio[x][base] = 1;
  return dp[x][base] = solve( convert( x ) );
}

int main( void ) {
  int t;
  scanf( "%d ", &t );
  memset( dp, -1, sizeof( dp ) ); 
  memset( bio, 0, sizeof( bio ) ); 
  
  for( int i = 0; i < t; ++i ) {
    fgets( buff, sizeof( buff ), stdin );
    istringstream is( buff );

    n = 0;
    while( is >> A[n++] );
    --n;
    
    for( int j = 2; j < MAXN; ++j ) {
      bool ok = 1;
      for( int k = 0; ok && k < n; ++k ) {
        base = A[k];
        ok &= solve( j );
      }
      if( ok ) { 
        printf( "Case #%d: %d\n", i+1, j ); 
        fprintf( stderr, "Case #%d: %d\n", i+1, j ); 
        break; 
      }
    }

    //    printf( "BIO\n" ); 
  }

  fprintf( stderr, "TIME:: %.2lfs\n", 1.*clock() / CLOCKS_PER_SEC );
  return NULA;
}

