// Watershed.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int inp[100][100],snk[100][100],h,w,count;

int findsnk(int i, int j)
{
	int min = inp[i][j],x = i,y = j;
	if(snk[i][j] == -1)
	{
		if(i>0 && inp[i-1][j]<min)
		{
			min = inp[i-1][j];
			x = i-1;
			y = j;
		}
		if(j>0 && inp[i][j-1]<min)
		{
			min = inp[i][j-1];
			x = i;
			y = j-1;
		}
		if(j<w-1 && inp[i][j+1]<min)
		{
			min = inp[i][j+1];
			x = i;
			y = j+1;
		}
		if(i<h-1 && inp[i+1][j]<min)
		{
			min = inp[i+1][j];
			x = i+1;
			y = j;
		}
		if(min == inp[i][j])
			snk[i][j] = ++count;
		else
			snk[i][j] = findsnk(x,y);
	}
	return snk[i][j];
}
void main()
{
	int i,j,k,t;
	FILE *fp,*ofp;
	fopen_s(&fp,"B-large.in","r");
	fopen_s(&ofp,"Output.txt","w");
	fscanf(fp,"%d\n",&t);
	for(k=0;k<t;k++)
	{
		count = 0;
		fscanf(fp,"%d%d\n",&h,&w);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				fscanf(fp,"%d",&inp[i][j]);
				snk[i][j] = -1;
			}
			fscanf(fp,"\n");
		}
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(snk[i][j] == -1)
					snk[i][j] = findsnk(i,j);
			}
		}
		fprintf(ofp,"Case #%d:\n",k+1);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
				fprintf(ofp,"%c ",snk[i][j]+96);
			fprintf(ofp,"\n");
		}
	}
}