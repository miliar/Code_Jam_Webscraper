#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX = 2000100;

int c[MAX];
int w[10];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int cn = 1; cn <= t; ++cn ) {
    memset( c, 0, sizeof(c) );

    int a, b;
    scanf( "%d %d", &a, &b );
    
    int ans = 0;
    for( int i = a; i <= b; ++i ) {
      int n = 0, x = i, d = x;
      while( x ) w[n++] = x%10, x /= 10;
      
      reverse( w, w + n );
      for( int j = 0; j < n; ++j )
        if( w[j] ) {
          int y = 0;
          for( int k = 0; k < n; ++k )
            y = y*10 + w[ (j+k)%n ];
          d = min( d, y );
        }

      ans += c[d]++;
    }
    printf( "Case #%d: %d\n", cn, ans );
  }
  return 0;
}
