#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

static const int MAXN = 111;
static const int MAXK = 33;

int N, K;
int Price[ MAXN ][ MAXK ];

void Read()
{
	int i, j;
	scanf( "%d%d", &N, &K );
	for( i = 0; i < N; ++i )
	{
		for( j = 0; j < K; ++j )
		{
			scanf( "%d", &Price[ i ][ j ] );
		}
	}
}

int Result;
bool Less[ MAXN ][ MAXN ];
int Pair[ MAXN ];
bool IsUsed[ MAXN ];

bool DFSLeft( int k );

inline bool DFSRight( int k )
{
	IsUsed[ k ] = true;
	if( Pair[ k ] == -1 )
	{
		return true;
	}
	else
	{
		if( DFSLeft( Pair[ k ] ) )
			return true;
	}
	return false;
}

bool DFSLeft( int k )
{
	int i;
	for( i = 0; i < N; ++i )
	{
		if( Less[ k ][ i ] && Pair[ i ] != k )
		{
			if( !IsUsed[ i ] && DFSRight( i ) )
			{
				Pair[ i ] = k;
				return true;
			}
		}
	}
	return false;
}

void Work()
{
	int i, j, k;

	for( i = 0; i < N; ++i )
	{
		for( j = 0; j < N; ++j )
		{
			Less[ i ][ j ] = true;
			for( k = 0; k < K; ++k )
			{
				if( Price[ i ][ k ] >= Price[ j ][ k ] )
				{
					Less[ i ][ j ] = false;
				}
			}
		}
	}

	memset( Pair, -1, sizeof( Pair ) );

	Result = N;
	for( i = 0; i < N; ++i )
	{
		memset( IsUsed, 0, sizeof( IsUsed ) );
		if( DFSLeft( i ) )
			--Result;
	}
}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
}

int T;

int main()
{
	int t;
	scanf( "%d", &T );
	for( t = 0; t < T; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
