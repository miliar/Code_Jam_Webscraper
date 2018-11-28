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

#define uint64 unsigned long long
#define _1 ((uint64)1)
#define int64 long long
/*
#define uint64 unsigned __int64
#define _1 ((uint64)1)
#define int64 __int64
*/

const int64 INF64=(_1<<63)-1;
const int INF32=(_1<<31)-1;

using namespace std;

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

#define MAXL 100
#define MAXD 10001
#define MAXS 10001

int L,D;
char dict[MAXD][MAXL];
char patt[MAXS];
int f[MAXD],g[MAXD];

int search()
{
	int i,j,k,pr,ret=0;

	fscanf(fin,"%s",patt);
	for (i=0; i<D; i++)
		f[i]=1;
	for (i=0, pr=0; i<L; i++)
	{
		j=pr;
		if (pr>=strlen(patt))
			return 0;

		if (patt[pr]=='(')
			while (patt[pr]!=')')
			{
				pr++;
				if (pr>=strlen(patt))
					return 0;
			}
		pr++;

		for (k=0; k<D; k++)
			g[k]=0;
		for (; j<pr; j++)
		{
			for (k=0; k<D; k++)
				if (dict[k][i]==patt[j])
					g[k]=1;
		}
		for (k=0; k<D; k++)
			if (g[k]==0)
				f[k]=0;
	}
	for (i=0; i<D; i++)
		ret+=f[i];
	return ret;
}

int main()
{
	int testdata,i;

	fscanf(fin,"%d %d %d",&L,&D,&testdata);
	for (i=0; i<D; i++)
		fscanf(fin,"%s",dict[i]);
	for (i=0; i<testdata; i++)
	{
		fprintf(fout,"Case #%d: %d\n",i+1,search());
	}
	return 0;
}
