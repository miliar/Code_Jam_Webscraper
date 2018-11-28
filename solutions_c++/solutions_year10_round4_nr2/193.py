#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<vector>
#include<queue> 
using namespace std;
#define M 4021
int xx[M],b[M],dp[M][15],n;
int Max(int a,int b)
{
    if (a>b)
    return a;
    return b;
} 
int Min(int a,int b)
{
    if (a<b)
    return a;
    return b;
}
void doit(int l,int r,int oo)
{
	int i,j;
	if(l+1==r)
	{
		dp[oo][xx[oo%(1<<n)]]=0;
		return ;
	}
	doit(l,(l+r)/2,oo*2);
	doit((l+r)/2,r,oo*2+1);
	for(i=0;i<=n;i++)
		for(j=0;j<=n;j++)
			dp[oo][Max(i,j)]=Min(dp[oo][Max(i,j)],dp[oo*2][i]+dp[oo*2+1][j]);
	for(i=0;i<n;i++)
		dp[oo][i]=Min(dp[oo][i],dp[oo][i+1]+b[oo]);
		return ;
}
int main()
{
	int dda,cas,i;
	freopen("B-large.in","r",stdin);
    freopen("BBB.out","w",stdout); 
	scanf("%d",&cas);
	for(dda=1;dda<=cas;dda++)
	{
		memset(dp,0x3f,sizeof(dp));
		scanf("%d",&n);
		for(i=(1<<n)-1;i>=0;i--)
		{
			scanf("%d",&xx[i]);
			xx[i]=n-xx[i];
		}
		
		
		for(i=(1<<n)-1;i>0;i--)
			scanf("%d",&b[i]);
		doit(0,(1<<n),1);
		printf("Case #%d: %d\n",dda,dp[1][0]);
	}
	return 0;
}
