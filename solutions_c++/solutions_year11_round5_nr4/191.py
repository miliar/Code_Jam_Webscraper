#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long llint;

const int MAXN = 130;

char s[MAXN];
int a[MAXN];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    scanf( "%s", s );
    
    llint ss = 0;
    int n = 0, l = strlen( s );
    for( int i = 0; i < l; ++i )
      if( s[i] == '1' ) ss += (1LL<<(l-i-1)); else
	if( s[i] == '?' ) a[n++] = l-i-1;
    
    for( int i = 0; i < (1<<n); ++i ) {
      llint x = ss;
      for( int j = 0; j < n; ++j )
	if( i&(1<<j) ) x += (1LL<<a[j]);
      
      llint v = sqrt( x + 0.5 );
      if( v*v == x ) {
	for( int j = 0; j < n; ++j )
	  s[ l-a[j]-1 ] = '0' + ((i>>j)&1);
	break;
      }
    }

    printf( "Case #%d: %s\n", c, s );
  }
  return 0;
}
