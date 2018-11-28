#include <cstdio>
#include <cstring>

#include <set>
#include <algorithm>

using namespace std;

#define MAXN 1005

int T, N;
int a[ MAXN ];
int d[ 10005 ];
int cnt[ 10005 ];

multiset< int > lens;
int shift;

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );

    memset( cnt, 0, sizeof cnt );
    memset( d, 0, sizeof d );

    for( int i = 0; i < N; ++i ) {
      scanf( "%d", a+i );
      ++cnt[a[i]];
    }

    for( int i = 0; i < 10005; ++i )
      d[i] = cnt[i+1] - cnt[i];

    int minl = 1000000000;
    lens.clear();
    shift = 0;

    for( int i = 0; i < 10005; ++i ) {
      if( d[i] < 0 ) {
	for( int j = 0; j < -d[i]; ++j ) {
	  minl = min( minl, (*lens.rbegin() )+shift );
	  lens.erase( lens.find( *lens.rbegin() ) );
	}
      }
      if( d[i] > 0 ) {
	for( int j = 0; j < d[i]; ++j ) 
	  lens.insert( -shift );
      }
      ++shift;
    }

    int Sol = ( minl == 1000000000 ) ? 0 : minl;
    printf( "Case #%d: %d\n", tc, Sol );
  }

  return 0;
}
