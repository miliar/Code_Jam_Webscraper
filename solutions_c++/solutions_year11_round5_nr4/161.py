#include <cmath>
#include <cstdio>
#include <cstring>

typedef unsigned long long llint;

int T;
int m[ 200 ];
char buff[ 200 ];

inline llint root( llint x ) {
  llint lo = 0, hi = 1LL << 31, mid;

  while( lo < hi ) {
    mid = ( lo + hi ) >> 1;
    if( mid*mid < x ) lo = mid+1;
    else hi = mid;
  }

  return lo;
}

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%s", buff );
    int n = strlen( buff );

    for( int i = 0; i < n; ++i )
      m[i] = ( buff[i] == '?' );

    int tot = 0;
    for( int i = 0; i < n; ++i )
      tot += m[i];

    bool done = 0;
    int cnt = 0;

    for( int i = 0; i < ( 1 << tot ); ++i ) {
      int now = 0;
      for( int j = 0; j < n; ++j ) {
	if( m[j] ) buff[j] = (( i >> (now++) )&1)+'0';
      }
    
      llint x = 0;

      for( int j = 0; j < n; ++j )
	x = x*2LL+llint(buff[j]-'0');

      llint y = llint( sqrt( x ) + 1e-9 );
      if( y*y == x ) { done = 1; break; }
    }

    printf( "Case #%d: %s\n", tc, buff );
  }

  return 0;
}
