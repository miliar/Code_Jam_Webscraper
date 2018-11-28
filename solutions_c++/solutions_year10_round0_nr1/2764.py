//snapper

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <math.h>

int _tmain(int argc, _TCHAR* argv[])
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T,N,K,i;
	char ans[10];
		
	fscanf(fp,"%d",&T);

	for(i=0;i<T;i++)
	{
		fscanf(fp,"%d%d",&N,&K);

		if((K+1)%(int)(pow((double)2,N))==0)
			strcpy(ans,"ON");
		else
			strcpy(ans,"OFF");
		fprintf(ofp,"Case #%d: %s\n", i+1, ans);
	}
	return 0;
}

