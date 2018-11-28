#include <cstdio>
#include <cstdlib>
#include <string>

int nbLines = 0 ;
char text[30][102] ;
char trash ;

char binder[26] = {
	'y', 'h', 'e', 's', 'o',
	'c', 'v', 'x', 'd', 'u',
	'i', 'g', 'l', 'b', 'k',
	'r', 'z', 't', 'n', 'w',
	'j', 'p', 'f', 'm', 'a',
	'q'
} ;

int main() {
	scanf("%d", &nbLines) ;
	
	scanf("%c", &trash) ;
	for (int i = 0 ; i < nbLines ; i++) {
		
		fgets(text[i], sizeof(text[i]), stdin) ;
	}
	
	for (int i = 0 ; i < nbLines ; i++) {
		
		printf("Case #%d: ", i+1) ;
		int j = 0 ;
		while (text[i][j] != '\n') {
			if (text[i][j] != ' ') {
				text[i][j] = binder[text[i][j] - 'a'] ;
			}
			printf("%c", text[i][j]) ;
			j++ ;
		}
		printf("\n") ;
	}
	
	return 0 ;
}