#include <cstdio>

const int MAXM = 10012;

int M, V;
int G[ 1 + MAXM ];
int C[ 1 + MAXM ];
int I[ 1 + MAXM ];

void Read()
{
	int i;
	scanf( "%d%d", &M, &V );
	for( i = 1; i <= ( M >> 1 ); ++i )
	{
		scanf( "%d%d", &G[ i ], &C[ i ] );
	}
	for( ; i <= M; ++i )
	{
		scanf( "%d", &I[ i ] );
	}
}

int Result;
int Min[ 2 ][ 1 + MAXM ];

void Work()
{
	int i;
	for( i = M; i > ( M >> 1 ); --i )
	{
		Min[ I[ i ] ][ i ] = 0;
		Min[ !I[ i ] ][ i ] = -1;
	}
	for( ; i >= 1; --i )
	{
		if( G[ i ] ) // AND
		{
			int min = -1;
			if( Min[ 1 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( C[ i ] && Min[ 1 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ] + 1;
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( C[ i ] && Min[ 0 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ] + 1;
				if( min == -1 || min > new_min )
					min = new_min;
			}
			Min[ 1 ][ i ] = min;

			min = -1;
			if( Min[ 0 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( Min[ 0 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( Min[ 1 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			Min[ 0 ][ i ] = min;
		}
		else // OR
		{
			int min = -1;
			if( Min[ 1 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( Min[ 1 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( Min[ 0 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			Min[ 1 ][ i ] = min;

			min = -1;
			if( Min[ 0 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ];
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( C[ i ] && Min[ 0 ][ i << 1 ] != -1 && Min[ 1 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 0 ][ i << 1 ] + Min[ 1 ][ i << 1 | 1 ] + 1;
				if( min == -1 || min > new_min )
					min = new_min;
			}
			if( C[ i ] && Min[ 1 ][ i << 1 ] != -1 && Min[ 0 ][ i << 1 | 1 ] != -1 )
			{
				int new_min = Min[ 1 ][ i << 1 ] + Min[ 0 ][ i << 1 | 1 ] + 1;
				if( min == -1 || min > new_min )
					min = new_min;
			}
			Min[ 0 ][ i ] = min;
		}
	}

	Result = Min[ V ][ 1 ];
}

void Write( int i )
{
	if( Result == -1 )
		printf( "Case #%d: IMPOSSIBLE\n", i );
	else
		printf( "Case #%d: %d\n", i, Result );
}

int main()
{
	int n, i;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
