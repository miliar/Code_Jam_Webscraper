#include<iostream>
#include<cstdio>
#define mod 100003
using namespace std;

int a[1010],dp[1010][1010],c[1010][1010];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int i,j,cs,cc,k;
	c[0][0]=1;
	for (i=1;i<=500;i++)
	{
		c[i][0]=1;
		c[i][i]=1;
		for (j=1;j<i;j++)
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%mod;
	}
	memset(dp,0,sizeof(dp));
	for (i=2;i<=500;i++) dp[i][1]=1;
	for (i=3;i<=500;i++)
		for (j=2;j<i;j++)
			for (k=1;k<=j;k++)
				dp[i][j]+=(dp[j][k]*c[i-j-1][j-k-1])%mod;
	
	for (i=2;i<=500;i++)
		for (j=1;j<i;j++)
			a[i]=(a[i]+dp[i][j])%mod;
	cin>>cs;
	for (cc=1;cc<=cs;cc++)
	{
		cin>>k;
		cout<<"Case #"<<cc<<": "<<a[k]<<endl;		
	}
}
