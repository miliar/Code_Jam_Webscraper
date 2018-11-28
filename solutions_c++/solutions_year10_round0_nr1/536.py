#include <cstdio>

int N, K;

void Read()
{
	scanf( "%d%d", &N, &K );
}

bool Result;

void Work()
{
	Result = ( K + 1 ) % ( 1 << N ) == 0;
}

void Write( int test )
{
	if( Result )
		printf( "Case #%d: ON\n", test );
	else
		printf( "Case #%d: OFF\n", test );
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
