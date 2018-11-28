#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
const int MAXN = 40;
const int MOD = 1999997;
const int M = 997;

char grid[MAXN][MAXN+1];

char dist[MOD];

int hash( vector< int >& V )
{
  int H = 0;
  for( int i = 0; i < ( int )V.size(); ++i )
    H = ( H * M + V[i] ) % MOD;
  return H;
}

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    int n; scanf( "%d", &n );
    vector< int > S( n, 0 );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", grid[i] );
      for( int j = 0; j < n; ++j )
	S[i] = S[i] * 2 + ( grid[i][j] - '0' );
    }
    
    memset( dist, -1, sizeof( dist ) );

    dist[hash( S )] = 0;
    queue< vector< int > > Q;
    int sol = -1;
    for( Q.push( S ); !Q.empty(); ) {
      vector< int > sad = Q.front(); Q.pop();
      
      bool ok = true;
      for( int i = 0; i < n && ok; ++i )
	for( int j = 0; j < n; ++j )
	  if ( j > i && ( sad[i] >> ( n - j - 1 ) ) & 1 ) { ok = false; break; }

      int dsad = hash( sad );
      if ( ok ) { sol = dist[dsad]; break; }

      for( int i = 0; i + 1 < n; ++i ) {
	swap( sad[i], sad[i+1] );
	int tmp = hash( sad );
	if ( dist[tmp] == -1 ) {
	  dist[tmp] = dist[dsad] + 1;
	  Q.push( sad );
	}
	swap( sad[i], sad[i+1] );
      }
    }
    printf( "Case #%d: %d\n", t_case + 1, sol );
  }
  return 0;
}
