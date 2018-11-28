#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
int t, m, n, vr[ 513 ][ 513 ], best[ 513 ][ 513 ], rez[ 513 ];
char buff[ 1024 ];

int getvr( char ch ) {
	if( ch <= '9' ) return( ch - '0' );
	return( ch - 'A' + 10 );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		memset( vr, 0, sizeof( vr ) );
		memset( best, 0, sizeof( best ) );
		
		scanf( "%d %d", &m, &n );
		for( int j = 0; j < m; ++j ) {
			scanf( "%s", buff );
			for( int k = 0; k < n/4; ++k )
				for( int l = 0; l < 4; ++l )
					vr[ j ][ 4 * k + l ] = ( getvr( buff[ k ] ) >> ( 3-l ) ) & 1;
		}
		
		for( int j = m-1; j >= 0; --j )
			for( int k = n-1; k >= 0; --k )
				best[ j ][ k ] = 1;
		
		for( int a = m-1; a >= 0; --a )
			for( int b = n-1; b >= 0; --b ) {
				if( best[ a ][ b ] == 0 ) continue;
				
				best[ a ][ b ] = 1;
				
				if( vr[ a ][ b ] != vr[ a+1 ][ b+1 ] ) continue;
				if( vr[ a ][ b ] == vr[ a+1 ][ b ] ) continue;
				if( vr[ a ][ b ] == vr[ a ][ b+1 ] ) continue;
				
				int A = best[ a+1 ][ b+1 ];
				int B = best[ a ][ b+1 ];
				int C = best[ a+1 ][ b ];
				
				best[ a ][ b ] = min( A, min( B, C ) ) + 1;
			}
							
		/*for( int j = m-1; j >= 0; --j )
			for( int k = n-1; k >= 0; --k ) {
				best[ j ][ k ] = 1;
				
				if( vr[ j ][ k ] != vr[ j+1 ][ k+1 ] ) continue;
				if( vr[ j ][ k ] == vr[ j+1 ][ k ] ) continue;
				if( vr[ j ][ k ] == vr[ j ][ k+1 ] ) continue;
				
				int A = best[ j+1 ][ k+1 ];
				int B = best[ j ][ k+1 ];
				int C = best[ j+1 ][ k ];
				
				best[ j ][ k ] = min( A, min( B, C ) ) + 1;
			}*/
		
		/*for( int j = 0; j < m; ++j ) {
			for( int k = 0; k < n; ++k )
				printf( "%d", best[ j ][ k ] );
				//printf( "%c", vr[ j ][ k ] ? '#' : ' ' );
			printf( "\n" );
		}
		printf( "\n" );	*/	
		
		memset( rez, 0, sizeof( rez ) );
		int cnt = 0;
		
		for( int j = min( m, n ); j > 0; --j ) {
			for( int k = 0; k < m; ++k )
				for( int l = 0; l < n; ++l )
					if( best[ k ][ l ] == j ) {
						if( rez[ j ]++ == 0 ) ++cnt;
						
						for( int a = k; a < k + j; ++a )
							for( int b = l; b < l + j; ++b )
								best[ a ][ b ] = 0;
								
						for( int a = m-1; a >= 0; --a )
							for( int b = n-1; b >= 0; --b ) {
								if( best[ a ][ b ] == 0 ) continue;
								
								best[ a ][ b ] = 1;
								
								if( vr[ a ][ b ] != vr[ a+1 ][ b+1 ] ) continue;
								if( vr[ a ][ b ] == vr[ a+1 ][ b ] ) continue;
								if( vr[ a ][ b ] == vr[ a ][ b+1 ] ) continue;
								
								int A = best[ a+1 ][ b+1 ];
								int B = best[ a ][ b+1 ];
								int C = best[ a+1 ][ b ];
								
								best[ a ][ b ] = min( A, min( B, C ) ) + 1;
							}
					}
			
			/*for( int j = 0; j < m; ++j ) {
				for( int k = 0; k < n; ++k )
					printf( "%d", best[ j ][ k ] );
					//printf( "%c", vr[ j ][ k ] ? '#' : ' ' );
				printf( "\n" );
			}
			printf( "\n" );*/
		}
		
		printf( "Case #%d: %d\n", i+1, cnt );
		for( int j = min( m, n ); j > 0; --j )
			if( rez[ j ] > 0 )
				printf( "%d %d\n", j, rez[ j ] );
	}
	
	return( 0 );
}
