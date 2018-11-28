#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


using namespace std;



int n, k, b;
long long t;

int dp[60][60];

long long x[60], v[60];


void Load()
{
	cin >> n >> k >> b >> t;
	int i;
	for (i = 0; i < n; i++)
		cin >> x[i];
	for (i = 0; i < n; i++)
		cin >> v[i];
	reverse(x, x+n);
	reverse(v, v+n);

}

void Solve()
{
	int i, j;
	memset(dp, 0x7f,sizeof(dp));
	dp[0][0] = 0;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j <= i; j++)
		{
			if (dp[i][j] == 0x7f7f7f7f) continue;
			if (x[i]+t*v[i] >= b)
			{
				dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+i-j);
			}
			if (i > j || x[i]+t*v[i] < b)
			{
				dp[i+1][j] = min(dp[i+1][j], dp[i][j]);
			}
		}
	}
	int ans = 0x7f7f7f7f;
	for (i = k; i <= n; i++)
	{
		ans = min(ans,dp[n][i]);
	}
	if (ans == 0x7f7f7f7f)
		cout << "IMPOSSIBLE\n";
	else
    	cout << ans << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
