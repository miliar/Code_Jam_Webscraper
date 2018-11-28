#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#define M 500000

using namespace std;

__int64 d,miin[21][2*M+1],dp[21][2*M+1],ans,z;
int T,t,i,j,x[21],c[21],n;

__int64 ab(__int64 x)
{
	return x>0?x:-x;
}

__int64 mx(__int64 x,__int64 y)
{
	return x>y?x:y;
}

__int64 cost(int i,int j)
{
	return mx(ab(x[i]-j+d),ab(x[i]-j+c[i]*d));
}

int main()
{
	freopen("b.in","r",stdin);	freopen("b.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		ans=1999999999;
		scanf("%d%I64d",&n,&d);
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&x[i],&c[i]);
			x[i]+=x[i];
		}
		d+=d;
		for(j=-M;j<-M+c[0]*d;j++)
		{
			dp[0][j+M]=1999999999;
			miin[0][j+M]=1999999999;
		}
		for(j=-M+c[0]*d;j<=M;j++)
		{
			dp[0][j+M]=cost(0,j);
			if(miin[0][j-1+M]<dp[0][j+M])
				miin[0][j+M]=miin[0][j-1+M];
			else
				miin[0][j+M]=dp[0][j+M];
		}
		for(i=1;i<n;i++)
		{
			for(j=-M;j<-M+c[i]*d;j++)
				dp[i][j+M]=miin[i][j+M]=1999999999;
			for(j=-M+c[i]*d;j<=M;j++)
			{
				z=cost(i,j);
				if(z>miin[i-1][M+j-c[i]*d])
					dp[i][j+M]=z;
				else
					dp[i][j+M]=miin[i-1][M+j-c[i]*d];
				miin[i][j+M]=miin[i][j-1+M]<dp[i][j+M]?miin[i][j-1+M]:dp[i][j+M];
			}
		}
		for(j=-M;j<=M;j++)
			if(dp[n-1][j+M]<ans)
				ans=dp[n-1][j+M];
		printf("Case #%d: %I64d.%I64d\n",++t,ans/2,ans%2*5);
	}
	return 0;
}