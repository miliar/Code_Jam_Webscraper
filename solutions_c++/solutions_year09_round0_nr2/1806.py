#include <cstdio>
#include <cstring>
using namespace std;
const int NULA = 0;
const int MAXH = 110;
const int MAXW = 110;

const int dx[] = { -1, 0, 0, 1 };
const int dy[] = { 0, -1, 1, 0 };

int t, h, w;
int ploca[ MAXH ][ MAXW ];
char basins[ MAXH ][ MAXW ];
char letter;

bool valid( int x, int y ) { return x >= 0 && x < h && y >= 0 && y < w; }

struct stanje {
  int x, y;

  stanje( void )            : x( -1 ), y( -1 ) {}
  stanje( int _x, int _y )  : x( _x ), y( _y ) {}

  int next( void ) {
    int minh = ploca[x][y];
    int ret = -1;

    for( int i = 0; i < 4; ++i )
      if( valid( x+dx[i], y+dy[i] ) && ploca[ x+dx[i] ][ y+dy[i] ] < minh ) {
        minh = ploca[ x+dx[i] ][ y+dy[i] ];
        ret = i;
      }

    return ret;
  }
  
  stanje add( int i ) { return stanje( x+dx[i], y+dy[i] ); }

  char& basin( void ) { return basins[x][y]; }
};

inline void clear( void ) {
  memset( ploca, 0, sizeof( ploca ) );
  memset( basins, 0, sizeof( basins ) );
  letter = 'a';
}

inline void input( void ) {
  scanf( "%d%d", &h, &w );
  for( int i = 0; i < h; ++i )
    for( int j = 0; j < w; ++j )
      scanf( "%d", ploca[i]+j );
}

inline void print( int Case ) {
  printf( "Case #%d:\n", Case );
  for( int i = 0; i < h; ++i )
    for( int j = 0; j < w; ++j )
      printf( "%c%c", basins[i][j], j+1<w ? ' ' : '\n' );
}

inline char dfs( stanje x ) {
  if( x.basin() ) return x.basin();
  int next = x.next();
  if( next == -1 ) return x.basin() = letter++;
  return x.basin() = dfs( x.add( next ) );
}

inline void solve( void ) {
  for( int i = 0; i < h; ++i )
    for( int j = 0; j < w; ++j )
      if( basins[i][j] == 0 )
        dfs( stanje( i, j ) );
}

int main( void ) {
  scanf( "%d", &t );
  for( int i = 0; i < t; ++i ) {
    clear();
    input();
    solve();
    print( i+1 );
  }

  return NULA;
}


