#include <cstdio>

int N, M, A;

void Read()
{
	scanf( "%d%d%d", &N, &M, &A );
}

//bool Result;
//int X[ 3 ], Y[ 3 ];
//
//void Work()
//{
//	int i;
//	X[ 0 ] = 0;
//	Y[ 0 ] = 0;
//
//	Result = true;
//
//	Y[ 1 ] = 0;
//	X[ 2 ] = 0;
//	for( i = 1; i <= A / i; ++i )
//	{
//		if( A % i != 0 )
//			continue;
//		if( i <= N && A / i <= M )
//		{
//			X[ 1 ] = i;
//			Y[ 2 ] = A / i;
//			return;
//		}
//		else if( i <= M && A / i <= N )
//		{
//			X[ 1 ] = A / i;
//			Y[ 2 ] = i;
//			return;
//		}
//	}
//
//	Y[ 1 ] = M;
//	X[ 2 ] = N;
//	A = N * M - A;
//	if( A > 0 )
//	{
//		for( i = 1; i <= A / i; ++i )
//		{
//			if( A % i != 0 )
//				continue;
//			if( i <= N && A / i <= M )
//			{
//				X[ 1 ] = i;
//				Y[ 2 ] = A / i;
//				return;
//			}
//			else if( i <= M && A / i <= N )
//			{
//				X[ 1 ] = A / i;
//				Y[ 2 ] = i;
//				return;
//			}
//		}
//	}
//
//	Result = false;
//}

bool Result;
int X[ 3 ], Y[ 3 ];

void Work()
{
	Result = true;
	for( X[ 1 ] = 0; X[ 1 ] <= N; ++X[ 1 ] )
	{
		for( Y[ 1 ] = 0; Y[ 1 ] <= M; ++Y[ 1 ] )
		{
			for( X[ 2 ] = 0; X[ 2 ] <= N; ++X[ 2 ] )
			{
				for( Y[ 2 ] = 0; Y[ 2 ] <= M; ++Y[ 2 ] )
				{
					if( X[ 1 ] * Y[ 2 ] - X[ 2 ] * Y[ 1 ] == A )
						return;
				}
			}
		}
	}
	Result = false;
}

void Write( int i )
{
	if( Result )
		printf( "Case #%d: %d %d %d %d %d %d\n", i, X[ 0 ], Y[ 0 ], X[ 1 ], Y[ 1 ], X[ 2 ], Y[ 2 ] );
	else
		printf( "Case #%d: IMPOSSIBLE\n", i );
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