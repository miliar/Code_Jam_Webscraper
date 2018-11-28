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

static const int MAXN = 512;
static const int MOD = 100003;

int N;

void Read()
{
	scanf( "%d", &N );
}

int C[ MAXN + 1 ][ MAXN + 1 ];
int Count[ MAXN + 1 ][ MAXN + 1 ]; // number, last

void Init()
{
	int i, j, k;
	C[ 0 ][ 0 ] = 1;
	for( i = 1; i <= MAXN; ++i )
	{
		C[ i ][ 0 ] = 1;
		for( j = 1; j <= i; ++j )
		{
			C[ i ][ j ] = ( C[ i - 1 ][ j - 1 ] + C[ i - 1 ][ j ] ) % MOD;
		}
	}

	for( j = 2; j <= MAXN; ++j )
	{
		Count[ 1 ][ j ] = 1;
	}

	for( i = 2; i < MAXN; ++i )
	{
		for( j = i + 1; j <= MAXN; ++j )
		{
			for( k = 1; k < i; ++k )
			{
				Count[ i ][ j ] = ( int )( ( Count[ i ][ j ] + ( long long )Count[ k ][ i ] * C[ j - i - 1 ][ i - k - 1 ] ) % MOD );
			}
		}
	}
}

int Result;

void Work()
{
	int i;
	Result = 0;
	for( i = 1; i < N; ++i )
	{
		Result = ( Result + Count[ i ][ N ] ) % MOD;
	}
}

void Write( int test )
{
	printf( "Case #%d: %d\n", test, Result );
}

int T;

int main()
{
	int t;
	scanf( "%d", &T );
	Init();
	for( t = 0; t < T; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
