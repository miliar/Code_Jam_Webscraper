// code.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS 1
#include "stdafx.h"

#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 100



int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi,*fo;
	int ttt,ti;

	int n,i,j;
	long double rpi[MAXN],wp[MAXN],owp[MAXN][MAXN],oowp[MAXN],owp2[MAXN];
	int g[MAXN],w[MAXN];
	int r[MAXN][MAXN];

	char red[MAXN+1];


	fi=fopen("Al.in","r");
	fo=fopen("A.out","w");

	fscanf(fi,"%d",&ttt);
	for (ti=0;ti<ttt;ti++)
	{
		fscanf(fi,"%d",&n);
		for (i=0;i<n;i++)
		{
			g[i]=0;
			w[i]=0;
			fscanf(fi,"%s",red);
			for (j=0;j<n;j++) 
			{	
				if (red[j]=='1') { r[i][j]=1; g[i]++; w[i]++; }
				else if (red[j]=='0') { r[i][j]=0; g[i]++; }
				else { r[i][j]=-1; }		
			}
			wp[i]=((long double) w[i])/g[i];
			for (j=0;j<n;j++)
			{
				if (r[i][j]==-1) owp[i][j]=wp[i];
				else owp[i][j]=((long double) w[i]-r[i][j])/(g[i]-1);
			}
		}
		for (i=0;i<n;i++)
		{
			owp2[i]=0;
			for (j=0;j<n;j++) if (r[i][j]>-1) owp2[i]+=owp[j][i];
			owp2[i]/=g[i];
		}
		for (i=0;i<n;i++)
		{
			oowp[i]=0;
			for (j=0;j<n;j++) if (r[i][j]>-1) oowp[i]+=owp2[j];
			oowp[i]/=g[i];
			rpi[i]=0.25 * wp[i] + 0.5 * owp2[i] + 0.25 * oowp[i];
		}



		fprintf(fo,"Case #%d:\n",ti+1);
		for (i=0;i<n;i++)
		{
			fprintf(fo,"%.12lf\n",rpi[i]);
		}

	}
	fclose(fi);
	fclose(fo);
	return 0;
}

