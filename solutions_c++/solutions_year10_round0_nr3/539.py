#include <cstdio>
#include <memory.h>

static const int MAXN = 1011;

int R, K, N;
int G[ MAXN ];

void Read()
{
	int i;
	scanf( "%d%d%d", &R, &K, &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &G[ i ] );
	}
}

long long Result;

long long Profit[ MAXN ];
int Count[ MAXN ];

void Work()
{
	int i;
	Result = 0;
	memset( Profit, -1, sizeof( Profit ) );
	memset( Count, -1, sizeof( Count ) );

	Profit[ 0 ] = 0;
	Count[ 0 ] = 0;

	int curr = 0;
	int count = 0;
	while( count < R )
	{
		int sum = 0;
		for( i = 0; i < N && sum + G[ ( curr + i ) % N ] <= K; ++i )
		{
			sum += G[ ( curr + i ) % N ];
		}

		Result += sum;
		++count;
		curr = ( curr + i ) % N;

		if( Profit[ curr ] == -1 )
		{
			Profit[ curr ] = Result;
			Count[ curr ] = count;
		}
		else if( ( R - count ) % ( count - Count[ curr ] ) == 0 )
		{
			int x = ( R - count ) / ( count - Count[ curr ] );
			Result += x * ( Result - Profit[ curr ] );
			break;
		}
	}
}

void Write( int test )
{
	printf( "Case #%d: %lld\n", test, Result );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 0; i < t; ++i )
	{
		Read();
		Work();
		Write( i + 1 );
	}
	return 0;
}
