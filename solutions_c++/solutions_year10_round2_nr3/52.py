#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;

#define fore(i,n) for(int i = 0; i < (n); i++)
#define fort(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

#define err(...) fprintf(stderr, __VA_ARGS__)

#define M 100003
#define maxn 507

int dp[maxn][maxn];
int t[maxn][maxn];

void test()
{
	int res = 0, n;
	scanf("%d", &n);
	for(int i = 1; i < n; i++) res = (res + dp[n][i]) % M;
	printf("%d\n", res);
}

void init()
{
	for(int i = 0; i < maxn; i++) t[0][i] = t[i][i] = 1;
	for(int i = 1; i < maxn; i++) for(int j = 1; j < i; j++)
	{
		t[j][i] = (t[j][i-1] + t[j-1][i-1]) % M;
	}
	for(int n = 2; n < maxn; n++) dp[n][1] = 1;
	for(int n = 2; n < maxn; n++) for(int s = 2; s < n; s++)
	{
		for(int i = max(0,2*s-n); i < s; i++)
		{
			dp[n][s] = (1LL * dp[s][i] * t[s-i-1][n-s-1] + dp[n][s]) % M;
		}
		//printf("dp[%d][%d] = %d\n", n,s,dp[n][s]);
	}
}

int main()
{
	init();
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++)
	{
		printf("Case #%d: ", TT);
		test();
	}
}
