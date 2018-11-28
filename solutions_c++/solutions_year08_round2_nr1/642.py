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
	long long N_, n, A, B, C, D, x0, y0, M, X, Y,res;
	long double v1, v2;
	FILE *in, *out;
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	
	
	fscanf(in,"%lld\n",&N_);
	long long mas[101][2];
	for(int i=0; i<N_; i++)
	{
		res=0;
		fscanf(in,"%lld %lld %lld %lld %lld %lld %lld %lld\n",&n, &A, &B, &C, &D, &x0, &y0, &M);
		X = x0; Y = y0;
		mas[0][0]=X; mas[0][1]=Y;
		for(int j=1; j<n; j++)
		{
			X=(A*X+B)%M;
			mas[j][0]=X;
			Y=(C*Y+D)%M;
			mas[j][1]=Y;
		}
		for(int k1=0;k1<n-2;k1++)
			for(int k2=k1+1;k2<n-1;k2++)
				for(int k3=k2+1;k3<n;k3++)
				{
					v1=(mas[k1][0]+mas[k2][0]+mas[k3][0]);
					v1=v1/3;
					v2=(mas[k1][1]+mas[k2][1]+mas[k3][1]);
					v2=v2/3;
					if(v1-(int)v1<e && v2-(int)v2<e) res++;
				}
				fprintf(out,"Case #%d: %lld\n",i+1,res);
	}
	
	fclose(in);
	fclose(out);
	return 0;
}

int compare( const void *arg1, const void *arg2 )
{
	return *(int*)arg1 - *(int*)arg2;
}
