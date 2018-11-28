#include <cstdio>
#include <algorithm>
using namespace std;
const int MAXN = 100;
const int MAXL = 10000;

int A[MAXN+2];
int dp[MAXN+2][MAXN+2];

int rasjeci( int a, int b )
{
  if ( A[a] >= A[b] || a + 1 == b ) return 0;
  int &ref = dp[a][b];

  if ( ref != -1 ) return ref;
  
  ref = MAXN * MAXL;
  for( int i = a + 1; i < b; ++i )
    ref = min( ref, rasjeci( a, i ) + rasjeci( i, b ) + A[b] - A[a] - 2 );

  return ref;
}

int main()
{
  int t, l, n; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%d%d", &l, &n );

    for( int i = 0; i < n; ++i )
      scanf( "%d", &A[i] );
    
    memset( dp, -1, sizeof( dp ) );
    A[n] = 0; A[n+1] = l + 1;
    sort( A, A + n + 2 );
    printf( "Case #%d: %d\n", t_case + 1, rasjeci( 0, n + 1 ) );
  }
  return 0;
}
