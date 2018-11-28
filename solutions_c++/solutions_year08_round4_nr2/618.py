#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    int r, c, A; scanf( "%d%d%d", &r, &c, &A );

    bool kraj = false;
    
    printf( "Case #%d: ", t_case + 1 );
    for( int x1 = 0; !kraj && x1 <= r; ++x1 )
      for( int y1 = 0; !kraj && y1 <= c; ++y1 )
	for( int x2 = x1; !kraj && x2 <= r; ++x2 )
	  for( int y2 = 0; !kraj && y2 <= c; ++y2 ) {
	    if ( x1 == x2 && y1 == y2 ) continue;
	    
	    for( int x3 = x2; x3 <= r; ++x3 ) {
	      int t = A - x1 * x2 + x2 * y1  - x3* y1 + x3 * y2;
	      if ( t == 0 ) {
		printf( "%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, 0 );
		kraj = true;
		break;
	      }

	      if ( x1 != x2 && t % ( x1 - x2  ) == 0 ) {
		int y3 = t / ( x1 - x2 );
		if ( 0 <= y3 && y3 <= c ) {
		  printf( "%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, t / ( x1 - x2 ) );
		  kraj = true;
		  break;
		}
	      }
	    }
	  }
    if ( !kraj )
      puts( "IMPOSSIBLE" );
  }
  return 0;
}
