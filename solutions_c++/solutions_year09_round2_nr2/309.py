#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
vector< int > znam;

int t, n;
char st[ 25 ];

void razdvoji( void ) {
	znam.clear();
	for( int i = 0; st[ i ] != 0; ++i )
		znam.push_back( st[ i ] - '0' );
}

void ispis( void ) {
	for( int i = 0; i < ( int )znam.size(); ++i )
		printf( "%d", znam[ i ] );
	printf( "\n" );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%s", st );
		razdvoji();
		
		if( !next_permutation( znam.begin(), znam.end() ) ) {
			znam.push_back( 0 );
			sort( znam.begin(), znam.end() );
			
			int tpoz = 0;
			while( znam[ tpoz ] == 0 ) ++tpoz;
			
			int tmp = znam[ 0 ];
			znam[ 0 ] = znam[ tpoz ];
			znam[ tpoz ] = tmp;
		}
		
		printf( "Case #%d: ", i + 1 ); ispis();
	}
	return( 0 );
}
