#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
const int MAXN = 1000;
char buff[MAXN+1];

int n, m;
int B[MAXN];

int dp[MAXN][MAXN];

int rek( int sad, int work )
{
  if ( work == m ) return 0;

  int &ref = dp[sad][work];
  if ( ref != -1 ) return ref;

  if ( sad != B[work] )
    return ( ref = rek( sad, work + 1 ) );
  
  ref = MAXN;
  for( int i = 0; i < n; ++i )
    if ( i != B[work] )
      ref = min( ref, rek( i, work + 1 ) + 1 );
  return ref;
}
 
int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    vector< string > A, V;
    scanf( " %d ", &n );
    for( int i = 0; i < n; ++i ) {
      gets( buff );
      A.push_back( buff );
      V.push_back( buff );
    }
    
    vector< string > B;
    scanf( " %d ", &m );
    for( int i = 0; i < m; ++i ) {
      gets( buff );
      B.push_back( buff );
      V.push_back( buff );
    }

    sort( V.begin(), V.end() );
    V.erase( unique( V.begin(), V.end() ), V.end() );

    for( int i = 0; i < m; ++i )
      ::B[i] = lower_bound( V.begin(), V.end(), B[i] ) - V.begin();

    memset( dp, -1, sizeof( dp ) );
    int sol = MAXN;
    for( int i = 0; i < n; ++i )
      sol = min( sol, rek( i, 0 ) );
    printf( "Case #%d: %d\n", t_case + 1, sol );
  }
  return 0;
}
