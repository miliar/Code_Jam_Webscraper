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
int ans;
int height[45];
char row[45];
int n;
int main()
{
	freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int T;
	int temp;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		_clr(height,0);
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%s",row+1);
			for(int j=n;j>=1;j--)
			{
				if(row[j]=='1')
				{
					height[i]=j;
					break;
				}
			}
		}
		ans=0;
		for(int i=1;i<=n;i++)
		{
			if(height[i]>i)
			{
				for(int j=i+1;j<=n;j++)
				{
					if(height[j]<=i)
					{
						temp=height[j];
						for(int k=j;k>i;k--) height[k]=height[k-1];
						height[i]=temp;
						ans+=j-i;
						break;
					}
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
