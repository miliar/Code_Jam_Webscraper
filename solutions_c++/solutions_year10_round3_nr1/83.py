#include <cstdio>
#include <algorithm>

using namespace std;

int a[1005], b[1005];

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n;
    scanf( "%d", &n );
    for( int i = 0; i < n; ++i )
      scanf( "%d %d", a+i, b+i );

    int ans = 0;
    for( int i = 0; i < n; ++i )
      for( int j = i+1; j < n; ++j )
	if( ( a[i] < a[j] ) != ( b[i] < b[j] ) ) ans++;

    printf( "Case #%d: %d\n", c, ans );
  }
  return 0;
}
