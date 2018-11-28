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

FILE *fin=fopen("B-large.in","r");
FILE *fout=fopen("B-large.out","w");

#define MAXN 101

int n,m,p[MAXN][MAXN],f[MAXN][MAXN];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int tot;

void init()
{
	int i,j;

	fscanf(fin,"%d %d",&n,&m);
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
		{
			fscanf(fin,"%d",&p[i][j]);
			f[i][j]=-1;
		}
}

int next(int x,int y)
{
	int xx,yy,i,md=INF32,ret;

	for (i=0; i<4; i++)
	{
		xx=x+dx[i];
		yy=y+dy[i];
		if (xx>=0&&xx<n&&yy>=0&&yy<m)
		{
			if (p[xx][yy]<md)
			{
				md=p[xx][yy];
				ret=i;
			}
		}
	}
	if (md>=p[x][y])
		return -1;
	else
		return ret;
}

int dg(int x,int y)
{
	if (f[x][y]==-1)
	{
		int d=next(x,y);
		if (d==-1)
		{
			f[x][y]=tot;
			tot++;
		}
		else
		{
			int c=dg(x+dx[d],y+dy[d]);
			f[x][y]=c;
		}
		return f[x][y];
	}
	else
		return f[x][y];
}

void search()
{
	int i,j;
	
	tot=0;
	for (i=0; i<n; i++)
		for (j=0; j<m; j++)
			if (f[i][j]==-1)
				dg(i,j);
	for (i=0; i<n; i++)
	{
		for (j=0; j<m; j++)
			fprintf(fout,"%c ",f[i][j]+'a');
		fprintf(fout,"\n");
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
