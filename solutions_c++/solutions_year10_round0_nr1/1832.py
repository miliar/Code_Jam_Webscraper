#include <cstdio>

void tobinary( int, int, bool * );

int main()
{
	int n, t, k, co = 0;
	scanf( "%d", &t );
	while( t-- > 0 )
	{
		scanf( "%d%d", &n, &k );
		bool M[50];
		for( int i = 0; i < 50; ++i )
			M[i] = false;
		tobinary( k, n, M );
		for( int i = 0; i < n - 1; ++i )
			M[ n - 1 ] = M[ n - 1 ] && M[ i ];
		if( M[n-1] )
			printf( "Case #%d: ON\n", ++co );
		else
			printf( "Case #%d: OFF\n", ++co );
	}
	return 0;
}

void tobinary( int k, int n, bool *M )
{
	int i = 0;
	while( k > 0 )
	{
		M[ i++ ] = ( k%2 ) == 0 ? false : true;
		if( i >= n )
			break;
		k /= 2;
	}
}

