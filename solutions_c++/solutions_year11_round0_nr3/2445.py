#include <cstdio>
using namespace std;

int main() {
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    int n;
    scanf( "%d", &n );
    int all = 0, mi = (int)1e9, sum = 0;
    for ( int i=0; i<n; i++ ) {
      int x;
      scanf( "%d", &x );
      all ^= x;
      sum += x;
      if ( x < mi ) mi = x;
    }
    printf( "Case #%d: ", q );
    if ( all != 0 ) printf( "NO\n" );
    else printf( "%d\n", sum - mi );
  }
}