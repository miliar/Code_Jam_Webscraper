#include <stdio.h>
#include <string.h>


bool available[10];
int k;
char str[10000];
int permu[10];
int minlen;

void generate(int cur) {
	if (cur==k) {
		char result[10000];
		memset(result,0,sizeof(result));
		for(int i=0;i<strlen(str)/k;i++)
			for(int j=0;j<k;j++)
			result[i*k+j] = str[i*k+permu[j]];

		int c=1;
		for(int i=1;i<strlen(result);i++)
			if (result[i] != result[i-1]) c++;
		if (c<minlen) minlen = c;
	}
	else {
		for(int i=0;i<k;i++)
			if (available[i])
			{
				permu[cur] = i;
				available[i] = false;
				generate(cur+1);
				available[i] = true;
			}
	}
}
void main(void){
	FILE* fin = fopen("perm.in","rt");
	FILE* fout = fopen("perm.out","wt");

	int N;
	fscanf(fin,"%d",&N);
	for(int i=0;i<N;i++){
		fscanf(fin, "%d\n", &k);
		fscanf(fin, "%s\n", str);
		
		for(int j=0;j<k;j++) available[j] = true;
		minlen = strlen(str)+1;
		generate(0);

		fprintf(fout,"Case #%d: %d\n",i+1, minlen);

	}

	fclose(fin);
	fclose(fout);
}