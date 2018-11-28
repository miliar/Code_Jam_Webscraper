#include <stdio.h>
#include <string.h>

struct element{
	int length;
	int repeat;
} table[20][512];

char s[512];
char *w="welcome to code jam";
int N;

void proc(){
}

int main(void){
	FILE *fin=fopen("C-large.in","r"), *fout=fopen("output.txt","w");

	fscanf(fin, "%d", &N);
	fgets(s, 512, fin);
	int i,j,R=19,C;
	for(int n=0; n<N; ++n){
		fgets(s, 512, fin);
		C = strlen(s);
		for(i=0; i<=R; ++i){ table[i][0].length=0; table[i][0].repeat=1; }
		for(j=0; j<=C; ++j){ table[0][j].length=0; table[0][j].repeat=1; }
		for(i=1; i<=R; ++i){
			for(j=1; j<=C; ++j){
				if(w[i-1]==s[j-1]){
					table[i][j].length=table[i-1][j-1].length+1;
					if(table[i][j].length==table[i][j-1].length){
						table[i][j].repeat=table[i-1][j-1].repeat+table[i][j-1].repeat;
					}else{
						table[i][j].repeat=table[i-1][j-1].repeat;
					}
				}else{
					table[i][j].length=table[i][j-1].length;
					table[i][j].repeat=table[i][j-1].repeat;
				}
				table[i][j].repeat%=10000;
			}
		}
		if(table[R][C].length!=strlen(w)) table[R][C].repeat=0;
		fprintf(fout, "Case #%d: %04d\n", n+1, table[R][C].repeat);
	}

	fclose(fin); fclose(fout);
	return 0;
}