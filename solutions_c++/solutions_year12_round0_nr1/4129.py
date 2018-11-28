#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main(){
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out","w",stdout);
	int n;
	scanf("%d\n", &n);
	char code[n][101];
	for(int i=0; i<n; i++){
		//scanf("%s", &code[i]);
		gets(code[i]);
	}
	char out[n][101];
	for(int i=0; i<n; i++){
		for(int j=0; j<strlen(code[i]); j++){
			switch(code[i][j]) {
				case 'a': out[i][j] = 'y'; break;
				case 'b': out[i][j] = 'h'; break;
				case 'c': out[i][j] = 'e'; break;
				case 'd': out[i][j] = 's'; break;
				case 'e': out[i][j] = 'o'; break;
				case 'f': out[i][j] = 'c'; break;
				case 'g': out[i][j] = 'v'; break;
				case 'h': out[i][j] = 'x'; break;
				case 'i': out[i][j] = 'd'; break;
				case 'j': out[i][j] = 'u'; break;
				case 'k': out[i][j] = 'i'; break;
				case 'l': out[i][j] = 'g'; break;
				case 'm': out[i][j] = 'l'; break;
				case 'n': out[i][j] = 'b'; break;
				case 'o': out[i][j] = 'k'; break;
				case 'p': out[i][j] = 'r'; break;
				case 'q': out[i][j] = 'z'; break;
				case 'r': out[i][j] = 't'; break;
				case 's': out[i][j] = 'n'; break;
				case 't': out[i][j] = 'w'; break;
				case 'u': out[i][j] = 'j'; break;
				case 'v': out[i][j] = 'p'; break;
				case 'w': out[i][j] = 'f'; break;
				case 'x': out[i][j] = 'm'; break;
				case 'y': out[i][j] = 'a'; break;
				case 'z': out[i][j] = 'q'; break;
				case ' ': out[i][j] = ' '; break;
			}
		}
		out[i][strlen(code[i])]='\0';
	}
	for(int i=0; i<n; i++){
		printf("Case #%d: %s\n", i+1, out[i]);
	}
	
	//system("pause");
}
