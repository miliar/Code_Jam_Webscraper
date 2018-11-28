#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN = 10000;
const int INF = 10001;

pair< int, int > V[MAXN+1];
int offset;
int L[MAXN+1];
int n;
int dp[MAXN+1][2];

int rek( int sad, int jedan )
{
  int &ref = dp[sad][jedan];
  if ( ref != -1 ) return ref;

  if ( sad > offset )
    return ( ref = ( L[sad] != jedan ) * INF );
  
  ref = INF;
  int and_c = rek( 2 * sad, jedan ) + rek( 2 * sad + 1, jedan );
  int or_c = min( and_c, min( rek( 2 * sad, jedan ) + rek( 2 * sad + 1, !jedan ), rek( 2 * sad, !jedan ) + rek( 2 * sad + 1, jedan ) ) );
  
  if ( V[sad].first == jedan ) {
    ref = min( ref, and_c );
    if ( V[sad].second == 1 )
      ref = min( ref, or_c + 1 );
  }
  else {
    ref = min( ref, or_c );
    if ( V[sad].second == 1 )
      ref = min( ref, and_c + 1 );
  }
  
  return ref;
}

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    int jedan; scanf( "%d%d", &n, &jedan );

    offset = ( n - 1 ) / 2;

    for( int i = 1; i <= offset; ++i )
      scanf( "%d%d", &V[i].first, &V[i].second );

    for( int i = offset + 1; i <= n; ++i )
      scanf( "%d", &L[i] );

    memset( dp, -1, sizeof( dp ) );
    int sol = rek( 1, jedan );
    printf( "Case #%d: ", t_case + 1 );
    if ( sol >= INF )
      puts( "IMPOSSIBLE" );
    else
      printf( "%d\n", sol );
  }
  return 0;
}
