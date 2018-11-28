#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
using namespace std;

static const int MAXN = 1012;

int N;
int A[ MAXN ];

void Read()
{
	int i;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &A[ i ] );
	}
}

double Result;
bool IsUsed[ MAXN ];

void Work()
{
	int i, j, r;

	for( i = 0; i < N; ++i )
	{
		--A[ i ];
	}

	memset( IsUsed, 0, sizeof( IsUsed ) );

	Result = 0;

	for( i = 0; i < N; ++i )
	{
		if( IsUsed[ i ] )
			continue;
		r = 0;
		for( j = i; !IsUsed[ j ]; j = A[ j ] )
		{
			IsUsed[ j ] = true;
			++r;
		} 
		if( r > 1 )
		Result += r;
	}
}

void Write( int t )
{
	printf( "Case #%d: %.6lf\n", t, Result );
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
