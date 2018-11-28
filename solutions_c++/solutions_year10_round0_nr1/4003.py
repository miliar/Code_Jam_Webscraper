// gcjay.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* iFile;
	FILE* oFile;
	iFile = fopen("A-large.in", "rb");
	oFile = fopen("out.txt", "w");
	if(iFile)
	{
		int len = 0;
		int aa = 0;
		fscanf(iFile, "%d", &len);
		for(aa; aa < len; aa++)
		{
			int N = 0;
			int K = 0;
			fscanf(iFile, "%d", &N);
			fscanf(iFile, "%d", &K);
			K++;
			int bb = 0;
			int T = 1;
			for(bb = 0; bb < N; bb++)
				T = 2 * T;
			if(K%T==0)
				fprintf(oFile, "Case #%d: ON\n", aa+1);
			else
				fprintf(oFile, "Case #%d: OFF\n", aa+1);
		}	
		fclose(iFile);
		fclose(oFile);
	}
	else
		return 1;
	return 0;
}

