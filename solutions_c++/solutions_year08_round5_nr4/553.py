#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN = 100;
const int MOD = 10007;

int r, c;
char rupa[MAXN][MAXN];
int dp[MAXN][MAXN];

int rek( int x, int y )
{
  if ( x >= r || y >= c ) return false;
  if ( rupa[x][y] ) return 0;

  int &ref = dp[x][y];
  if ( ref != -1 ) return ref;
  
  if ( x == r - 1 && y == c - 1 )
    return ( ref = 1 );

  ref = ( rek( x + 1, y + 2 ) + rek( x + 2, y + 1 ) );
  if ( ref >= MOD ) ref -= MOD;
  return ref;
}

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    int q; scanf( "%d%d%d", &r, &c, &q );
    
    memset( rupa, false, sizeof( rupa ) );
    
    for( int i = 0; i < q; ++i ) {
      int x, y; scanf( "%d%d", &x, &y );
      --x; --y;

      rupa[x][y] = true;
    }
    
    memset( dp, -1, sizeof( dp ) );
    printf( "Case #%d: %d\n", t_case + 1, rek( 0, 0 ) );

    
  }
  return 0;
}
