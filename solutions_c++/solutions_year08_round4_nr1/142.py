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
#define int64 long long
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

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

#define MAXN 10011
#define NA 1000001

int n,v,g[MAXN],c[MAXN],l[MAXN],f[MAXN][2];

void init()
{
	int i;

	fscanf(fin,"%d %d",&n,&v);
	for (i=0; i<(n-1)/2; i++)
	{
		fscanf(fin,"%d %d",g+i,c+i);
		l[i]=0;
	}
	for (i=(n-1)/2; i<n; i++)
	{
		fscanf(fin,"%d",g+i);
		c[i]=0;
		l[i]=1;
	}
}

void search()
{
	int i,j,k,ll,rr,ii;

	for (i=0; i<n; i++)
	{
		f[i][0]=NA;
		f[i][1]=NA;
	}

	for (i=n-1; i>=0; i--)
	{
		if (l[i]==1)
		{
			f[i][g[i]]=0;
		}
		else
		{
			ll=i*2+1;
			rr=i*2+2;
			if (c[i]==1)
			{
				for (j=0; j<2; j++)
					for (k=0; k<2; k++)
						if (f[ll][j]!=NA&&f[rr][k]!=NA)
						{
							if (g[i]==1)
								ii=(j&k);
							else
								ii=(j|k);
							f[i][ii]=min(f[i][ii],f[ll][j]+f[rr][k]);
							if (g[i]==1)
								ii=(j|k);
							else
								ii=(j&k);
							f[i][ii]=min(f[i][ii],f[ll][j]+f[rr][k]+1);
						}
			}
			else
			{
				for (j=0; j<2; j++)
					for (k=0; k<2; k++)
						if (f[ll][j]!=NA&&f[rr][k]!=NA)
						{
							if (g[i]==1)
								ii=(j&k);
							else
								ii=(j|k);
							f[i][ii]=min(f[i][ii],f[ll][j]+f[rr][k]);
						}
			}
		}
	}

	if (f[0][v]==NA)
		fprintf(fout,"IMPOSSIBLE\n");
	else
		fprintf(fout,"%d\n",f[0][v]);
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
