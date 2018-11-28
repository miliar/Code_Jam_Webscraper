#include <cstdio>
#include <cstring>

char str [500];

char dic [] = "yhesocvxduiglbkrztnwjpfmaq";

int main () {
	int TC, len;
	scanf("%d ", &TC);
	
	for ( int cc = 1; cc <= TC; ++cc ) {
		printf("Case #%d: ", cc);
	
		gets( str );
		len = strlen( str );
		for ( int i = 0; i < len; ++i ) {
			if ( str[i] == ' ' )
				printf(" ");
			else
				printf("%c", dic[ str[i] - 'a' ] );
		}
		printf("\n");
	}
	return 0;
}
