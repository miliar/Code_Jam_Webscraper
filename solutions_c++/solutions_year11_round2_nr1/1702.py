#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
int i, j, k, r, e, t, n, a, b, count;
double sum;
char table[100][101];
double wp[100], owp[100], oowp[100], rpi[100], m_wp[100][100];
void main()
{
	FILE *rFile=fopen("D:\\A-large (1).in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\R1B-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=1; i<=t; i++)
	{
		fscanf(rFile, "%d", &n);
		for (j=0; j<n; j++) fscanf(rFile, "%s", table[j]);
		for (j=0; j<n; j++)
		{
			for (k=0; k<n; k++)
			{
				if (table[j][k]=='1') a++;
				if (table[j][k]=='1'||table[j][k]=='0') b++;
			}
			wp[j]=(double)a/(double)b;
			a=0; b=0;
		}
		for (j=0; j<n; j++)
		{
			for (k=0; k<n; k++)
			{
				if (k==j) continue;
				for (r=0; r<n; r++)
				{
					if (r==k) continue;
					if (table[j][r]=='1') a++;
					if (table[j][r]=='1'||table[j][r]=='0') b++;
				}
				m_wp[j][k]=(double)a/(double)b;
				a=0; b=0;
			}
		}
		for (j=0; j<n; j++)
		{
			sum=0; count=0;
			for (k=0; k<n; k++)
			{
				if (table[j][k]=='1'||table[j][k]=='0')
				{
					sum+=m_wp[k][j];
					count++;
				}
			}
			owp[j]=sum/(double)count;
		}
		for (j=0; j<n; j++)
		{
			sum=0; count=0;
			for (k=0; k<n; k++)
			{
				if (table[j][k]=='1'||table[j][k]=='0')
				{
					sum+=owp[k];
					count++;
				}
			}
			oowp[j]=sum/(double)count;
		}
		for (j=0; j<n; j++)
		{
			rpi[j]=0.25*wp[j] + 0.50*owp[j] + 0.25*oowp[j];
		}
		fprintf(wFile, "Case #%d:\n", i);
		for (j=0; j<n; j++)
			fprintf(wFile, "%lf\n", rpi[j]);
	}
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}