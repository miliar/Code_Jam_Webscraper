#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <map>
using namespace std;

int mod=100003;
int c[510][510]={0};
int f[510][510]={0};
int ans[510]={0};

void init()
{
	for(int i=0;i<505;i++)
	{
		c[i][0]=c[i][i]=1;
	}
	for(int i=1;i<505;i++)
	{
		for(int j=1;j<i;j++)
		{
			c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod;
			c[j][i]=0;
		}
	}

	for(int i=1;i<505;i++)
	{
		f[i][1]=1;
	}
	for(int i=2;i<505;i++)
	{
		for(int j=2;j<=i-1;j++)
		{
			f[i][j]=0;
			for(int k=1;k<j;k++)
			{
				
				f[i][j]=(f[i][j]+f[j][k]*c[i-j-1][j-k-1]%mod)%mod;
			}
		}
	}
	for(int i=2;i<505;i++)
	{
		for(int j=1;j<i;j++)
			ans[i]+=f[i][j];
	}

}
void solve()
{
	int t;
	cin>>t;
	cout<<ans[t]<<endl;
}
int main()
{
	freopen("d://out.txt","w",stdout);
	init();
	int cs;
	cin>>cs;
	for(int ii=1;ii<=cs;ii++)
	{
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}