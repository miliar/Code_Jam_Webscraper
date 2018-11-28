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

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

#define MAXN 10011

int n;
double p[MAXN];
char f[MAXN][100];
int c1[MAXN],c2[MAXN];

int m,mf;
char name[101];
char ft[101][101];

void read(int k)
{
	char c;

	do
		fscanf(fin,"%c",&c);
	while (c!='(');
	
	fscanf(fin,"%lf",&p[k]);

	do
	{
		fscanf(fin,"%c",&c);
		if (c>='a'&&c<='z')
			break;
	}
	while (c!=')');

	if (c>='a'&&c<='z')
	{
		while (c>='a'&&c<='z')
		{
			f[k][strlen(f[k])]=c;
			fscanf(fin,"%c",&c);
		}
		c1[k]=n;
		n++;
		c2[k]=n;
		n++;
		read(c1[k]);
		read(c2[k]);
		do
			fscanf(fin,"%c",&c);
		while (c!=')');
	}
}

void init()
{
	int i,j;

	n=0;
	for (i=0; i<MAXN; i++)
	{
		c1[i]=-1;
		c2[i]=-1;
		for (j=0; j<100; j++)
			f[i][j]=0;
	}
	fscanf(fin,"%d\n",&i);
	n=1;
	read(0);
}

double prob(int k)
{
	int i;

	if (c1[k]==-1&&c2[k]==-1)
		return p[k];
	else
	{
		for (i=0; i<mf; i++)
			if (strcmp(ft[i],f[k])==0)
				return p[k]*prob(c1[k]);
		return p[k]*prob(c2[k]);
	}
}

void search()
{
	int i,j;

	fscanf(fin,"%d",&m);
	for (i=0; i<m; i++)
	{
		fscanf(fin,"%s %d",name,&mf);
		for (j=0; j<mf; j++)
			fscanf(fin,"%s",ft[j]);
		fprintf(fout,"%0.7lf\n",prob(0));
	}
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d:\n",i+1);
		init();
		search();
	}
	return 0;
}
