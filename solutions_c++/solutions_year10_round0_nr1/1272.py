#include <cstdio>
#include <algorithm>

using namespace std;

int main( void ) {
  int tc; scanf( "%d", &tc );
  for( int t = 0; t < tc; ++t ) {
    int n, k; scanf( "%d %d", &n, &k );
    printf( "Case #%d: %s\n", t+1, (k+1)%(1<<n) ? "OFF" : "ON" );
  }
  return 0;
}

