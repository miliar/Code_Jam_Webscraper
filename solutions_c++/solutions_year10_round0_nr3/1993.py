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

//FILE *fin=fopen("C-sample.in","r");
//FILE *fout=fopen("C-sample.out","w");

//FILE *fin=fopen("C-small-attempt1.in","r");
//FILE *fout=fopen("C-small-attempt1.out","w");

FILE *fin=fopen("C-large.in","r");
FILE *fout=fopen("C-large.out","w");

#define MAXN 10011

int64 R, C;
int n;
int64 g[MAXN];

int p[MAXN];
int f[MAXN];
int64 l[MAXN];

void init()
{
	fscanf(fin,"%I64d %I64d %d",&R,&C,&n);
	for (int i=0; i<n; i++)
		fscanf(fin,"%I64d",g+i);

	for (int i=0; i<n; i++)
	{
		int64 temp=0;
		int j=i;
		while (temp+g[j]<=C)
		{
			temp+=g[j];
			j++;
			j%=n;
			if (j==i)
				break;
		}
		p[i]=j;
		l[i]=temp;
	}
}

void search()
{
	int i,s,period=0;
	int64 periodl=0;
	int64 ret=0;

	for (int j=0; j<n; j++)
		f[j]=0;
	i=0;
	while (f[i]==0)
	{
		period++;
		periodl+=l[i];
		f[i]=1;
		i=p[i];
	}
	s=i;

	i=0;
	while (i!=s)
	{
		period--;
		periodl-=l[i];
		i=p[i];
	}

	i=0;
	while (i!=s)
	{
		ret+=l[i];
		i=p[i];
		R--;
		if (R==0)
			break;
	}

	ret+=(R/period)*periodl;
	i=s;
	for (int j=0; j<(R%period); j++)
	{
		ret+=l[i];
		i=p[i];
	}

	fprintf(fout,"%I64d\n",ret);
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		init();
		search();
	}
	return 0;
}
