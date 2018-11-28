#include <stdio.h>
#include<memory.h>
#include<string.h>

	int T;
	int R, K, N;
	int sum;
	int i;//case counter
	int j;//round counter
	int x;//begin position
	int G_Value[1000];
	int G_Sum[1000] = {0};
	int G_Next[1000];

int main(){

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	fscanf(fp, "%d", &T);
	for(i = 1; i <= T; ++i){

		fscanf(fp, "%d%d%d", &R, &K, &N);
		for(j = 0; j < N; ++j)
			fscanf(fp, "%d", &G_Value[j]);

		for(j = 0; j < N; ++j){
			sum = G_Value[j];
			x = j;
			if(x == N-1)
				x = 0;
			else
				++x;
			sum += G_Value[x];
			while(sum <= K && x != j){
				if(x == N-1)
					x = 0;
				else
					++x;
				sum += G_Value[x];
			}
			sum -= G_Value[x];
			G_Sum[j] = sum;
			G_Next[j] = x;

		}

		x = 0;
		sum = 0;
		for(j = 0; j < R; ++j){
				sum += G_Sum[x];
				x = G_Next[x];
		}

		fprintf(ofp, "Case #%d: %d\n", i, sum);
	}

	return 0;
}