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

FILE *fin=fopen("D-small-attempt0.in","r");
FILE *fout=fopen("D-small-attempt0.out","w");

#define MAXN 50011
#define MAXM 16

int m,n;
char s[MAXN],t[MAXN];
int f[MAXM],u[MAXM];
int ret;

void init()
{
	fscanf(fin,"%d",&m);
	fscanf(fin,"%s",s);
	n=strlen(s);
}

void dg(int p)
{
	int i,temp;

	if (p<m)
		for (f[p]=0; f[p]<m; f[p]++)
		{
			if (u[f[p]]==0)
			{
				u[f[p]]=1;
				dg(p+1);
				u[f[p]]=0;
			}
		}
	else
	{
		temp=0;
		for (i=0; i<n; i++)
		{
			t[i]=s[(i/m)*m+f[i%m]];
			if (i>0)
				if (t[i]!=t[i-1])
					temp++;
		}
		if (temp<ret)
			ret=temp;
	}
}

void search()
{
	int i;

	for (i=0; i<m; i++)
		u[i]=0;
	ret=MAXN;
	dg(0);
	fprintf(fout,"%d\n",ret+1);
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
