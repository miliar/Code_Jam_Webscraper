#include <cstdio>
#include <cstring>

#include <set>
#include <map>
#include <algorithm>

using namespace std;
typedef long long llint;

int T; llint t;
int N, C, L;

llint a[ 1000005 ];

struct state {
  int pos, l;
  state() { pos = l = 0; }
  state( int P, int L ) { pos = P; l = L; }
};

inline bool operator<( state a, state b ) {
  if( a.pos != b.pos ) return ( a.pos < b.pos );
  return ( a.l < b.l );
}

map< state, llint > d;

struct cmp {
  bool operator()( state a, state b ) {
    if( d[a] != d[b] ) return ( d[a] < d[b] );
    return ( a < b );
  }
};

set< state, cmp > pq;

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%lld%d%d", &L, &t, &N, &C );

    for( int i = 1; i <= C; ++i ) {
      scanf( "%lld", a+i );
    }

    printf( "Case #%d: ", tc );

    for( int i = C+1; i <= N; ++i )
      a[i] = a[i-C];

    for( int i = 1; i <= N; ++i )
      a[i] += a[i-1];

    pq.clear();
    d.clear();

    state s( 0, L );
    d[s] = 0;

    pq.insert( s );

    while( !pq.empty() ) {
      state c = *pq.begin();
      pq.erase( pq.begin() );

      if( c.pos == N ) { printf( "%lld\n", d[c] ); break; }

      if( d[c] >= t && c.l > 0 ) {
	state nc( c.pos+1, c.l-1 );
	if( !d.count( nc ) || d[nc] > d[c] + a[c.pos+1]-a[c.pos] ) {
	  pq.erase( nc );
	  d[nc] = d[c] + a[c.pos+1] - a[c.pos];
	  pq.insert( nc );
	}
      }

      if( d[c] < t && d[c] + 2*( a[c.pos+1]-a[c.pos] ) >= t && c.l > 0 ) {
	llint dd = t - d[c];
	llint path = ( dd + 1 ) / 2;
	llint len = a[c.pos+1] - a[c.pos] + path;

	state nc( c.pos+1, c.l-1 );
	if( !d.count( nc ) || d[nc] > d[c] + len ) {
	  pq.erase( nc );
	  d[nc] = d[c] + len;
	  pq.insert( nc );
	}
      }

      llint nlen = 2*( a[c.pos+1] - a[c.pos] );
      
      state nc( c.pos+1, c.l );
      if( !d.count( nc ) || d[nc] > d[c] + nlen ) {
	pq.erase( nc );
	d[nc] = d[c] + nlen;
	pq.insert( nc );
      }
    }
  }

  return 0;
}
