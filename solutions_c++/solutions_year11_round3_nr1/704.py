//============================================================================
// Name        : gcj_A.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#define ll long long
#define _clr(a) memset(a,0,sizeof(a));
#define FOR(i,x,n) for(int i=x;i<n;i++)
#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b
#define abs(a) a>0?a:a*-1
#define re return
#define sqr(x) ((x) * (x))
#define inf 268435456;
using namespace std;
const double eps=1e-10;
const double pi=acos(-1);
char a[55][55];
int main()
{
	int n,m,cas=1,t;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",a[i]);
		int flag=1;
		for(int i=0;i<n&&flag;i++)
			for(int j=0;j<m&&flag;j++)
			{

				if(a[i][j]=='#')
				{
					if(i==n-1||j==m-1)flag=0;
					if(a[i+1][j+1]=='#'&&a[i+1][j]=='#'&&a[i][j+1]=='#')
					{
						a[i][j]='/';
						a[i+1][j]='\\';
						a[i+1][j+1]='/';
						a[i][j+1]='\\';
					}
					else flag=0;
				}
			}

		printf("Case #%d:\n",cas++);
		//printf("Case %d: ",cas++);
		//puts("");
		if(flag)for(int i=0;i<n;i++)puts(a[i]);
		else puts("Impossible");
	}
	re 0;
}
