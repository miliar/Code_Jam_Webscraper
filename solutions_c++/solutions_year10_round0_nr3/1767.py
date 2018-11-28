#include <cstdio>
#include <cstdlib>
#include <cstring>

int t, n, k, r, g[ 1005 ], next[ 1005 ], ind[ 1005 ];
long long last[ 1005 ], suma[ 1005 ];

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d %d %d", &r, &k, &n );
		for( int j = 0; j < n; ++j )
			scanf( "%d", &g[ j ] );
		
		int p = 0, e = 0, s = 0, c = 0;
		for( int j = 0; j < n; ++j ) {
			if( j != 0 ) s -= g[ p++ ];
			while( s + g[ e ] <= k ) {
				s += g[ e++ ];
				if( e == n ) e = 0;
				if( e == p ) break;
			}
			next[ p ] = e;
			suma[ p ] = s;
		}
		
		memset( last, -1, sizeof( last ) );
		memset( ind, -1, sizeof( ind ) );
		
		long long profit = 0; p = 0;
		while( r > 0 && ind[ p ] == -1 ) {
			last[ p ] = profit;
			ind[ p ] = c++;
			
			profit += suma[ p ];
			p = next[ p ]; --r;
		}
		
		if( r > 0 ) {
			long long ciklvr = profit - last[ p ];
			profit = last[ p ] + ciklvr * ( r / ( c - ind[ p ] ) + 1 );
			r = r % ( c - ind[ p ] );
			
			for( ; r > 0; --r ) {
				profit += suma[ p ];
				p = next[ p ];
			}
		}
		
		printf( "Case #%d: %Ld\n", i+1, profit );
	}
	
	return( 0 );
}
