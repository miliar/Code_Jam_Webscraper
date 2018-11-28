#include<stdio.h>
#include<string.h>

#define LL long long
#define mod 100003

LL ncr[502][502];
LL calc(int n,int r)
{
	if(!r || n==r)return 1;
	if(ncr[n][r]!=-1)return ncr[n][r];
	ncr[n][r]=(calc(n-1,r)+calc(n-1,r-1))%mod;
	return ncr[n][r];
}

LL dp[502][502];
LL make(int n,int k)
{
	int i;
	if(k==1 || k==2 || (n-1)==k)
		return 1;
	if(dp[n][k]!=-1)
		return dp[n][k];
	dp[n][k]=0;
	LL temp;
	for(i=1;i<=(n-k) && (k-i)>=1;i++)
		temp=make(k,k-i)*calc(n-k-1,i-1),
		dp[n][k]=(dp[n][k]+temp)%mod;
	return dp[n][k];
}

int main()
{
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	int t,i,n,ans,cs;
	memset(ncr,-1,sizeof(ncr));
	memset(dp,-1,sizeof(dp));
	scanf("%d",&t);
	for(cs=0;cs<t;cs++)
	{
		scanf("%d",&n);
		ans=0;
		for(i=1;i<n;i++)
			ans=(ans+make(n,i))%mod;
		printf("Case #%d: %d\n",cs+1,ans);
	}
	return 0;
}