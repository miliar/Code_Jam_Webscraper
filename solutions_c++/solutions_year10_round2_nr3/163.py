#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

const int MaxN = 508;
const int mod = 100003;
typedef long long LL;

int dp[MaxN][MaxN];
int C[MaxN][MaxN];

void Init()
{
	C[0][0] = C[1][0] = C[1][1] = 1;
	for(int i=2; i<MaxN; i++)	
	{
		C[i][0] = C[i][i] = 1;
		for(int j=1; j<i; j++)	
			C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod;	
	}
	dp[1][0] = 1;
	for(int i=2; i<MaxN; i++)
	{
		dp[i][1] = 1;
		for(int j=2; j<i; j++)
		{
			for(int k=0; k<j-1 && k<i-j; k++)
			{
				dp[i][j] += (LL)dp[j][j-k-1]*C[i-j-1][k]%mod;	
			}	
			dp[i][j] %= mod;
		}	
	}	
	for(int i=2; i<MaxN; i++)
	{
		for(int j=2; j<i; j++)	dp[i][j] += dp[i][j-1];
		dp[i][i-1] %= mod;	
	}
}	

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	Init();
	int cases;	cin >> cases;
	for(int cas=1; cas<=cases; cas++)
	{
		int N;	cin >> N;
		printf("Case #%d: %d\n", cas, dp[N][N-1]);
	}
	
	
	return 0;	
}
