#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

char Map[ 256 ];

void Init()
{
	int i;
	for( i = 'a'; i <= 'z'; ++i )
	{
		Map[ i ] = i;
	}

	Map[ 'z' ] = 'q';
	Map[ 'q' ] = 'z';

	const char *g = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	const char *s = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	while( *g != '\0' && *s != '\0' )
	{
		Map[ *g++ ] = *s++;
	}
}

char Str[ 256 ];

void Work( int test )
{
	gets( Str );
	printf( "Case #%d: ", test );
	for( const char *s = Str; *s != '\0'; ++s )
	{
		if( *s == ' ' )
			putchar( ' ' );
		else
			putchar( Map[ *s ] );
	}
	putchar( '\n' );
}

int main()
{
	int i, t;
	Init();
	scanf( "%d\n", &t );
	for( i = 1; i <= t; ++i )
	{
		Work( i );
	}
	return 0;
}
