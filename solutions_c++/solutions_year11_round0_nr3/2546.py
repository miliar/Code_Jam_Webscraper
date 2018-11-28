// code.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS 1
#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi,*fo;
	int t,ti,n,i;
	long sum,min,xsum,c;

	fi=fopen("A.in","r");
	fo=fopen("A.out","w");

	fscanf(fi,"%d",&t);


	for (ti=0;ti<t;ti++)
	{
		sum=0;
		min=2000000;
		xsum=0;
		fscanf(fi,"%d",&n);
		for (i=0;i<n;i++)
		{
			fscanf(fi,"%ld",&c);
			sum+=c;
			xsum=xsum ^ c;
			if (c<min) min=c;
		}
		if (xsum==0) fprintf(fo,"Case #%d: %ld\n",ti+1,sum-min);
		else fprintf(fo,"Case #%d: NO\n",ti+1);

	}



	fclose(fi);
	fclose(fo);
	return 0;
}

