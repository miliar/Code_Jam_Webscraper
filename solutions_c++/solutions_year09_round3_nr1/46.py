#include <cstdio>
#include <cstring>

using namespace std;

typedef long long llint;

const int MaxL = 65;

char s[ MaxL ];
int e[ 255 ];
int d[ 255 ];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int w = 1; w <= t; ++w ) {
    memset( e, 0, sizeof( e ) );

    scanf( "%s", s );
    int n = strlen( s ), b = 0;
    for( int i = 0; i < n; ++i )
      if( !e[ s[i] ] ) e[ s[i] ] = 1, b++;
    if( b == 1 ) b++;

    memset( e, 0, sizeof( e ) );
    d[0] = 1;
    for( int i = 0; i < n; ++i )
      if( s[i] == s[0] ) d[i] = 1, e[i] = 1;
    
    int c = 0;
    for( int i = 1; i < n; ++i )
      if( !e[i] ) {
	d[i] = c;
	for( int j = 0; j < n; ++j )
	  if( s[j] == s[i] ) d[j] = c, e[j] = 1;
	c++;
	if( c == 1 ) c++;
      }

    llint r = 0, p = 1;
    for( int i = n-1; i >= 0; --i )
      r += p*d[i], p *= b;
    
    printf( "Case #%d: %lld\n", w, r );
  }
  return 0;
}
