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

//FILE *fin=fopen("A-sample.in","r");
//FILE *fout=fopen("A-sample.out","w");

//FILE *fin=fopen("A-small-attempt0.in","r");
//FILE *fout=fopen("A-small-attempt0.out","w");

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

#define MAXN 101

int n,p[MAXN];

void init()
{
	int i,j;
	char x[MAXN];

	fscanf(fin,"%d\n",&n);
	for (i=0; i<n; i++)
	{
		fscanf(fin,"%s",x);
		p[i]=0;
		for (j=0; j<n; j++)
			if (x[j]=='1')
				p[i]=j;
	}
}

void swap(int &a,int &b)
{
	int c=a;
	a=b;
	b=c;
}

void search()
{
	int i,j,ret=0;

	for (i=0; i<n; i++)
		if (p[i]>i)
		{
			for (j=i+1; j<n; j++)
				if (p[j]<=i)
					break;
			do
			{
				swap(p[j],p[j-1]);
				j--;
				ret++;
			}
			while(j>i);
		}
	fprintf(fout,"%d\n",ret);
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
