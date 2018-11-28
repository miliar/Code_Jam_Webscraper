// try1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

int Snap(_int64 N, _int64 K)
{
	if( N-1 > K)
		return 0;
	K = K % (int)(pow((double)2,(double)N));
	if (pow((double)2,(double)N) - 1> K)
		return 0;
	else 
		return 1;
}


int main(int argc, char* argv[])
{
	int N, K, nInputs;
	FILE *f=fopen(argv[1],"r");
	FILE *fout= fopen(argv[2],"wt");
	fscanf(f,"%d", &nInputs);
	int nLine=0;
	while(!feof(f) && nLine < nInputs)
	{
		fscanf(f,"%d %d",&N, &K);
		fprintf(fout,"Case #%d: %s\n", nLine+1,Snap(N, K)?"ON":"OFF");
		nLine++;
	}
	fclose(f);
	fclose(fout);
	return 0;
}

