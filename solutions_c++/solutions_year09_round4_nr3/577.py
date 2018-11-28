#include <cstdio>
#include <algorithm>
using namespace std;
const int MAXN = 16;
const int MAXK = 25;

int P[MAXN][MAXK];
char ok[MAXN][MAXN];
char valid[1<<MAXN];
int dp[1<<MAXN];
int n, k;

int rek( int state )
{
  int &ref = dp[state];
  if ( ref != -1 ) return ref;

  if ( state == ( 1 << n ) - 1 ) return ( ref = 0 );

  ref = n;
  for( int p = 0; p < ( 1 << n ); p = ( p + state + 1 ) & ~state )
    if ( p != 0 && valid[p] )
      ref = min( ref, rek( state | p ) + 1 );
  return ref;
}

bool moze( int A, int B )
{
  for( int i = 0; i < k; ++i )
    if ( P[A][i] == P[B][i] ) return false;

  for( int i = 1; i < k; ++i )
    if ( ( P[A][0] < P[B][0] ) != ( P[A][i] < P[B][i] ) ) return false;
  return true;
}

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%d%d", &n, &k );
    
    memset( ok, false, sizeof( ok ) );
    for( int i = 0; i < n; ++i ) {
      for( int j = 0; j < k; ++j )
	scanf( "%d", &P[i][j] );
      
      for( int j = 0; j < i; ++j )
	ok[i][j] = ok[j][i] = moze( i, j );
    }
    
    for( int state = 0; state < ( 1 << n ); ++state ) {
      valid[state] = true;
      for( int i = 0; valid[state] && i < n; ++i )
	if ( ( state >> i ) & 1 )
	  for( int j = i + 1; j < n; ++j )
	    if ( ( state >> j ) & 1 )
	      if ( !ok[i][j] ) {
		valid[state] = false;
		break;
	      }
    }
    
    memset( dp, -1, sizeof( dp ) );
    printf( "Case #%d: %d\n", t_case + 1, rek( 0 ) );
  }
  return 0;
}
