#include <cstdio>
#include <cstdlib>

int main()
{
	int t, n, caso = 0, P[ 2 ], turns = 0, N[ 110 ], L[ 2 ], ix;
	char R[ 3 ];
	scanf( "%d", &t );
	while( caso++ < t )
	{
		scanf( "%d", &n );
		P[ 0 ] = P[ 1 ] = 1, L[ 0 ] = L[ 1 ] = turns = 0;
		for( int i = 0; i < n; ++i )
		{
			scanf( "%s%d", R, &N[ i ] );
			if( R[ 0 ] == 'O' )/*orange*/
				ix = 0;
			else
				ix = 1;
			int steps = abs( N[ i ] - P[ ix ] );
			int done = turns - L[ ix ];
			/*printf( "%c %d, Done %d, required %d\n", R[0], N[ i ], done, steps );*/
			if( done >= steps )
				steps = 0;
			else
				steps -= done;
			turns += steps + 1; /* move to the spot plus push */
			L[ ix ] = turns; /* update */
			P[ ix ] = N[ i ];
		}
		printf( "Case #%d: %d\n", caso, turns );
	}
	return 0;
}

