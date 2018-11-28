// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

#define FNAME "B-large.in"
#define FOUT FNAME##".out"

void solveB()
{
	FILE *fi, *fo;
	fopen_s(&fi, FNAME, "rt");
	fopen_s(&fo, FOUT, "wt");
	int t;
	int l,p,c,lt;
	int i,j;
	fscanf_s(fi, "%d", &t);
	for (i = 1 ; i <= t ; ++i)
	{
		printf("Case #%d\n", i);
		fprintf(fo, "Case #%d: ", i);
		fscanf_s(fi, "%d %d %d", &l,&p,&c);
		lt = j = 0;
		while ((__int64)p>(__int64)c*(__int64)l)
		{
			p = (p+c-1)/c;
			++j;
		}
		while(j)
		{
			j=j/2;
 			++lt;
		}
		fprintf(fo, "%d", lt);
		fprintf(fo, "\n");
	}
	fclose(fi);
	fclose(fo);
}

int _tmain(int argc, _TCHAR* argv[])
{
	solveB();
	return 0;
}

