#include <stdio.h>
#include <string.h>

int main()
{
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "qr_a_small.out", "w", stdout );

	char en[] = "yhesocvxduiglbkrztnwjpfmaq";
	char str[1000];
	int T;

	scanf( "%d\n", &T );


	for ( int kase = 1; kase <= T; kase++ )
	{
		printf( "Case #%d: ", kase );

		gets(str);

		int len = strlen( str );

		for( int i = 0; i < len; i++ )
		{
			if( str[i] == ' ' )
				printf( " " );
			else
				printf( "%c", en[ str[i]-'a' ] );
		}

		printf( "\n" );
	}
	return 0;
}