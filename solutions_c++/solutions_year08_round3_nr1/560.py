// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int compare( const void *arg1, const void *arg2 );

int _tmain(int argc, _TCHAR* argv[])
{
	long double e = 0.000000001;
	long long N_, P, K, L;
	long long res;
	long long mas[1001];
	FILE *in, *out;
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	
	fscanf(in,"%lld\n",&N_);

	for(int i=0; i<N_; i++)
	{
		res=0;
		fscanf(in,"%lld %lld %lld\n",&P, &K, &L);
		for(int j=0; j<L; j++)
			fscanf(in,"%lld",&mas[j]);
		qsort(&mas[0],L,sizeof(long long),compare);
		for(int j=0;j<L;j++)
			res+=mas[j]*(1+(long)(j/K));
		fprintf(out,"Case #%d: %lld\n",i+1,res);
	}
	
	fclose(in);
	fclose(out);
	return 0;
}

int compare( const void *arg1, const void *arg2 )
{
	return *(long*)arg2 - *(long*)arg1;
}
