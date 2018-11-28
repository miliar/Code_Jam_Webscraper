#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
int i, j, k, e, n, t, r, c, count, x, y;
char pic[50][51];
void getIndex()
{
	int l_count=0;
	x=0; y=0;
	while (pic[x][y]!='#')
	{
		l_count++;
		x=l_count/c;
		y=l_count%c;
	}
}
void main()
{
	FILE *rFile=fopen("D:\\A-large (2).in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\R1C-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=1; i<=t; i++)
	{
		fscanf(rFile, "%d", &r); fscanf(rFile, "%d", &c);
		for (j=0; j<r; j++) fscanf(rFile, "%s", pic[j]);
		fprintf(wFile, "Case #%d:\n", i);
		count=0;
		for (j=0; j<r; j++)
			for (k=0; k<c; k++)
				if (pic[j][k]=='#') count++;
		if (count%4)
		{
			fprintf(wFile, "Impossible\n");
			continue;
		}
		for (j=0; j<count/4; j++)
		{
			getIndex();
			pic[x][y]='/';
			if (x<r-1) pic[x+1][y]='\\';
			if (y<c-1) pic[x][y+1]='\\';
			if (x<r-1&&y<c-1) pic[x+1][y+1]='/';
		}
		count=0;
		for (j=0; j<r; j++)
			for (k=0; k<c; k++)
				if (pic[j][k]=='#') count++;
		if (count==0)
		{
			for (j=0; j<r; j++) fprintf(wFile, "%s\n", pic[j]);
		}
		else fprintf(wFile, "Impossible\n");
	}
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}
