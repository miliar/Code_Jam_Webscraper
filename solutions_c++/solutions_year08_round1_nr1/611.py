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
#define MinNum(a,b) ((a)>(b)?(b):(a))
#define MaxNum(a,b) ((a)<(b)?(b):(a))
#define INF INF32
#define NA (-1)

#define uint64 unsigned long long
#define _1 ((uint64)1)
#define int64 __int64
/*
#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64
*/

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

/*
class Temp{
public:
	void Ret()
	{
	}
};
*/

FILE *fin=fopen("in.in","r");
FILE *fout=fopen("out.out","w");

#define MAXN 1001

int n;
int64 x[MAXN];
int64 y[MAXN];

void init()
{
	int i,j,temp;
	fscanf(fin,"%d",&n);
	for (i=0; i<n; i++)
	{
		fscanf(fin,"%d",&temp);
		x[i]=temp;
	}
	for (i=0; i<n; i++)
	{
		fscanf(fin,"%d",&temp);
		y[i]=temp;
	}
	for (i=0; i<n; i++)
		for (j=i+1; j<n; j++)
			if (x[i]>x[j])
			{
				temp=x[i];
				x[i]=x[j];
				x[j]=temp;
			}
	for (i=0; i<n; i++)
		for (j=i+1; j<n; j++)
			if (y[i]>y[j])
			{
				temp=y[i];
				y[i]=y[j];
				y[j]=temp;
			}
}

void search()
{
	int64 ans;
	int i;

	ans=0;
	for (i=0; i<n; i++)
		ans+=x[i]*y[n-i-1];
	fprintf(fout,"%I64d\n",ans);
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
