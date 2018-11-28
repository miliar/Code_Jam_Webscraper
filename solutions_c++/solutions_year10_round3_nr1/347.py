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
int N,height[1000][2];
int main()
{
	freopen("e:\\A-large.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	//freopen("e:\\A-small-attempt0.in","r",stdin);
	//freopen("e:\\A-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&height[i][0],&height[i][1]);
		}
		int ans=0;
		for(int i=0;i<N;i++)
		{
			for(int j=i+1;j<N;j++)
			{
				if((height[i][0]-height[j][0])*(height[i][1]-height[j][1])<0) ans++;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
