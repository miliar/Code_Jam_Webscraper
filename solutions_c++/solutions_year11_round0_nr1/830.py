#include <cstdio>
#include <cstdlib>

static const int MAXN = 111;

int N;
char P[ MAXN ];
int R[ MAXN ];

void Read()
{
	int i;
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		scanf( " %c%d", &P[ i ], &R[ i ] );
	}
}

int Result;

void Work()
{
	int i;
	int t1, t2, b1, b2;
	t1 = t2 = 0;
	b1 = b2 = 1;

	for( i = 0; i < N; ++i )
	{
		if( P[ i ] == 'O' )
		{
			t1 += abs( R[ i ] - b1 ) + 1;
			b1 = R[ i ];
			if( t1 <= t2 )
				t1 = t2 + 1;
		}
		else
		{
			t2 += abs( R[ i ] - b2 ) + 1;
			b2 = R[ i ];
			if( t2 <= t1 )
				t2 = t1 + 1;
		}
	}

	if( t1 > t2 )
		Result = t1;
	else
		Result = t2;
}

void Write( int t )
{
	printf( "Case #%d: %d\n", t, Result );
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
