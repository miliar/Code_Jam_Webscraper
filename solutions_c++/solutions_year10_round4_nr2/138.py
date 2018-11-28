#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
using namespace std;
#define MAX 3000
int a[MAX],b[MAX],dp[MAX][12],n;
void calc(int l,int r,int m)
{
	int i,j;
	if(l+1==r)
	{
		dp[m][a[m%(1<<n)]]=0;
		return ;
	}
	calc(l,(l+r)/2,m*2);
	calc((l+r)/2,r,m*2+1);
	for(i=0;i<=n;i++)
		for(j=0;j<=n;j++)
			dp[m][max(i,j)]=min(dp[m][max(i,j)],dp[m*2][i]+dp[m*2+1][j]);
	for(i=0;i<n;i++)
		dp[m][i]=min(dp[m][i],dp[m][i+1]+b[m]);
}
int main()
{
	int dd,cs,i;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		memset(dp,0x3f,sizeof(dp));
		scanf("%d",&n);
		for(i=(1<<n)-1;i>=0;i--)
		{
			scanf("%d",&a[i]);
			a[i]=n-a[i];
		}
		for(i=(1<<n)-1;i>0;i--)
			scanf("%d",&b[i]);
		calc(0,(1<<n),1);
		printf("Case #%d: %d\n",dd,dp[1][0]);
	}
}