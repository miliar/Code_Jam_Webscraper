#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

static const int MAXN = 1012;

int X, S, R, T, N;
int B[ MAXN ], E[ MAXN ], W[ MAXN ];

void Read()
{
	int i;
	scanf( "%d%d%d%d%d", &X, &S, &R, &T, &N );
	for( i = 0; i < N; ++i )
	{
		scanf( "%d%d%d", &B[ i ], &E[ i ], &W[ i ] );
	}
}

bool Asc( int i, int j )
{
	return W[ i ] < W[ j ];
}

bool Desc( int i, int j )
{
	return W[ i ] > W[ j ];
}

double Result;
int Index[ MAXN ];

void Work()
{
	int i;

	for( i = 0; i < N; ++i )
	{
		Index[ i ] = i;
	}

	sort( Index, Index + N, Asc );

	double result = 0;
	double time = T;
	double x = X;

	for( i = 0; i < N; ++i )
	{
		x -= E[ i ] - B[ i ];
	}

	if( time > 0 )
	{
		double t = ( double )x / R;
		
		if( t > time )
		{
			result += time;
			result += ( double )( x - R * time ) / S;
			time = 0;
		}
		else
		{
			result += t;
			time -= t;
		}	
	}
	else
	{
		result += ( double )x / S;
	}

	for( i = 0; i < N; ++i )
	{
		if( time > 0 )
		{
			double t = ( double )( E[ Index[ i ] ] - B[ Index[ i ] ] ) / ( R + W[ Index[ i ] ] );
			if( t > time )
			{
				result += time;
				result += ( double )( E[ Index[ i ] ] - B[ Index[ i ] ] - ( R + W[ Index[ i ] ] ) * time ) / ( S + W[ Index[ i ] ] );
				time = 0;
			}
			else
			{
				result += t;
				time -= t;
			}
		}
		else
		{
			result += ( double )( E[ Index[ i ] ] - B[ Index[ i ] ] ) / ( S + W[ Index[ i ] ] );
		}
	}

	Result = result;
}

void Write()
{
	printf( "%.9lf\n", Result );
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
