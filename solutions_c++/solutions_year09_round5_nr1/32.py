#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef pair< int, int > par;
#define x first
#define y second

const int INF = 1000000000;

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

int bio[6];

struct state {
  vector< par > v;
  int con;
  void dfs( int x ) {
    if( bio[x] ) return;
    bio[x] = 1;
    for( int i = 0; i < 4; ++i ) {
      int X = v[x].x+dx[i], Y = v[x].y+dy[i];
      for( int j = 0; j < v.size(); ++j )
	if( !bio[j] && v[j].x == X && v[j].y == Y ) dfs( j );
    }
  }

  void f5() {
    sort( v.begin(), v.end() );
    memset( bio, 0, sizeof( bio ) );
    dfs( 0 );
    con = 1;
    for( int i = 0; i < v.size(); ++i )
      con &= bio[i];
  }
  state() {};
  friend bool operator < ( const state &a, const state &b ) {
    for( int i = 0; i < a.v.size(); ++i )
      if( a.v[i] != b.v[i] ) return a.v[i] < b.v[i];
    return 0;
  }
};


state st[1000000];
int dp[1000000];
char a[13][13];
int cnt, n, m, w;

struct cmp {
  bool operator() ( const int &a, const int &b ) {
    if( dp[a] != dp[b] ) return dp[a] < dp[b];
    return a < b;
  }
};

set< int, cmp > S;
map< state, int > M;

int valid( int x, int y, state &s ) {
  if( x < 0 || y < 0 || x >= n || y >= m || a[x][y] == '#' ) return 0;
  for( int i = 0; i < cnt; ++i )
    if( s.v[i].x == x && s.v[i].y == y ) return 0;
  return 1;
}

void ins( state &s ) { if( !M.count( s ) ) st[w] = s, M[s] = w++; }

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    cnt = 0;
    vector< par > x, c;

    scanf( "%d %d", &n, &m );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", a[i] );
      for( int j = 0; j < m; ++j ) {
	if( a[i][j] == 'o' || a[i][j] == 'w' ) {
	  x.push_back( par( i, j ) );
	  cnt++;
	}
	if( a[i][j] == 'x' || a[i][j] == 'w' ) c.push_back( par( i, j ) );
      }
    }

    memset( dp, 63, sizeof( dp ) );
    S.clear(); M.clear(); w = 0;
    
    state P; P.v = x;
    state K; K.v = c;

    P.f5(); K.f5();
    ins( P ); ins( K );

    dp[M[P]] = 0;
    S.insert( M[P] );
    while( S.size() ) {
      int ind = *S.begin();
      S.erase( S.begin() );
      
      state s = st[ind];
      for( int i = 0; i < s.v.size(); ++i )
	for( int j = 0; j < 4; ++j )
	  if( valid( s.v[i].x+dx[j], s.v[i].y+dy[j], s ) && valid( s.v[i].x-dx[j], s.v[i].y-dy[j], s ) ) {
	    state t = s;
	    t.v[i].x += dx[j], t.v[i].y += dy[j];
	    t.f5(); ins( t );
	    if( !s.con && !t.con ) continue;
	    
	    int k = M[t];
	    if( dp[ind]+1 < dp[k] ) {
	      S.erase( k );
	      dp[k] = dp[ind]+1;
	      S.insert( k );
	    }
	  }
    }

    int r = dp[M[K]];
    if( r >= INF ) r = -1;
    printf( "Case #%d: %d\n", d, r );
  }
  return 0;
}
    
