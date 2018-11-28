#include <stdio.h>
#include <string.h>

char code[26] = {
	  'y',
	  'h',
	  'e',
	  's',
	  'o',
	  'c',
	  'v',
	  'x',
	  'd',
	  'u',
	  'i',
	  'g',
	  'l',
	  'b',
	  'k',
	  'r',
	  'z',
	  't',
	  'n',
	  'w',
	  'j',
	  'p',
	  'f',
	  'm',
	  'a',
	  'q'	
};

int n;
char g[102];
int gLen;

int main(){
	scanf("%d ", &n);
	for(int cases = 1; cases<= n; cases++){
		gets(g);
		gLen = strlen(g);
		printf("Case #%d: ", cases);
		for(int i = 0; i < gLen; i++){
			if(g[i] == ' ')
				printf(" ");
			else
				printf("%c", code[g[i] - 'a']);
		}
		printf("\n");
	}
	return 0;
}




