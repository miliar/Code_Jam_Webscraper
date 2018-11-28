#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
short dp[ 11 ][ 1005 ][ 1005 ];

short solve( int L, int P, int C ) {
	if( C * L >= P ) return( 0 );
	if( dp[ C ][ L ][ P ] != -1 )
		return( dp[ C ][ L ][ P ] );
	
	short rez = 10000;
	for( int i = L+1; i < P; ++i )
		rez = min( rez, max( solve( L, i, C ), solve( i, P, C ) ) );
	
	return( dp[ C ][ L ][ P ] = rez + 1 );
}

int main( void ) {
	memset( dp, -1, sizeof( dp ) );
	for( int C = 2; C <= 10; ++C )
		for( int L = 1; L <= 1000; ++L )
			for( int P = L + 1; P <= 1000; ++P )
				solve( L, P, C );
	
	int t, L, P, C;
	scanf( "%d", &t );
	
	for( int i = 0; i < t; ++i ) {
		scanf( "%d %d %d", &L, &P, &C );
		printf( "Case #%d: %d\n", i+1, solve( L, P, C ) );
	}
	
	return( 0 );
}
