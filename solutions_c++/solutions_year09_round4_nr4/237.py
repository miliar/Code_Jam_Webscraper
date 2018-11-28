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

//FILE *fin=fopen("D-sample.in","r");
//FILE *fout=fopen("D-sample.out","w");

FILE *fin=fopen("D-small-attempt0.in","r");
FILE *fout=fopen("D-small-attempt0.out","w");

//FILE *fin=fopen("A-large.in","r");
//FILE *fout=fopen("A-large.out","w");

#define MAXN 10011

int n;
double x[MAXN],y[MAXN],r[MAXN];

void init()
{
	int i;

	fscanf(fin,"%d",&n);
	for (i=0; i<n; i++)
		fscanf(fin,"%lf %lf %lf",x+i,y+i,r+i);
}

double search()
{
	int i,j;
	double ret1,ret2,ret3;

	if (n==1)
		return r[0];
	if (n==2)
		return max(r[0],r[1]);
	if (n==3)
	{
		ret1=max(r[0],(sqrt((x[1]-x[2])*(x[1]-x[2])+(y[1]-y[2])*(y[1]-y[2]))+r[1]+r[2])/2);
		ret2=max(r[1],(sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]))+r[0]+r[2])/2);
		ret3=max(r[2],(sqrt((x[1]-x[0])*(x[1]-x[0])+(y[1]-y[0])*(y[1]-y[0]))+r[1]+r[0])/2);
		return min(ret1,min(ret2,ret3));
	}
	return 0;
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d",&testdata);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: ",i+1);
		init();
		fprintf(fout,"%0.6lf\n",search());
	}
	return 0;
}
