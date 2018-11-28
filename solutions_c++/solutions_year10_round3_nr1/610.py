#include <cstdio>

int main( void ) {


  int test; scanf( "%d", &test );
  
  
  for( int cs = 1; cs <= test; ++cs ) {
    int n; scanf( "%d", &n );
    int a[1010], b[1010];
    
    int sol = 0;
    for( int i = 0; i < n; ++i ) {
      scanf( "%d%d", a+i, b+i );
      for( int j = i-1; j >= 0; --j ) {
        if( a[j] < a[i] && b[j] > b[i] ) ++sol;
        if( a[j] > a[i] && b[j] < b[i] ) ++sol;
      }
    }
    
    printf( "Case #%d: %d\n", cs, sol );
  }

return 0;
}