#include<cstdio>
#include<cstring>

const int mx=550;
const __int64 mod=100003;

int n=501;
__int64 c[mx][mx];
__int64 dp[mx][mx];
__int64 ans[mx];

void init_c()
{
	c[0][0]=1;
	for(int i=0;i<100;i++)
	{
		c[i][0]=1;
		for(int j=1;j<=i;j++)
		{
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%mod;
		}
	}
}

__int64 cc(int n,int k)
{
	if(n<0||k<0||k>n)return 0;
	return c[n][k];
}

void init()
{
	int i,j,k;
	init_c();
	for(i=0;i<n;i++)
		dp[0][i]=dp[1][i]=dp[2][i]=0;
	for(i=2;i<n;i++)
		dp[i][1]=1;
	for(i=3;i<n;i++)
	{
		for(j=2;j<i;j++)
		{
			for(k=1;k<j;k++)
			{
				dp[i][j]+=dp[j][k]*cc(i-j-1,j-k-1);
				dp[i][j]%=mod;
			}
		}
	}
	for(i=2;i<n;i++)
	{
		ans[i]=0;
		for(j=1;j<n;j++)
		{
			ans[i]+=dp[i][j];
			ans[i]%=mod;
		}
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outC.txt","w",stdout);
	int tt,ca=1;
	init();
	scanf("%d",&tt);
	/*
	freopen("out500_2.txt","w",stdout);
	for(int i=2;i<=500;i++)
		printf("%d: %I64d\n",i,ans[i]);
	*/
	while(tt--)
	{
		scanf("%d",&n);
		printf("Case #%d: %I64d\n",ca++,ans[n]);
	}
	

	return 0;
}
