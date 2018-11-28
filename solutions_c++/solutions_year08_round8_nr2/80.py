#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

static const int MAXC = 12;
static const int MAXN = 312;

int N;
char C[ MAXN ][ MAXC + 1 ];
int H[ MAXN ];
int A[ MAXN ];
int B[ MAXN ];

void Read()
{
	int i, j;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%s%d%d", C[ i ], &A[ i ], &B[ i ] );
		H[ i ] = 0;
		for( j = 0; C[ i ][ j ] != 0; ++j )
		{
			H[ i ] = H[ i ] * 97 + C[ i ][ j ];
		}
		--A[ i ];
	}
}

bool Compare( int i, int j )
{
	return A[ i ] < A[ j ];
}

int Result;
int Index[ MAXN ];

void Work()
{
	int i, j;

	for( i = 0; i < N; ++i )
	{
		Index[ i ] = i;
	}

	sort( Index, Index + N, Compare );

	Result = -1;

	for( i = 0; i < ( 1 << N ); ++i )
	{
		set< int > h;
		int max = 0;
		int count = 0;
		for( j = 0; j < N; ++j )
		{
			if( !( i >> j & 1 ) )
				continue;
			if( h.find( H[ Index[ j ] ] ) == h.end() )
				if( h.size() == 3 )
					break;
				else
					h.insert( H[ Index[ j ] ] );
			if( max < A[ Index[ j ] ] )
				break;
			max = B[ Index[ j ] ];
			++count;
		}
		if( !( j == N && max == 10000 ) )
			continue;
		if( Result == -1 || Result > count )
			Result = count;
	}
}

void Write( int i )
{
	printf( "Case #%d: ", i );
	if( Result != -1 )
		printf( "%d\n", Result );
	else
		puts( "IMPOSSIBLE" );
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
