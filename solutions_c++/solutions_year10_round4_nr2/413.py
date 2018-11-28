#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int inf = 1000000000;

int P;
int tree[1<<11];
int dp[1<<11][12];

int solve( int x, int miss ) {
  if( x >= (1<<P) ) {
    if( miss > tree[x] ) return inf;
    return 0;
  }

  int &ret = dp[x][miss];
  if( ret != -1 ) return ret;

  ret = inf;
  ret = min( ret, solve( 2*x, miss+1 ) + solve( 2*x+1, miss+1 ) );
  ret = min( ret, solve( 2*x, miss ) + solve( 2*x+1, miss ) + tree[x] );

  return ret;
}

int main( void ) {
  int tc; scanf( "%d", &tc );
  for( int t = 1; t <= tc; ++t ) {
    scanf( "%d", &P );
    for( int i = P; i >= 0; --i )
      for( int j = 0; j < (1<<i); ++j )
        scanf( "%d", &tree[(1<<i)+j] );

    memset( dp, -1, sizeof dp );
    printf( "Case #%d: %d\n", t, solve( 1, 0 ) );
  }
  return 0;
}

