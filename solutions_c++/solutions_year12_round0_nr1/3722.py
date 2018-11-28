#include <cstdio>
#include <cstring>

char c;
char cyph[] = { "yhesocvxduiglbkrztnwjpfmaq" };

int main (void) {
	
	int T, N;
	scanf ( "%d", &T );
	getc ( stdin );
	
	for ( int t=1; t<=T; ++t ) {
		
		printf ( "Case #%d: ", t );
		while ( ( c = getc ( stdin ) ) != '\n' ) {
			if ( c == ' ' ) printf ( "%c", c );
			else printf ( "%c", cyph[c-'a'] );
			}
		printf ( "\n" );
		
		}
	
}
