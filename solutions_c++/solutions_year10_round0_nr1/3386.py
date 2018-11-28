#include <stdio.h>
#include <memory.h>
#include <string.h>

int main()
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	unsigned int T,N,K,Out,i;

	fscanf(fp, "%d", &T);
	for(i=1;i<=T;i++) 
	{
		fscanf(fp, "%d%d", &N,&K);
		unsigned int j=1;

		j=j<<N;
		j=j-1;
		K=K<<(32-N);
		K=K>>(32-N);
		Out=j^K;
		if(Out) fprintf(ofp, "Case #%d: %s\n", i,"OFF");
		else fprintf(ofp,"Case #%d: %s\n",i,"ON");
	}
	return 0;
}
