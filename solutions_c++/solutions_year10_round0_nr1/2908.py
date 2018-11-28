#include <stdio.h>
#include <math.h>
#include <string.h>


int main(){
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int tc,i=0;
	int N,K;
	fscanf(fp, "%d", &tc);
	while(i<tc)
	{i++;
	fscanf(fp, "%d %d", &N,&K);
	if ((K+1) % (int)pow(2.0,N) == 0)
			fprintf(ofp, "Case #%d: ON\n", i);
			else 
			fprintf(ofp, "Case #%d: OFF\n", i);

	}
	return 0;
	}