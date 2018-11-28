#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int a[ 20000 ];
int n, t;

void ini( void )
	 {
		  scanf( "%d", &n );
		  int i;
		  for( i=1; i<=n; i++ )
			   scanf( "%d", &a[ i ] );
		  sort( a + 1, a + n + 1 );
			   
		  return;
	 }

int work( void )
	 {
		  int i, j;
		  int ans, sum;
		  ans = sum = 0;
		  for( i=1; i<=n; i++ )
			   {
					ans = ans ^ a[ i ];
					sum = sum + a[ i ];
			   }
		 sum = sum - a[ 1 ];
		 if ( ans == 0 ) return sum;
		 return -1;
	 }

int main( void )
	 {

		  int i, k;
		  freopen( "3.in", "r", stdin );
		  freopen( "3.out", "w", stdout );

		  scanf( "%d", &t );
		  for( i=1; i<=t; i++ )
			   {
					ini(  );
					k = work(  );
					if ( k == -1 )
						 printf( "Case #%d: NO\n", i );
					else
						 printf( "Case #%d: %d\n", i, k );
			   }
		  return 0;
	 }
