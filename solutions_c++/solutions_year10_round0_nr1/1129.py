#include <stdio.h>
#include<memory.h>
#include<string.h>
int main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T;
	int N, K;
	int i;
	fscanf(fp, "%d", &T);
	for(i = 1; i <= T; ++i){
		fscanf(fp, "%d%d", &N, &K);
		++K;
		N = 32 - N;
		fprintf(ofp, "Case #%d: %s\n", i, (K<<N)?"OFF":"ON");
	}

	return 0;
}