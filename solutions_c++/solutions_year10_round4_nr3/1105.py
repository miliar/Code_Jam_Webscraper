#include "stdafx.h"
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void get_min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void get_max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
int map[105][105];
int map2[105][105];
int map3[105][105];
bool check()
{
	memset(map2,0,sizeof(map2));
	memset(map3,-1,sizeof(map3));
	bool ok=false;
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			if(map[i][j]==0)
			{
				if(map[i-1][j]==1&&map[i][j-1]==1) 
					map2[i][j]=1;
			}
			//printf("%d",map2[i][j]);
		}
		//printf("\n");
	}
	//printf("\n\n");
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			if(map[i][j]==1)
			{
				if(map[i-1][j]==0&&map[i][j-1]==0) 
					map3[i][j]=0;
			}
			//printf("%d",map2[i][j]);
		}
	}
	//printf("\n");
	for(int i=1;i<=100;i++)
	{
		for(int j=1;j<=100;j++)
		{
			if(map2[i][j]==1) map[i][j]=1;
			if(map3[i][j]==0) map[i][j]=0;
			if(map[i][j]==1) 
				ok=true;
		}
	}
	/*for(int i=1;i<=10;i++)
	{
		for(int j=1;j<=10;j++)
		{
			printf("%d",map[i][j]);
		}
		printf("\n");
	}
	printf("\n");*/
	return ok;
}
int main()
{
	//freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	freopen("e:\\C-small-attempt0.in","r",stdin);
	//freopen("e:\\A-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int n;
		int x,y,x2,y2;
		_clr(map,0);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d%d",&x,&y,&x2,&y2);
			if(x>x2) swap(x,x2);
			if(y>y2) swap(y,y2);
			for(int j=x;j<=x2;j++)
			{
				for(int k=y;k<=y2;k++)
				{
					map[k][j]=1;
				}
			}	
		}
		int ans=0;
		while(check())
		{
			ans++;
		}
		printf("%d\n",ans+1);
	}
	return 0;
}
