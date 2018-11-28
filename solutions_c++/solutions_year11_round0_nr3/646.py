#include <cstdio>
#include <cstring>

#include <vector>
#include <algorithm>

using namespace std;

int N, T;
int a[ 1005 ];

int main( void )
{
  scanf( "%d", &T );

  for( int tc = 1; tc <= T; ++tc ) {
    scanf( "%d", &N );
    scanf( "%d", &a[0] ); 
    
    int minv = a[0];
    int sum = a[0];
    int fx = a[0];

    for( int i = 1; i < N; ++i ) {
      scanf( "%d", a+i );
      minv = min( minv, a[i] );
      sum += a[i];
      fx ^= a[i];
    }

    printf( "Case #%d: ", tc );

    if( fx ) printf( "NO\n" );
    else printf( "%d\n", sum-minv );
  }

  return 0;
}
