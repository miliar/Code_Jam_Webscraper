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

static const int MAXN = 44;

int N;
char M[ MAXN ][ MAXN ];

void Read()
{
	int i;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%s", M[ i ] );
	}
}

int Result;
bool IsUsed[ MAXN ];

void Work()
{
	int i, j, k;
	Result = 0;
	memset( IsUsed, 0, sizeof( IsUsed ) );
	for( k = 0; k < N; ++k )
	{
		for( i = 0; i < N; ++i )
		{
			if( IsUsed[ i ] )
				continue;
			for( j = k + 1; j < N; ++j )
			{
				if( M[ i ][ j ] == '1' )
					break;
			}
			if( j == N )
				break;
			++Result;
		}
		IsUsed[ i ] = true;
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
