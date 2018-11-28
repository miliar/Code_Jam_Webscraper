#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;
pair< int, int > P[ 1005 ];

int t, n;

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d", &n );
		for( int j = 0; j < n; ++j )
			scanf( "%d %d", &P[ j ].first, &P[ j ].second );
		
		sort( P, P + n );
		int rez = 0;
		
		for( int j = 0; j < n; ++j )
			for( int k = 0; k < j; ++k )
				rez += ( P[ j ].second < P[ k ].second );
		
		printf( "Case #%d: %d\n", i+1, rez );
	}
	return( 0 );
}
