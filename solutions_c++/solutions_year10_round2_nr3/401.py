#include<cstdio>
#include<cstring>

long long int fact(int n)
{
	if(n == 0) return 1;

	long long int s = 1;
	for(long long int i = 1;i <= n;++i) s *= i;
	return s;
}

long long int bc(int n,int r)
{
	if(n < r) return 0LL;

	if(r >= n-r)
	{
		long long int s = 1;
		for(long long int i = r+1;i <= n;++i) s *= i;
		return s / fact(n-r);
	}
	else
	{
		long long int s = 1;
		for(long long int i = n-r+1;i <= n;++i) s *= i;
		return s / fact(r);
	}
}

int main()
{
	int T,N;
	long long int dp[505][505];
	scanf("%d\n",&T);
	for(int ii = 1;ii <= T;++ii)
	{
		memset(dp,0,sizeof(dp));
		scanf("%d\n",&N);

		for(int i = 2; i<=N;++i) dp[i][1] = 1LL;
		for(int i = 2;i <= N;++i) for(int j = 2;j < i;++j) for(int k = 1;k < j;++k) dp[i][j] = (dp[i][j] + dp[j][k] * bc(i-1-j,j-k-1)) % 100003LL;

		//for(int i = 2;i <= N;++i)
		//{
		//	for(int j = 1;j < i;++j) printf("%lld ",dp[i][j]);
		//	printf("\n");
		//}

		long long int s = 0;
		for(int i = 1;i <= N-1;++i) s = (s + dp[N][i]) % 100003LL;
		printf("Case #%d: %lld\n",ii,s);
	}

	return 0;
}
