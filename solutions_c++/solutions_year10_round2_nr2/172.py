#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <ctime>
using namespace std;

static const int MAXN = 56;

int N, K, B, T;
int X[ MAXN ];
int V[ MAXN ];

void Read()
{
	int i;
	scanf( "%d%d%d%d", &N, &K, &B, &T );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &X[ i ] );
	}
	for( i = 0; i < N; ++i )
	{
		scanf( "%d", &V[ i ] );
	}
}

int Result;

void Work()
{
	int i;

	Result = 0; 

	int good = 0, bad = 0;
	for( i = N - 1; i >= 0; --i )
	{
		if( X[ i ] + V[ i ] * T >= B )
		{
			++good;
			Result += bad;
		}
		else
		{
			++bad;
		}
		if( good == K )
			return;
	}

	Result = -1;
}

void Write( int test )
{
	if( Result == -1 )
		printf( "Case #%d: IMPOSSIBLE\n", test );
	else
		printf( "Case #%d: %d\n", test, Result );
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
