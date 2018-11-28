#pragma warning (disable: 4786)
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;
int tr[50010],m,to[50010],tc[50010];
int dfs(int v)
{
	if (v*2+1>=m) return tr[v];
	if (to[v]) return dfs(v*2+1)&dfs(v*2+2);
	return dfs(v*2+1)|dfs(v*2+2);
}

int bw[50006][2],opy0[3][2]={{0,0},{0,1},{1,0}},
oph1[3][2]={{1,1},{1,0},{0,1}};
int min(int a,int b ) {return a<b?a:b;}
int f(int i , int j)
{
	if (i*2+1>=m) 
	{
		if (tr[i]==j) return 0;
		return -1;
	}
	if (bw[i][j]!=-1)return bw[i][j];
	int k,mi=1<<30;
	if (to[i]==1)
	{
		if (j==0)
		{
			for (k = 0 ; k < 3 ; k++)
				if (f(i*2+1,opy0[k][0])!=-1 && f(i*2+2,opy0[k][1])!=-1)
					mi = min(f(i*2+1,opy0[k][0])+f(i*2+2,opy0[k][1]),mi);
		}
		else
		{
			if (f(i*2+1,1)!=-1 && f(i*2+2,1)!=-1)
				mi = min(f(i*2+1,1)+f(i*2+2,1),mi);
		}
	}
	else
	{
		if (j == 0)
		{
			if (f(i*2+1,0)!=-1 && f(i*2+2,0)!=-1)
				mi = min(f(i*2+1,0)+f(i*2+2,0),mi);
		}
		else
		{
			for (k = 0 ; k < 3 ; k++)
				if (f(i*2+1,oph1[k][0])!=-1 && f(i*2+2,oph1[k][1])!=-1)
					mi = min(f(i*2+1,oph1[k][0])+f(i*2+2,oph1[k][1]),mi);
		}
	}
	if (tc[i]==1)
	{
		to[i] ^= 1;
		if (to[i]==1)
		{
			if (j==0)
			{
				for (k = 0 ; k < 3 ; k++)
					if (f(i*2+1,opy0[k][0])!=-1 && f(i*2+2,opy0[k][1])!=-1)
						mi = min(f(i*2+1,opy0[k][0])+f(i*2+2,opy0[k][1])+1,mi);
			}
			else
			{
				if (f(i*2+1,1)!=-1 && f(i*2+2,1)!=-1)
					mi = min(f(i*2+1,1)+f(i*2+2,1)+1,mi);
			}
		}
		else
		{
			if (j == 0)
			{
				if (f(i*2+1,0)!=-1 && f(i*2+2,0)!=-1)
					mi = min(f(i*2+1,0)+f(i*2+2,0)+1,mi);
			}
			else
			{
				for (k = 0 ; k < 3 ; k++)
					if (f(i*2+1,oph1[k][0])!=-1 && f(i*2+2,oph1[k][1])!=-1)
						mi = min(f(i*2+1,oph1[k][0])+f(i*2+2,oph1[k][1])+1,mi);
			}
		}
		to[i] ^= 1;
	}

	if (mi == 1<<30) return bw[i][j]=-1;
	return bw[i][j] = mi;
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int ca,T,tm,ans=100000,v,g,i,j;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d%d",&m,&v);
		g = (m-1)/2;
		for (i = 0 ; i < g ; i++) scanf("%d%d",&to[i],&tc[i]);
		for ( ; i < m ; i++) scanf("%d",&tr[i]);
		memset(bw,-1,sizeof bw);
		ans = f(0,v);
	/*	for (i = 0 ; i < (2<<g) ; i++)
		{
			for (j = 0 ; j < g ; j++)
				if (((1<<j)&i) && tc[j])
					to[j]^=1;
			if (dfs(0)==v)
			{
				for (j = tm = 0 ; j < g ; j++)
					if (((1<<j)&i) && tc[j])
					{
						tm++;
					}
				if (ans > tm) ans = tm;
			}
			for (j = 0 ; j < g ; j++)
				if (((1<<j)&i) && tc[j])
					to[j]^=1;
		}*/
		if (ans == -1) printf("Case #%d: IMPOSSIBLE\n",ca);
		else
			printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}