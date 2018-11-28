#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long llint;
typedef long double ldouble;

int T;
int N; llint L, H;
llint a[ 10005 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d%lld%lld", &N, &L, &H );

    for( int i = 0; i < N; ++i )
      scanf( "%lld", a+i );

    printf( "Case #%d: ", tc );

    bool done = 0;
    llint Sol;

    for( llint i = L; i <= H && !done; ++i ) {
      bool ok = 1;
      for( int j = 0; j < N; ++j )
	if( !( a[j] % i == 0 || i % a[j] == 0 ) ) ok = 0;

      if( ok ) { done = 1; Sol = i; break; }
    }

    if( !done ) printf( "NO\n" );
    else printf( "%lld\n", Sol );

  }

  return 0;
}
