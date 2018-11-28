#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <memory.h>

static const int MAXN = 1012;

int N;
int C[ MAXN ];

void Read()
{
	int i;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &C[ i ] );
	}
}

int Result;

void Work()
{
	int i;

	Result = -1;

	int r = 0;
	for( i = 0; i < N; ++i )
	{
		r ^= C[ i ];
	}
	if( r != 0 )
		return;

	Result = 0;
	int m = -1;
	for( i = 0; i < N; ++i )
	{
		Result += C[ i ];
		if( m == -1 || m > C[ i ] )
			m = C[ i ];
	}

	Result -= m;
}

void Write( int t )
{
	printf( "Case #%d: ", t );
	if( Result == -1 )
		printf( "NO\n" );
	else
		printf( "%d\n", Result );
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
