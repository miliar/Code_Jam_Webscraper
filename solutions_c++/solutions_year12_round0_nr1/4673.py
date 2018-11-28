#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	
	int n, len;
	char in[110], trash[10];
	scanf("%d", &n);
	gets(trash);
	for(int i =0; i<n; i++){
		gets(in);
		len = strlen(in);
		printf("Case #%d: ", i+1);
		for(int j =0; j<len; j++){
			if(in[j] == 'a')	printf("y");
			else if(in[j] == 'b')	printf("h");
			else if(in[j] == 'c') printf("e");
			else if(in[j] == 'd') printf("s");
			else if(in[j] == 'e') printf("o");
			else if(in[j] == 'f') printf("c");
			else if(in[j] == 'g') printf("v");
			else if(in[j] == 'h') printf("x");
			else if(in[j] == 'i') printf("d");
			else if(in[j] == 'j') printf("u");
			else if(in[j] == 'k') printf("i");
			else if(in[j] == 'l') printf("g");
			else if(in[j] == 'm') printf("l");
			else if(in[j] == 'n') printf("b");
			else if(in[j] == 'o') printf("k");
			else if(in[j] == 'p') printf("r");
			else if(in[j] == 'q') printf("z");
			else if(in[j] == 'r') printf("t");
			else if(in[j] == 's') printf("n");
			else if(in[j] == 't') printf("w");
			else if(in[j] == 'u') printf("j");
			else if(in[j] == 'v') printf("p");
			else if(in[j] == 'w') printf("f");
			else if(in[j] == 'x') printf("m");
			else if(in[j] == 'y') printf("a");
			else if(in[j] == 'z') printf("q");
			else if(in[j] == ' ') printf(" ");
		}
		printf("\n");
	}


return 0;
}
