#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

int t, c, d, n, oppose[ 256 ][ 256 ];
char combine[ 256 ][ 256 ], b[ 105 ];

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		memset( oppose, 0, sizeof( oppose ) );
		memset( combine, 0, sizeof( combine ) );
		
		scanf( "%d", &c );
		for( int j = 0; j < c; ++j ) {
			scanf( "%s", b );
			combine[ ( int )b[ 0 ] ][ ( int )b[ 1 ] ] = b[ 2 ];
			combine[ ( int )b[ 1 ] ][ ( int )b[ 0 ] ] = b[ 2 ];
		}
		
		scanf( "%d", &d );
		for( int j = 0; j < d; ++j ) {
			scanf( "%s", b );
			oppose[ ( int )b[ 0 ] ][ ( int )b[ 1 ] ] = 1;
			oppose[ ( int )b[ 1 ] ][ ( int )b[ 0 ] ] = 1;
		}
		
		scanf( "%d %s", &n, b );
		string rez = "";
		
		for( int j = 0; j < n; ++j ) {
			if( rez == "" ) rez.push_back( b[ j ] );
			else {
				int f = 0, len = ( int )rez.size();
				char cc = combine[ ( int )rez[ len-1 ] ][ ( int )b[ j ] ];
				
				if( cc != 0 ) rez[ len - 1 ] = cc;
				else {
					for( int k = 0; k < len; ++k )
						if( oppose[ ( int )rez[ k ] ][ ( int )b[ j ] ] )
							{ f = 1; break; }
					
					if( f ) rez = ""; else rez.push_back( b[ j ] );
				}
			}
			
			//printf( "(%s)\n", rez.c_str() );
		}
		
		int len = ( int )rez.size();
		
		printf( "Case #%d: [", i+1 );		
		for( int j = 0; j < len; ++j )
			printf( "%c%s", rez[ j ], j < len-1 ? ", " : "" );
		printf( "]\n" );
	}
	
	return( 0 );
}
