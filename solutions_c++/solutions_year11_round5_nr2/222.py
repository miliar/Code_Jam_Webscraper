#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1005;

int a[MAXN];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n;
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i )
      scanf( "%d", a+i );
    sort( a, a + n );

    int ans = 0;
    do {
      int c = 1000, x = 0;
      while( x < n ) {
	int y = x+1;
	while( y < n && a[y] == a[y-1]+1 ) y++;
	c = min( c, y-x );
	x = y;
      }
      ans = max( ans, c );
    } while( next_permutation( a, a + n ) );
   
    if( n == 0 ) ans = 0;
    printf( "Case #%d: %d\n", c, ans );
  }
  return 0;
}
