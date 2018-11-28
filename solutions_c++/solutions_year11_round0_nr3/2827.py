#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include <iostream>
using namespace std;
int i, j, k, e, n, t, s;
int value[1000];
int binary[1000][20];
int sum[20];
void convert()
{
	int m, a, tmp;
	for (m=0; m<n; m++) for (a=0; a<20; a++) binary[m][a]=0;
	for (m=0; m<n; m++)
	{
		a=0;
		tmp=value[m];
		while (tmp)
		{
			binary[m][a]=tmp%2;
			tmp=tmp/2;
			a++;
		}
	}
}
int getresult()
{
	int a, all=0, minimum=1000001;
	for (a=0; a<n; a++)
	{
		all+=value[a];
		if (value[a]<minimum) minimum=value[a];
	}
	return all-minimum;
}
void main()
{
	FILE *rFile=fopen("D:\\C-large.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\C-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=0; i<t; i++)
	{
		fscanf(rFile, "%d", &n);
		for (j=0; j<n; j++) fscanf(rFile, "%d", &value[j]);
		convert();
		for (j=0; j<20; j++) sum[j]=binary[0][j];
		for (j=1; j<n; j++)
			for (k=0; k<20; k++)
			{
				sum[k]=(sum[k]+binary[j][k])%2;
			}
		s=0;
		for (j=0; j<20; j++) s+=sum[j];
		if (s)
		{
			printf("NO!\n");
			fprintf(wFile, "Case #%d: NO\n", i+1);
			continue;
		}
		printf("%d\n", getresult());
		fprintf(wFile, "Case #%d: %d\n", i+1, getresult());
	}//for i=0
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}