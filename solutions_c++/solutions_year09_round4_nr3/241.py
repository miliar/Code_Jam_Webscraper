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

//FILE *fin=fopen("C-small-attempt0.in","r");
//FILE *fout=fopen("C-small-attempt0.out","w");

FILE *fin=fopen("C-large.in","r");
FILE *fout=fopen("C-large.out","w");

#define MAXN 101
#define MAXM 101

int n,m;
int r[MAXN][MAXM];
int p[MAXN][MAXN];
int cx[MAXN],yx[MAXN],fx[MAXN];

int path(int pp)
{
	int i;

	if (fx[pp]==1) return 0;

	fx[pp]=1;
	for (i=0; i<n; i++)
		if (p[pp][i])
			if (yx[i]==-1||path(yx[i]))
			{
				yx[i]=pp; cx[pp]=1; return 1;
			}
	return 0;
}

void search()
{
	int ans=0;
	int i;
	
	memset(cx,0,sizeof(cx)); memset(yx,-1,sizeof(yx));
	for (i=0; i<n; i++)
	if (cx[i]==0)
	{
		memset(fx,0,sizeof(fx)); if (path(i)) ans++;
	}
	fprintf(fout,"%d\n",n-ans);
}


void init()
{
	int i,j,k;
	fscanf(fin,"%d %d",&n,&m);
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
			fscanf(fin,"%d",&r[i][j]);

	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
		{
			p[i][j]=0;
			for (k=0; k<m; k++)
				if (r[i][k]>=r[j][k])
					break;
			if (k==m)
				p[i][j]=1;
		}

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
