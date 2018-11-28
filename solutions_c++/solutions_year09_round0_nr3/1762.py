//Pipe input file to program and pipe output of program to outfile

#include <stdio.h>

#define debug 0
#define dprintf debug&&printf


char welcome[32] = "welcome to code jam";
int g[512][32];
char rad[512];

int rek(int r, int w) {
	if(g[r][w] != -1){
		return g[r][w];
	}
	int svar = 0;
	if(!welcome[w]){
		svar = 1;
	} else if(rad[r]){
		if(rad[r] == welcome[w]){
			svar = (rek(r+1, w) + rek(r+1, w+1))%1000;
		} else {
			svar = rek(r+1, w);
		}
	}
	return g[r][w] = svar;
}

int main(){
	int N;
	scanf("%d\n", &N);
	for(int fall=0;fall<N;fall++){	
		gets(rad);		
		for(int i=0;i<512;i++)
			for(int j=0;j<32;j++)
				g[i][j] = -1;
		dprintf("Input: '%s'\n", rad);
		printf("Case #%d: %04d\n", fall+1, rek(0, 0));
	}
	return 0;
}
