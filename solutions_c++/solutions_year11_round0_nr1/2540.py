// code.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS 1
#include "stdafx.h"

#include <math.h>


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi,*fo;
	int t,ti;

	int c[100],b[100];	
	int n,i,but,r,max;
	char col[10];
	int p[2],v[2];


	fi=fopen("A.in","r");
	fo=fopen("A.out","w");

	fscanf(fi,"%d",&t);


	for (ti=0;ti<t;ti++)
	{
		fscanf(fi,"%d",&n);
		for (i=0;i<n;i++)
		{
			fscanf(fi,"%s %d",col,&but);
			if (col[0]=='O') c[i]=0; else c[i]=1;
			b[i]=but;
		}
		p[0]=p[1]=1;
		v[0]=v[1]=0;
		for (i=0;i<n;i++)
		{
			r=c[i];
			v[r]+=abs(p[r]-b[i])+1;
			p[r]=b[i];
			if (v[1-r]>=v[r]) v[r]=v[1-r]+1;
		}
		max=v[0];
		if (v[1]>max) max=v[1];
		fprintf(fo,"Case #%d: %d\n",ti+1,max);

	}
	fclose(fi);
	fclose(fo);
	return 0;
}

