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

#define MAXN 101
#define MAXM 1001
#define MAXL 1001

FILE *fin=fopen("inp.txt","r");
FILE *fout=fopen("out.txt","w");

int n,m;
char name[MAXN][MAXL];
int num[MAXM];
int ret[MAXM][MAXN];

void eqstr(char *s)
{
	char c;

	do
	{
		c=s[strlen(s)-1];
		if (c>='A'&&c<='Z')
			return;
		if (c>='a'&&c<='z')
			return;
		if (c>='0'&&c<='9')
			return;
		if (c==' ')
			return;
		s[strlen(s)-1]=0;
	}
	while (strlen(s)>0);
}

void init()
{
	int i,j;
	char temp[MAXL];

	fscanf(fin,"%d\n",&n);
	for (i=0; i<n; i++)
	{
		fgets(name[i],MAXL,fin);
		eqstr(name[i]);
	}
	fscanf(fin,"%d\n",&m);
	for (i=0; i<m; i++)
	{
		fgets(temp,MAXL,fin);
		eqstr(temp);
		for (j=0; j<n; j++)
			if (strcmp(temp,name[j])==0)
			{
				num[i]=j;
				break;
			}
	}
}

void search()
{
	int i,j,k,ans;

	if (m==0)
	{
		fprintf(fout,"0\n");
		return;
	}

	for (i=0; i<m; i++)
		for (j=0; j<n; j++)
			ret[i][j]=INF;
	for (j=0; j<n; j++)
		if (num[0]!=j)
			ret[0][j]=0;
	for (i=1; i<m; i++)
		for (j=0; j<n; j++)
			if (num[i]!=j)
			{
				if (ret[i-1][j]<INF)
					ret[i][j]=MinNum(ret[i-1][j],ret[i][j]);
				for (k=0; k<n; k++)
					if (ret[i-1][k]<INF)
						if (k!=j)
							ret[i][j]=MinNum(ret[i-1][k]+1,ret[i][j]);
			}
	ans=INF;
	for (j=0; j<n; j++)
		ans=min(ans,ret[m-1][j]);
	fprintf(fout,"%d\n",ans);
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
