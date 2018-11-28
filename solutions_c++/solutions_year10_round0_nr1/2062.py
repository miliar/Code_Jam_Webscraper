#include <cstdio>

using namespace std;

int main( void ) {
  int t;
  scanf( "%d", &t );
  for( int c = 1; c <= t; ++c ) {
    int n, k;
    scanf( "%d %d", &n, &k );
    k %= (1<<n);

    printf( "Case #%d: ", c );
    if( k == (1<<n)-1 ) puts( "ON" ); else
      puts( "OFF" );
  }
  return 0;
}
