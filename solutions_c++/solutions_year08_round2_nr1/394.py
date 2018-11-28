#include <cstdio>

int N, A, B, C, D, X0, Y0, M;

void Read()
{
	scanf( "%d%d%d%d%d%d%d%d", &N, &A, &B, &C, &D, &X0, &Y0, &M );
}

long long Result;

void Work()
{
	int i;
	int count[ 3 ][ 3 ] = { 0 };
	int x, y;

	x = X0;
	y = Y0;
	for( i = 0; i < N; ++i )
	{
		++count[ x % 3 ][ y % 3 ];
		x = ( int )( ( ( long long )A * x + B ) % M );
		y = ( int )( ( ( long long )C * y + D ) % M );
	}

	Result = 0;
	for( x = 0; x < 3; ++x )
	{
		for( y = 0; y < 3; ++y )
		{
			Result += ( long long )count[ x ][ y ] * ( count[ x ][ y ] - 1 ) * ( count[ x ][ y ] - 2 ) / 6;
		}
	}
	for( x = 0; x < 3; ++x )
	{
		Result += ( long long )count[ x ][ 0 ] * count[ x ][ 1 ] * count[ x ][ 2 ];
	}
	for( y = 0; y < 3; ++y )
	{
		Result += ( long long )count[ 0 ][ y ] * count[ 1 ][ y ] * count[ 2 ][ y ];
	}
	Result += ( long long )count[ 0 ][ 0 ] * count[ 1 ][ 1 ] * count[ 2 ][ 2 ];
	Result += ( long long )count[ 0 ][ 0 ] * count[ 1 ][ 2 ] * count[ 2 ][ 1 ];
	Result += ( long long )count[ 0 ][ 1 ] * count[ 1 ][ 2 ] * count[ 2 ][ 0 ];
	Result += ( long long )count[ 0 ][ 1 ] * count[ 1 ][ 0 ] * count[ 2 ][ 2 ];
	Result += ( long long )count[ 0 ][ 2 ] * count[ 1 ][ 0 ] * count[ 2 ][ 1 ];
	Result += ( long long )count[ 0 ][ 2 ] * count[ 1 ][ 1 ] * count[ 2 ][ 0 ];
}

void Write( int i )
{
	printf( "Case #%d: %I64d\n", i, Result );
}

int main()
{
	int i, n;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
