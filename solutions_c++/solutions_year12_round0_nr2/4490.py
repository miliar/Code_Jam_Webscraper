// Codejam2012.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpi;
	FILE *fpo;
	int nT, nN, nS, np;
	int nti[100];
	int m = 0;
	int ret = 0;
	int avg;

	int i,j;

	fpi = fopen("B-large.in","r");
	if (!fpi) exit(0);
	fpo = fopen("B-large.out","w");
	if (!fpo) exit(0);

	//fpi = fopen("test.txt","r");
	//if (!fpi) exit(0);
	//fpo = fopen("testout.txt","w");
	//if (!fpo) exit(0);

	fscanf(fpi, "%d\n", &nT);

	i = 0;
	while (i < nT)
	{
		fscanf(fpi, "%d %d %d", &nN, &nS, &np);
		ret = 0;
		for (j = 0; j<nN; j++)
		{
			fscanf(fpi, "%d", &nti[j]);
			m = nti[j] % 3;
			switch(m)
			{
			case 0:
				avg = nti[j] / 3;
				if (avg >= np)
				{
					ret = ret + 1;
				}
				else if ((avg+1 >= np) && (nS>0) && (avg >= 1))
				{
					ret = ret + 1;
					nS = nS - 1;
				}
				break;
			case 1:
				avg = (nti[j]+2) / 3;
				if (avg >= np)
				{
					ret = ret + 1;
				}
				break;
			case 2:
				avg = (nti[j]+1) / 3;
				if (avg >= np)
				{
					ret = ret + 1;
				}
				else if ((avg+1 >= np) && (nS>0))
				{
					ret = ret + 1;
					nS = nS - 1;
				}
				break;
			}
		}
		fprintf(fpo, "Case #%d: ", i+1);
		fprintf(fpo, "%d\n", ret);
		i = i+1;
	}

	fclose(fpi);
	fclose(fpo);	
	return 0;
}

