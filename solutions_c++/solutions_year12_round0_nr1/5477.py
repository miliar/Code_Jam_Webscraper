#include <cstdio>

int main()
{
	int t, c = 0;
	char G;
	char M[ 255 ];
	M[ 'a' ] = 'y', M[ 'b' ] = 'h', M[ 'c' ] = 'e', M[ 'd' ] = 's', M[ 'e' ] = 'o';
	M[ 'f' ] = 'c', M[ 'g' ] = 'v', M[ 'h' ] = 'x', M[ 'i' ] = 'd', M[ 'j' ] = 'u';
	M[ 'k' ] = 'i', M[ 'l' ] = 'g', M[ 'm' ] = 'l', M[ 'n' ] = 'b', M[ 'o' ] = 'k';
	M[ 'p' ] = 'r', M[ 'q' ] = 'z', M[ 'r' ] = 't', M[ 's' ] = 'n', M[ 't' ] = 'w';
	M[ 'u' ] = 'j', M[ 'v' ] = 'p', M[ 'w' ] = 'f', M[ 'x' ] = 'm', M[ 'y' ] = 'a';
	M[ 'z' ] = 'q';
	scanf( "%d\n", &t );
	while( c++ < t )
	{
		printf( "Case #%d: ", c );
		while( ( G = getchar() ) != '\n' && G != EOF )
			if( G >= 'a' && G <= 'z' )
				putchar( M[ G ] );
			else
				putchar( ' ' );
		putchar( '\n' );
	}
	return 0;
}
