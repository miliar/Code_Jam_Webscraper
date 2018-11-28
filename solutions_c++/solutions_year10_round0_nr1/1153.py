#include <cstdio>


int main( void ) {

  int test; scanf( "%d", &test );
  
  for( int cs = 1; cs <= test; ++cs ) {
    int n, k; scanf( "%d%d", &n, &k );
    
    printf( "Case #%d: %s\n", cs, ( k % (1<<n) ) == (1<<n)-1 ? "ON" : "OFF" );
  }

return 0;
}