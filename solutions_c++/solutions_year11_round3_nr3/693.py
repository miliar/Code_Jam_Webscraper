#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
int i, j, k, e, n, t, r, c, count, x, y, low, high, flag;
int a[100];
int gotit()
{
	int ii, m_flag=1;
	for (ii=0; ii<n; ii++)
	{
		if (j%a[ii]&&a[ii]%j)
		{
			m_flag=0;
			break;
		}
	}
	return m_flag;
}
void main()
{
	FILE *rFile=fopen("D:\\C-small-attempt0.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\R1C-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=1; i<=t; i++)
	{
		fscanf(rFile, "%d", &n); fscanf(rFile, "%d", &low); fscanf(rFile, "%d", &high);
		for (j=0; j<n; j++) fscanf(rFile, "%d", &a[j]);
		flag=0;
		for (j=low; j<=high; j++)
			if (gotit())
			{
				flag=1;
				break;
			}
		fprintf(wFile, "Case #%d: ", i);
		if (flag) fprintf(wFile, "%d\n", j);
		else fprintf(wFile, "NO\n");
	}
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}
