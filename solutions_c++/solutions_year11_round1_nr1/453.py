#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

long long N;
int Pg, Pd;

void Read()
{
	scanf( "%lld%d%d", &N, &Pd, &Pg );
}

int nod( int x, int y )
{
	while( true )
	{
		if( x == 0 )
			return y;
		y %= x;
		if( y == 0 )
			return x;
		x %= y;
	}
}

bool Result; 

void Work()
{
	Result = false;

	if( 100 / nod( Pd, 100 ) > N )
		return;

	if( Pd != 0 && Pg == 0 )
		return;

	if( Pd != 100 && Pg == 100 )
		return;

	Result = true;
}

void Write( int t )
{
	printf( "Case #%d: ", t );
	if( Result )
		puts( "Possible" );
	else
		puts( "Broken" );
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
