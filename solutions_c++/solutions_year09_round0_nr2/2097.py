#include <cstdio>
#include <cstdlib>
#include <cstring>

const int dr[ 4 ][ 2 ] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

int t, h, w, mat[ 105 ][ 105 ];
int slovo[ 105 ][ 105 ], trensl;

int rekurzija( int red, int stup ) {
	int nred = -1, nstup = -1, najn = 100000;
	for( int i = 0; i < 4; ++i ) {
		int tred = red + dr[ i ][ 0 ];
		int tstup = stup + dr[ i ][ 1 ];
		
		if( tred < 0  ||  tred >= h ) continue;
		if( tstup < 0  ||  tstup >= w ) continue;
		
		if( mat[ tred ][ tstup ] < najn ) {
			najn = mat[ tred ][ tstup ];
			nred = tred; nstup = tstup;
		}
	}
	
	if( najn < mat[ red ][ stup ] ) {
		slovo[ red ][ stup ] = rekurzija( nred, nstup );
	} else {
		if( slovo[ red ][ stup ] == -1 ) slovo[ red ][ stup ] = trensl++;
	}
	
	return( slovo[ red ][ stup ] );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d %d", &h, &w );
		for( int j = 0; j < h; ++j )
			for( int k = 0; k < w; ++k )
				scanf( "%d", &mat[ j ][ k ] );
		
		memset( slovo, -1, sizeof( slovo ) ); trensl = 'a';
		printf( "Case #%d:\n", i + 1 );
		
		for( int j = 0; j < h; ++j )
			for( int k = 0; k < w; ++k ) {
				if( slovo[ j ][ k ] == -1 ) rekurzija( j, k );
				printf( "%c%c", slovo[ j ][ k ], k < w-1 ? ' ' : '\n' );
			}
	}
	return( 0 );
}
