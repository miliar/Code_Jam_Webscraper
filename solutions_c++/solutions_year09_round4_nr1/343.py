#include <cstdio>
#include <algorithm>

using namespace std;

const int MaxN = 55;

char s[ MaxN ];
int a[ MaxN ];
int n;

int ok() {
  for( int i = 0; i < n; ++i )
    if( a[i] > i ) return 0;
  return 1;
}

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int d = 1; d <= t; ++d ) {
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i ) {
      scanf( "%s", s );
      a[i] = -1;
      for( int j = 0; j < n; ++j )
	if( s[j] == '1' ) a[i] = j;
    }
    
    int r = 0;
    while( !ok() ) {
      for( int i = 0; i < n; ++i )
	if( a[i] > i ) {
	  int j = i;
	  while( a[j] > i ) j++;
	  for( int k = j; k > i; --k )
	    swap( a[k], a[k-1] ), r++;
	}
    }

    printf( "Case #%d: %d\n", d, r );
  }
  return 0;
}
