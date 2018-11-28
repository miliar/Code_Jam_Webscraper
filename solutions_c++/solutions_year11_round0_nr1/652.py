#include <cstdio>
#include <cstring>

#include <queue>
#include <algorithm>

using namespace std;

#define MAX 105
#define MAXN 105

int T, N;
int p[ MAXN ];
char w[ MAXN ];

int d[ MAXN ][ MAX ][ MAX ];
int bio[ MAXN ][ MAX ][ MAX ];
int cookie;

struct state {
  int pos, a, b;
  state() { pos = a = b = 0; }
  state( int P, int A, int B ) { pos = P; a = A; b = B; }
};

inline int dist( state s ) {
  return d[s.pos][s.a][s.b];
}

queue< state > q;

inline void relax( state a, state b ) {
  if( bio[b.pos][b.a][b.b] != cookie ) {
    bio[b.pos][b.a][b.b] = cookie;
    d[b.pos][b.a][b.b] = dist( a )+1;
    q.push( b );
  }
}

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );

    for( int i = 0; i < N; ++i ) {
      scanf( " %c %d", w+i, p+i );
      --p[i];
    }

    while( !q.empty() ) q.pop();

    ++cookie;
    d[0][0][0] = 0;
    q.push( state( 0, 0, 0 ) );

    while( !q.empty() ) {
      state c = q.front(); q.pop();

      //printf( "%d %d %d\n", c.pos, c.a, c.b );

      if( c.pos == N ) {
	printf( "Case #%d: %d\n", tc, dist( c ) );
	break;
      }

      if( c.a > 0 ) {
	relax( c, state( c.pos, c.a-1, c.b ) );
	if( c.b > 0 ) relax( c, state( c.pos, c.a-1, c.b-1 ) );
	if( c.b < 99 ) relax( c, state( c.pos, c.a-1, c.b+1 ) );
      }
      if( c.a < 99 ) {
	relax( c, state( c.pos, c.a+1, c.b ) );
	if( c.b > 0 ) relax( c, state( c.pos, c.a+1, c.b-1 ) );
	if( c.b < 99 ) relax( c, state( c.pos, c.a+1, c.b+1 ) );
      }
      
      if( c.b > 0 ) {
	relax( c, state( c.pos, c.a, c.b-1 ) );
	if( c.a > 0 ) relax( c, state( c.pos, c.a-1, c.b-1 ) );
	if( c.a < 99 ) relax( c, state( c.pos, c.a+1, c.b-1 ) );
      }
      if( c.b < 99 ) {
	relax( c, state( c.pos, c.a, c.b+1 ) );
	if( c.a > 0 ) relax( c, state( c.pos, c.a-1, c.b+1 ) );
	if( c.a < 99 ) relax( c, state( c.pos, c.a+1, c.b+1 ) );
      }
      

      if( w[c.pos] == 'O' && p[c.pos] == c.a ) {
	relax( c, state( c.pos+1, c.a, c.b ) );
	if( c.b > 0 ) relax( c, state( c.pos+1, c.a, c.b-1 ) );
	if( c.b < 99 ) relax( c, state( c.pos+1, c.a, c.b+1 ) );
      }
      if( w[c.pos] == 'B' && p[c.pos] == c.b ) {
	relax( c, state( c.pos+1, c.a, c.b ) );
	if( c.a > 0 ) relax( c, state( c.pos+1, c.a-1, c.b ) );
	if( c.a < 99 ) relax( c, state( c.pos+1, c.a+1, c.b ) );
      }
    }
  }

  return 0;
}
