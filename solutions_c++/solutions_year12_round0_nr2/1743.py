#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

static const int MAXN = 111;

int N, S, T, A[ MAXN ];

void Read()
{
	int i;
	scanf( "%d%d%d", &N, &S, &T );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &A[ i ] );
	}
}

int Surprise( int x )
{
	if( x < 2 )
		return x;
	return ( x + 1 ) / 3 + 1;
}

int Normal( int x )
{
	if( x == 0 )
		return 0;
	return ( x - 1 ) / 3 + 1;
}

int Result;

void Work()
{
	int i;
	Result = 0;

	for( i = 0; i < N; ++i )
	{
		if( Normal( A[ i ] ) >= T )
			++Result;
		else if( S > 0 && Surprise( A[ i ] ) >= T )
		{
			++Result;
			--S;
		}
	}
}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 1; i <= t; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
