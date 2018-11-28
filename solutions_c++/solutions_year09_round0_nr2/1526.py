#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
const int MAXN = 100;
const int MAXC = 26;

int grid[MAXN][MAXN];
int sliv[MAXN][MAXN];

int r, c; 

struct coor {
  int x, y;

  bool valid() { return ( x >= 0 && x < r && y >= 0 && y < c ); }
  coor( int nx = 0, int ny = 0 ) { x = nx; y = ny; }
  friend coor operator+( const coor& A, const coor& B ) { return coor( A.x + B.x, A.y + B.y ); }
};

const coor delta[4] = { coor( -1, 0 ), coor( 0, -1 ), coor( 0, 1 ), coor( 1, 0 ) };

vector< coor > V;

bool cmp( const coor& A, const coor& B ) 
{
  if ( grid[A.x][A.y] != grid[B.x][B.y] ) return ( grid[A.x][A.y] < grid[B.x][B.y] );
  if ( A.x != B.x ) return ( A.x < B.x );
  return ( A.y < B.y );
}

int dao[MAXC];

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    scanf( "%d%d", &r, &c );
        
    V.clear();
    for( int i = 0; i < r; ++i ) 
      for( int j = 0; j < c; ++j ) {
	V.push_back( coor( i, j ) );
	scanf( "%d", &grid[i][j] );
      }

    sort( V.begin(), V.end(), cmp );

    memset( sliv, -1, sizeof( sliv ) );
    int sliv_cnt = 0;
    for( int i = 0; i < ( int )V.size(); ++i ) {
      int mn = 1000000;
      for( int p = 0; p < 4; ++p ) {
	coor next = V[i] + delta[p];
	if ( next.valid() ) 
	  mn = min( mn, grid[next.x][next.y] );
      }

      if ( mn >= grid[V[i].x][V[i].y] ) 
	sliv[V[i].x][V[i].y] = sliv_cnt++;
      else 
	for( int p = 0; p < 4; ++p ) {
	  coor next = V[i] + delta[p];
	  if ( !next.valid() ) continue;
	  if ( grid[next.x][next.y] == mn ) {
	    sliv[V[i].x][V[i].y] = sliv[next.x][next.y];
	    break;
	  }
	}
    }
    
    printf( "Case #%d:\n", t_case + 1 );
    memset( dao, -1, sizeof( dao ) );
    int cnt = 0;
    for( int i = 0; i < r; ++i, putchar( '\n' ) )
      for( int j = 0; j < c; ++j ) {
	if ( dao[sliv[i][j]] == -1 ) 
	  dao[sliv[i][j]] = cnt++;
	
	if ( j > 0 ) putchar( ' ' );
	putchar( 'a' + dao[sliv[i][j]] );
      }
  }
  return 0;
}
