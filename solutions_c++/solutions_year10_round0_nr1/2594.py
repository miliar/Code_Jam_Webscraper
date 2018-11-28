// cj1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include<math.h>
#include<stdio.h>

long power(int n)
{
	int i;
	long s=1;
	for(i=0;i<n;i++)
	{
		s=s*2;
	}
	return s;
}

int check(int n,int k)
{
	k=k+1;
	long x;
	x=power(n);
	if(k%x==0)
		return 1;
	else
		return 0;
}

void main()
{
	FILE *fp=fopen("large.in","r");
	FILE *fout=fopen("output.txt","w");
	int i,num_inp,n,k;
	fscanf(fp,"%d",&num_inp);
	for(i=0;i<num_inp;i++)
	{
		fscanf(fp,"%d",&n);
		fscanf(fp,"%d",&k);
		fprintf(fout,"Case #%d: ",i+1);
		if(check(n,k))
			fprintf(fout,"ON");
		else
			fprintf(fout,"OFF");
		fprintf(fout,"\n");
	}
}		