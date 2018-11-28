#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)<(b)?(b):(a))
#define INF INF32
#define NA (-1)

#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

FILE *fin=fopen("C-large.in","r");
FILE *fout=fopen("C-large.out","w");

#define MAXL 1001

char p[MAXL];
char *q="welcome to code jam";

int n;
int m=19;
int sum[MAXL][19];

void search()
{
	int i,j,ret;

	fgets(p,MAXL,fin);
	n=(int)strlen(p);

	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
			sum[i][j]=0;

	for (i=0; i<n; i++)
	{
		if (p[i]==q[0])
		{
			if (i==0)
				sum[i][0]=1;
			else
				sum[i][0]=sum[i-1][0]+1;
			sum[i][0]%=10000;
		}
		else
		{
			if (i>0)
				sum[i][0]=sum[i-1][0];
		}
		for (j=1; j<m; j++)
			if (i>0)
			{
				sum[i][j]=sum[i-1][j];
				if (p[i]==q[j])
					sum[i][j]+=sum[i-1][j-1];
				sum[i][j]%=10000;
			}
	}

	ret=sum[n-1][m-1];
	if (ret<10)
		fprintf(fout,"000%d\n",ret);
	else if (ret<100)
		fprintf(fout,"00%d\n",ret);
	else if (ret<1000)
		fprintf(fout,"0%d\n",ret);
	else
		fprintf(fout,"%d\n",ret);
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d\n",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		search();
	}
	return 0;
}
