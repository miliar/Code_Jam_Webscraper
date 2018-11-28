#include <cstdio>
#include <algorithm>

using namespace std;

const int MaxN = 5004;
const int MaxL = 20;

int a[ MaxL ];
char s[ MaxN ];
char w[ MaxN ][ MaxL ];

int main( void ) {
  int l, d, n;
  scanf( "%d %d %d", &l, &d, &n );
  for( int i = 0; i < d; ++i )
    scanf( "%s", w[i] );
  for( int i = 0; i < n; ++i ) {
    scanf( "%s", s );
    int ptr = 0;
    for( int j = 0; j < l; ++j ) {
      a[j] = 0;
      if( isalpha( s[ptr] ) ) { a[j] |= ( 1 << ( s[ptr++]-'a' ) ); continue; }
      ptr++;
      while( isalpha( s[ptr] ) ) a[j] |= ( 1 << ( s[ptr++]-'a' ) );
      ptr++;
    }

    int r = 0;
    for( int j = 0; j < d; ++j ) {
      int ok = 1;
      for( int k = 0; k < l; ++k )
	if( !( ( a[k]>>( w[j][k]-'a' ) )&1 ) ) { ok = 0; break; }
      r += ok;
    }
    printf( "Case #%d: %d\n", i+1, r );
  }
  return 0;
}
