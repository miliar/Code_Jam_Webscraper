#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define MOD 100003

/*int dp[501][501][2],tot[501];

int main()
{
	int T,i,j,k,N;
	//freopen("C-small-attempt1.in","r",stdin);
	//freopen("C.out","w",stdout);
	memset(dp,0,sizeof(dp));
	memset(tot,0,sizeof(tot));
	dp[1][0][1] = 1;
	tot[1] = 1;
	for(i = 2;i <= 500;i++)
	{
		for(j = 0;j < i - 1;j++)
		{
			dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1])%MOD;
			dp[i][j][1] = tot[j];
		}
		for(j = 0;j < i;j++)
			tot[i] = (tot[i] + dp[i][j][1])%MOD;
	}
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d",&N);
		int ans = 0;
		for(i = 0;i <= N;i++)
			ans = (ans + dp[N][i][0])%MOD;
		printf("Case #%d: %d\n",Case,(ans + tot[N])%MOD);
	}
	return 0;
}*/

int check(int n)
{
	int num[26],i,j,ans = 0;
	bool use[26];
	for(i = 0;i < (1 << (n - 1));i++)
	{
		memset(use,false,sizeof(use));
		for(j = 0;j < n - 1;j++)
		{
			if(i & (1 << j))
				use[j+2] = true;
		}
		use[1] = true;
		if(!use[n])
			continue;
		int t = 1;
		for(j = 2;j <= n;j++)
		{
			if(use[j])
				num[j] = t,t++;
		}
		t = n;
		while(t != 1)
		{
			if(!use[num[t]])
				break;
			t = num[t];
		}
		if(t == 1)
		{
			ans++;
		}
	}
	return ans;
}

int f[501];

int main()
{
	int i;
	//freopen("C-small-attempt3.in","r",stdin);
	//freopen("C.out","w",stdout);
	for(i = 2;i <= 25;i++)
		f[i] = check(i) % MOD;
	int T,N;
	scanf("%d",&T);
	for(int Case = 1;Case <= T;Case++)
	{
		scanf("%d",&N);
		printf("Case #%d: %d\n",Case,f[N]);
	}
	return 0;
}
