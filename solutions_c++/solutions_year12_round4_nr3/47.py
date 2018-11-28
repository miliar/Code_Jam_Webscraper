#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const int MAXN=2012;
int T;
int n,x[MAXN],h[MAXN],f[MAXN],w[MAXN];
int g[MAXN][MAXN];
int maxh;

void init()
{
	scanf("%d",&n);
	for (int i=1;i<n;i++) scanf("%d",&x[i]);
}

bool check()
{
	for (int i=1;i<n-1;i++)
		for (int j=i+1;j<x[i];j++)
			if (x[i]<x[j]) return false;
	return true;
}

void dfs(int v,int value)
{
	w[v]=value;
	for (int i=1;i<=g[v][0];i++)
		dfs(g[v][i],value+i-1);
}

void work()
{
	if (!check())
	{
		printf(" Impossible\n");
		return;
	}
	
	maxh=10000000;
	memset(g,0,sizeof(g));
	for (int i=1;i<n;i=x[i])
	{
		for (int j=i;j<=x[i]-1;j++)
		{
			int son=j,father=x[j];
			g[father][++g[father][0]]=son;
		}
		dfs(x[i],0);
		h[x[i]]=maxh;
		for (int j=x[i]-1;j>=i;j--)
			h[j]=h[x[j]]-(x[j]-j)*w[j];
	}	
	for (int i=1;i<=n;i++)
		printf(" %d",h[i]);
	printf("\n");
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		printf("Case #%d:",t);
		work();
	}
	return 0;
}
