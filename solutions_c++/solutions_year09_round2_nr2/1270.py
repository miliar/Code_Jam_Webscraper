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

FILE *fin=fopen("B-small-attempt0.in","r");
FILE *fout=fopen("B-small-attempt0.out","w");

#define MAXN 10011

int f[10],_d[20],d[20],x[20],l,flag,comp;

void dg(int p)
{
	int i;

	if (p==-1)
	{
		if (flag==1)
		{
			comp=1;
			for (i=l-1; i>=0; i--)
				fprintf(fout,"%d",x[i]);
			fprintf(fout,"\n");
		}
		if (flag==0)
		{
			flag=1;
		}
		return;
	}

	for (i=d[p]; i<10; i++)
		if (f[i]>0)
		{
			f[i]--;
			x[p]=i;
			dg(p-1);
			f[i]++;
			if (comp)
				return;
		}
	d[p]=0;
}

void search()
{
	int i;
	int64 temp;

	fscanf(fin,"%I64d",&temp);
	l=0;
	for (i=0; i<10; i++)
		f[i]=0;
	while (temp>0)
	{
		d[l]=temp%10;
		_d[l]=d[l];
		f[d[l]]++;
		temp/=10;
		l++;
	}
	flag=0;
	comp=0;
	dg(l-1);
	if (comp==0)
	{
		sort(_d+0,_d+l);
		for (i=0; i<l; i++)
			if (_d[i]>0)
				break;
		fprintf(fout,"%d",_d[i]);
		_d[i]=0;
		for (i=0; i<l; i++)
			fprintf(fout,"%d",_d[i]);
		fprintf(fout,"\n");
	}
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		search();
	}
	return 0;
}
