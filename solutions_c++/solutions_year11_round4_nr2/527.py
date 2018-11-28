#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

static const int MAXR = 523;
static const int MAXC = 523;

int R, C, D;
int W[ MAXR ][ MAXC ];

void Read()
{
	int i, j;
	scanf( "%d%d%d", &R, &C, &D );
	for( i = 0; i < R; ++i )
	{
		for( j = 0; j < C; ++j )
		{
			scanf( "%1d", &W[ i ][ j ] );
		}
	}
}

int K;
int S[ MAXR ][ MAXC ];
int I[ MAXR ][ MAXC ];
int J[ MAXR ][ MAXC ];

int Fi( int i, int j )
{
	return W[ i ][ j ] * ( 2 * i + 1 );
}

int Fj( int i, int j )
{
	return W[ i ][ j ] * ( 2 * j + 1 );
}

void Work()
{
	int i, j;

	memset( &S, 0, sizeof( S ) );

	for( i = 1; i <= R; ++i )
	{
		for( j = 1; j <= C; ++j )
		{
			W[ i - 1 ][ j - 1 ] += D;
			I[ i ][ j ] = I[ i - 1 ][ j ] + I[ i ][ j - 1 ] - I[ i - 1 ][ j - 1 ] + Fi( i - 1, j - 1 );
			J[ i ][ j ] = J[ i - 1 ][ j ] + J[ i ][ j - 1 ] - J[ i - 1 ][ j - 1 ] + Fj( i - 1, j - 1 );
			S[ i ][ j ] = S[ i - 1 ][ j ] + S[ i ][ j - 1 ] - S[ i - 1 ][ j - 1 ] + W[ i - 1 ][ j - 1 ];
		}
	}


	for( K = min( R, C ); K >= 3; --K )
	{
		for( i = 0; i + K <= R; ++i )
		{
			for( j = 0; j + K <= C; ++j )
			{
				int wi = I[ i + K ][ j + K ] + I[ i ][ j ] - I[ i ][ j + K ] - I[ i + K ][ j ];
				int wj = J[ i + K ][ j + K ] + J[ i ][ j ] - J[ i ][ j + K ] - J[ i + K ][ j ];
				int w = S[ i + K ][ j + K ] + S[ i ][ j ] - S[ i ][ j + K ] - S[ i + K ][ j ];

				wi -= Fi( i, j ); // * ( 2 * i + 1 );
				wi -= Fi( i, j + K - 1 ); // * ( 2 * i;
				wi -= Fi( i + K - 1, j ); // * ( i + K - 1 );
				wi -= Fi( i + K - 1, j + K - 1 ); // * ( i + K - 1 );

				wj -= Fj( i, j ); // * j;
				wj -= Fj( i, j + K - 1 ); // * ( j + K - 1 );
				wj -= Fj( i + K - 1, j ); // * j;
				wj -= Fj( i + K - 1, j + K - 1 ); // * ( j + K - 1 );

				w -= W[ i ][ j ];
				w -= W[ i ][ j + K - 1 ];
				w -= W[ i + K - 1 ][ j ];
				w -= W[ i + K - 1 ][ j + K - 1 ];

				if( wi == ( i * 2 + K ) * w &&
					 wj == ( j * 2 + K ) * w )
					return;
			}
		}
	}

	K = -1;
}

void Write()
{
	if( K != -1 )
		printf( "%d\n", K );
	else
		puts( "IMPOSSIBLE" );
}

int main()
{
	int i, t;
	scanf( "%d", &t );
	for( i = 0; i < t; ++i )
	{
		Read();
		Work();
		printf( "Case #%d: ", i + 1 );
		Write();
	}
	return 0;
}
