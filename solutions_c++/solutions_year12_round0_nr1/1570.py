#include <cstdio>
#include <cstring>

const char str[30] = "yhesocvxduiglbkrztnwjpfmaq";

char s[105];

int main()
{
	int cas;
	scanf( "%d" , &cas );
	gets(s);
	for ( int i = 1; i <= cas; i++ ) {
		printf( "Case #%d: " , i );
		gets(s);
		int len = strlen(s);
		for ( int j = 0; j < len; j++ ) {
			if ( s[j] >= 'a' && s[j] <= 'z' ) printf( "%c" , str[s[j]-'a'] );
			else printf( "%c" , s[j] );
		}
		printf( "\n" );
	}
	return 0;
}
