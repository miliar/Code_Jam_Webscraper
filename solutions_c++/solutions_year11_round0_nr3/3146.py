#include <cstdio>

void cando( int *, int, int, int, int, int, int, int & );

int main()
{
	int t, n, caso = 0, T[ 20 ], max;
	scanf( "%d", &t );
	while( caso++ < t )
	{
		scanf( "%d", &n );
		for( int i = 0; i < n; ++i )
			scanf( "%d", &T[ i ] );
		max = -1;
		cando( T, n, 0, 0, 0, 0, 0, max );
		if( max == -1 )
			printf( "Case #%d: NO\n", caso );
		else
			printf( "Case #%d: %d\n", caso, max );
	}
	return 0;
}

void cando( int *T, int n, int sumA, int sumB, int realA, int realB, int ix, int &max )
{
	if( ix >= n )
	{
		if( sumA == sumB && realA > max && realA > 0 && realB > 0 )
			max = realA;
	}
	else
	{
		/*printf( "%d.- [%d %d, %d %d] -> [%d %d, %d %d] o [%d %d, %d %d]\n", ix, sumA, sumB, realA, realB, sumA^T[ix], sumB, realA+T[ix],
		     realB, sumA, sumB^T[ix], realA, realB+T[ix] );*/
		cando( T, n, sumA^T[ ix ], sumB, realA + T[ ix ], realB, ix + 1, max );
		cando( T, n, sumA, sumB^T[ ix ], realA, realB + T[ ix ], ix + 1, max );
	}
}

