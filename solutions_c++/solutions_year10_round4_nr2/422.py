#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
const int INF=599999999;

int M[2005],ans,cost;

int dp[2005][15],save[2005][15];
int main()
{
	freopen("D:\\B-large.in","r",stdin);
	freopen("D:\\B-large.out","w",stdout);
	int t,p,i,j,ii,jj,k,N,x,y;
	scanf("%d",&t);
	int cnt=0;
	while(t--)
	{
		scanf("%d",&p);
		N=(1<<p);
		for(i=1;i<=N;i++)
		{
			scanf("%d",&M[i]);
			M[i]=p-M[i];
			for(k=0;k<M[i];k++)
				dp[i][k]=INF;
			for(k=M[i];k<=p+1;k++)
				dp[i][k]=0;
		}
		for(i=p-1;i>=0;i--)
		{
			x=(1<<i);
			for(j=1;j<=x;j++)
			{
				scanf("%d",&cost);
				for(k=0;k<=p;k++)
				{
					save[j][k]=min(dp[2*j-1][k]+dp[2*j][k],dp[2*j-1][k+1]+dp[2*j][k+1]+cost);
					if(save[j][k]>INF)save[j][k]=INF;
				}
			}
			for(j=1;j<=x;j++)
				for(k=0;k<=p;k++)
					dp[j][k]=save[j][k];
		}
		ans=dp[1][0];
		printf("Case #%d: %d\n",++cnt,ans);
	}
}