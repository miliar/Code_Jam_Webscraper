// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#define FNAME "A-large.in"
#define FOUT FNAME##".out"

void solveA()
{
	FILE *fi, *fo;
	int A[1000], B[1000];
	fopen_s(&fi, FNAME, "rt");
	fopen_s(&fo, FOUT, "wt");
	int t,n, inter=0;
	int i,j,k;
	fscanf_s(fi, "%d", &t);
	for (i = 1 ; i <= t ; ++i)
	{
		fprintf(fo, "Case #%d: ", i);
		fscanf_s(fi, "%d", &n);
		inter = 0;
		for (j=0;j<n;++j)
		{
			fscanf_s(fi, "%d %d", &A[j], &B[j]);
			for (k=0;k<j;++k)
			{
				if ((A[k]>A[j] && B[k]<B[j]) ||
					(A[k]<A[j] && B[k]>B[j]))
				{
					++inter;
				}
			}
		}
		fprintf(fo, "%d", inter);
		fprintf(fo, "\n");
	}
	fclose(fi);
	fclose(fo);
}

int _tmain(int argc, _TCHAR* argv[])
{
	solveA();
	return 0;
}

