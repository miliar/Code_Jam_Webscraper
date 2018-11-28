#include <stdlib.h>
#include <stdio.h>

#define MAX_WORDS 5000
#define MAX_LEN 15

int L, D, N;

int words[MAX_WORDS][MAX_LEN];
int pattern[MAX_LEN];
int i,j,k,c;


int read_token() {
	int res=0;
	int loop=-1;
	char c;

	while(loop!=0) {
		scanf("%c", &c);
		switch(c) {
			case '\r':
			case '\n':
				break;
			case '(':
				loop=1;
				break;
			case ')':
				loop=0;
				break;
			default:
				res|=1<<(c-'a');
				loop++;
		}
	}				
	return res;
}

int main() {
	scanf("%d %d %d", &L, &D, &N);
	for (i=0; i<D; i++) 
		for (j=0; j<L; j++)
			words[i][j]=read_token();

	for (k=1; k<=N; k++) {
		for (j=0; j<L; j++)
			pattern[j]=read_token();

		c=0;
		for (i=0; i<D; i++) {
			for (j=0; j<L; j++)
				if ((pattern[j] & words[i][j]) != words[i][j]) break;
			if (j==L) c++;
		}
		printf("Case #%d: %d\n", k, c);
	}

}
