#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int a[513][513];
int v[513][513],h[513][513];
int ans[513];

void calc(int n,int m)
{
	int i,j;
	for (i=0; i<n; ++i)
	{
		for (j=0; j<m; ++j)
		{
			if (a[i][j]==-1) h[i][j]=0;
			else if (j==0 || a[i][j]==a[i][j-1])
				h[i][j]=1;
			else h[i][j]=h[i][j-1]+1;
		}
	}
	for (i=0; i<m; ++i)
	{
		for (j=0; j<n; ++j)
		{
			if (a[j][i]==-1) v[j][i]=0;
			else if (j==0 || a[j][i]==a[j-1][i])
				v[j][i]=1;
			else v[j][i]=v[j-1][i]+1;
		}
	}
}

int num[256];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t,tt;
	int i,j,u;
	int n,m;
	int ii,jj;
	char c;
	int res;
	scanf("%d",&t);
	for (i=0; i<10; ++i)
		num['0'+i]=i;
	for (c='A',i=10; c<='F'; ++c,++i)
		num[c]=i;
	for (tt=0; tt<t; ++tt)
	{
		scanf("%d%d\n",&n,&m);
		for (i=0; i<n; ++i)
		{
			for (j=0; j<(m>>2); ++j)
			{
				scanf("%c",&c);
				for (u=0; u<4; ++u)
					a[i][j*4+u]=(num[c]>>(3-u))&1;
			}
			scanf("\n");
		}
	/*	for (i=0; i<n; ++i)
		{
			for (j=0; j<m; ++j)
				printf("%d ",a[i][j]);
			printf("\n");
		}
	*/	memset(ans,0,sizeof(ans));
		for (u=min(n,m); u>0; --u)
		{
			calc(n,m);
			for (i=0; i<n; ++i)
				for (j=0; j<m; ++j)
				{
					if (min(h[i][j],v[i][j])>=u)
					{
						for (ii=i; ii>i-u; --ii)
							if (h[ii][j]<u) break;
						if (ii>i-u) continue;
						for (ii=i; ii>i-u; --ii)
						{
							for (jj=j; jj>j-u; --jj)
								if (a[ii][jj]==-1) break;
							if (jj>j-u) break;
						}
						if (ii>i-u) continue;
						for (ii=i; ii>i-u; --ii)
							for (jj=j; jj>j-u; --jj)
								a[ii][jj]=-1;
						ans[u]++;
					//	printf("%d %d %d\n",i,j,u);
					}
				}
		}
		res=0;
		for (u=1; u<=min(n,m); ++u)
			if (ans[u]>0) res++;
		printf("Case #%d: %d\n",tt+1,res);
		for (u=min(n,m); u>0; --u)
			if (ans[u]>0) printf("%d %d\n",u,ans[u]);
	//	return 0;
	}
	return 0;
}