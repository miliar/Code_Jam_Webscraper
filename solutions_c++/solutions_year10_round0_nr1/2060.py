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

#define MAXN 10011

int n,k;

void init()
{
	fscanf(fin,"%d %d",&n,&k);
}

void search()
{
	n=(1<<n)-1;
	if ((k&n)==n)
		fprintf(fout,"ON\n");
	else
		fprintf(fout,"OFF\n");
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
