#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXK = 20;
const int MAXS = 50012;

int K;
char S[ MAXS + 1 ];

void Read()
{
	scanf( "%d", &K );
	scanf( "%s", S );
}

int Result;
int Index[ MAXK ];
int T[ MAXS ];

void Work()
{
	int i, j; 
	for( i = 0; i < K; ++i )
	{
		Index[ i ] = i;
	}

	Result = -1;

	int len = ( int )strlen( S );
	do
	{
		int curr = 1;
		for( i = 0; i < len; i += K )
		{
			for( j = 0; j < K; ++j )
			{
				T[ i + j ] = S[ i + Index[ j ] ];
			} 
		}

		for( i = 1; i < len; ++i )
		{
			if( T[ i - 1 ] != T[ i ] )
				++curr;
		}

		if( Result == -1 || Result > curr )
			Result = curr;
	} while( next_permutation( Index, Index + K ) );
}

void Write( int i )
{
	printf( "Case #%d: %d\n", i, Result );
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
