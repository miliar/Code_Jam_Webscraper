#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int veci[101][101];
int a[101][101], p[101];
int dp[101], last[101];
int n, k;

vector< int > E[ 101 ];
int dad[101];
int bio[101];
int cookie;

struct cmpf {
  bool operator() ( const int &x, const int &y ) {
    for( int i = 0; i < k; ++i )
      if( a[x][i] != a[y][i] ) return a[x][i] < a[y][i];
    return 0;
  }
};

int cmp( const int &x, const int &y ) {
  for( int i = 0; i < k; ++i )
    if( a[x][i] != a[y][i] ) return a[x][i] < a[y][i];
  return 0;
}

int match( int x ) {
  if( x == -1 ) return 1;
  if( bio[x] == cookie ) return 0;

  bio[x] = cookie;
  for( int i = 0; i < E[x].size(); ++i )
    if( match( dad[ E[x][i] ] ) ) {
      dad[ E[x][i] ] = x;
      return 1;
    }
  return 0;
}

int main( void ) {
  cookie = 1;

  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    vector< int > v;
    scanf( "%d %d", &n, &k );
    for( int i = 0; i < n; ++i ) {
      E[i].clear();
      for( int j = 0; j < k; ++j )
	scanf( "%d", a[i]+j );
      v.push_back( i );
    }
    
    for( int i = 0; i < n; ++i )
      for( int j = 0; j < n; ++j ) {
	int ok = 1;
	for( int l = 0; l < k; ++l )
	  if( a[i][l] <= a[j][l] ) { ok = 0; break; }
	veci[i][j] = ok;
      }

    sort( v.begin(), v.end(), cmp );
    multiset< int, cmpf > S;
    for( int i = 0; i < v.size(); ++i ) {
      multiset< int, cmpf > :: iterator it = S.insert( v[i] );
      while( it != S.begin() ) {
	it--;
	if( veci[v[i]][*it] ) E[v[i]].push_back( *it );
      }
    }

    memset( dad, -1, sizeof( dad ) );
    int r = n;
    for( int i = 0; i < n; ++i, ++cookie )
      r -= match( i );

    printf( "Case #%d: %d\n", d, r );
  }
  return 0;
}
