#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
#define M 510
#define MOD 100003

long long C[M][M];

long long dp[M][M];

int n;

void show_ans()
{
	long long ans = 0;
	int j;
		for (j=1;j<n;j++) ans = (ans + dp[n][j]) % MOD;
	cout << ans << endl;
}

long long calc(int a,int b)
{
	if (a < b) return 0;
	if (C[a][b] != -1) return C[a][b];
	if (b == 0)
	{
		C[a][b] = 1;
		return C[a][b];
	}
	else
	{
		C[a][b] = calc(a - 1,b - 1) + calc(a - 1,b);
		return C[a][b];
	}
}

void work_ans()
{
	memset(dp,0,sizeof(dp));
	dp[2][1] = 1;
	int i,j,k;
	long long temp;
	for (i=3;i<=n;i++)
		for (j=1;j<i;j++)
		{
			if (j == 1)
			{
				dp[i][j] = 1;
				continue;
			}
			for (k=0;k<j-1;k++)
			{
				temp = dp[j][j - k - 1] * calc(i - j - 1,k);
				dp[i][j] = (dp[i][j] + temp) % MOD;
			}
		}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	cin >> t;
	memset(C,-1,sizeof(C));
	for (i=1;i<=t;i++)
	{
		cin >> n;
		work_ans();
		cout << "Case #" << i << ": ";
		show_ans();
	}
	return 0;
}