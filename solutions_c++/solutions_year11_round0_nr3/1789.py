#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;
int n, t, c[ 1005 ];

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d", &n );
		
		int svi = 0, suma = 0;
		for( int j = 0; j < n; ++j ) {
			scanf( "%d", &c[ j ] );
			svi ^= c[ j ]; suma += c[ j ];
		}
		
		sort( c, c + n );
		if( svi == 0 ) printf( "Case #%d: %d\n", i+1, suma - c[ 0 ] );
		else printf( "Case #%d: NO\n", i+1 );
	}
	return( 0 );
}
