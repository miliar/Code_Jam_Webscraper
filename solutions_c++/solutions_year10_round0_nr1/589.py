#include <cstdio>

inline bool check( int n, int k ) {
  int mask = ( 1 << n ) - 1;
  return ( k & mask ) == mask;
}

int main( void ) {
  int n, k, t;
  scanf( "%d", &t );

  for( int i = 0; i < t; ++i ) {
    scanf( "%d %d", &n, &k );
    printf( "Case #%d: %s\n", i+1, check( n, k ) ? "ON" : "OFF" );
  }
  return 0;
}

