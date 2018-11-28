#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

const int MAXN = 500+10, MOD = 100003;

typedef long long ll;

ll dp[MAXN][MAXN], cmb[MAXN][MAXN];

void init()
{
	for(int i=0; i<MAXN-1; i++)
	{
		cmb[i][0] = 1;
		for(int j=1; j<=i; j++)
			cmb[i][j] = (cmb[i-1][j] + cmb[i-1][j-1])%MOD;
	}
}

void BF(int n) //BruteForce
{
	int cnt = 0;
	for(int i=0; i<(1<<(n-1)); i++)
	{
		int plc[MAXN];
		memset(plc, 0, sizeof plc);
		vector<int> vl(1);
		for(int j=0; j<n-1; j++)
			if((i >> j)&1)
			{
				int d = j + 2;
				vl.push_back(d);
				plc[d] = vl.size()-1;
			}

		int t = n;
		while(plc[t])
			t = plc[t];
		if(t == 1)
			cnt++;
	}
	cout <<"@ " << cnt << endl;
}

int main()
{
	int t;
	init();
	cin >> t;
	for(int ts=1; ts<=t; ts++)
	{
		memset(dp, 0, sizeof dp);
		int n;
		cin >> n;
//		BF(n);
		dp[1][1] = 0;
		for(int i=2; i<=n; i++)
		{
			dp[i][1] = 1;
			for(int j=2; j<i; j++)
				for(int k=1; k<j; k++)
					dp[i][j] = (dp[i][j] + dp[j][k] * cmb[i-j-1][j-k-1])%MOD;
		}
		ll sum = 0;
		for(int i=0; i<n; i++)
			sum += dp[n][i];
		sum %= MOD;
		cout << "Case #" << ts << ": " << sum << endl;
	}
	return 0;
}
