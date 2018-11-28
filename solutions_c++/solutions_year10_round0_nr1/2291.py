// snapper.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"

bool snap(unsigned int n, unsigned int k)
{
	unsigned int max = 1<<n;
	unsigned int remain = k % max;
	printf("%u,%u: %u\n",max,k,remain);
	return (remain == (max-1));
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fin = fopen("a.in","r");
	FILE* fout = fopen("a.out","w");
	unsigned int line, n, k;
	fscanf(fin,"%u\n",&line);
	printf("%u\n",line);
	for(unsigned int i = 0; i < line; i++)
	{
		fscanf(fin,"%u %u\n",&n,&k);
		bool light = snap(n,k);
		if(light)
		{
			fprintf(fout,"Case #%u: ON\n",i+1);
		}else{
			fprintf(fout,"Case #%u: OFF\n",i+1);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

