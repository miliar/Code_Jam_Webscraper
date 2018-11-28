#include <stdio.h>
#include <math.h>
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
	int N; //represent the number of buttonns taht need to be pressed
	int i, j;
	int C;
	int out;
	int sum;
	int min;

	fscanf(fp,"%d", &T);
	for(i = 1; i <= T; ++i){

		out = 0;
		sum = 0;
		min = 2000000000;

		fscanf(fp, "%d", &N);
		for(j = 1; j <= N; ++j){
			fscanf(fp,"%d", &C);
			out = out ^ C;
			sum+= C;
			if(C < min) min = C;
		}

		if(out)
			fprintf(ofp,"Case #%d: NO\n", i);
		else
			fprintf(ofp,"Case #%d: %d\n", i, sum-min);
	}

	return 0;
}