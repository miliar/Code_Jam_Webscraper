// b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin, *fout;
	fin = fopen("b.in","r");
	fout = fopen("b.out","w");
	int t;
	fscanf(fin,"%d\n",&t);
	for(int casecount = 0; casecount < t; casecount++)
	{
		int l, p, c;
		fscanf(fin,"%d %d %d\n", &l, &p, &c);
		double res = (double)p/(double)l;
		if(res <= c)
		{
			fprintf(fout,"Case #%d: %d\n",casecount+1,0);
			continue;
		}

		res = log(res);
		res = res/log((double)c);
		res = log(res) / log((double)2);
		int r = res;
		if(res - r > 0.0000001)
		{
			r+=1;
		}
		fprintf(fout,"Case #%d: %d\n",casecount+1,r);
	}
	return 0;
}

