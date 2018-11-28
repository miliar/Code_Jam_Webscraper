#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, m;
ll del, ins;
vector<ll> a;
vector<vector<ll> > dp;

ll oo = 1 << 25;

ll Abs(ll x)
{
	return x > 0 ? x : -x;
}

ll Solve()
{
	int ceil = 1 << 8;
	dp.assign(n + 1, vector<ll>(ceil, oo));
	dp[0][0] = 0;
	for(int i = 1; i < ceil; i++)
		dp[0][i] = 0;
	for(int i = 1; i <= n; i++)
	{
		for(int j = 0; j < ceil; j++)
		{
			dp[i][j] = dp[i - 1][j] + del;
			for(int k = 0; k < ceil; k++)
			{
				if(Abs(j - k) <= m)
				{
					dp[i][j] = min(dp[i][j], dp[i - 1][k] + Abs(a[i - 1] - j));					
				}
				if(Abs(j - a[i - 1]) <= m && Abs(k - a[i - 1]) <= m)
				{
					dp[i][j] = min(dp[i][j], dp[i - 1][k] + ins);
				}
			}			
		}
		for(int j = 0; j < ceil; j++)
		{
			for(int k = 1; k <= m && j - k >= 0; k++)
			{
				dp[i][j] = min(dp[i][j], dp[i][j - k] + ins);
			}			
		}
		for(int j = ceil - 1; j >= 0; j--)
		{
			for(int k = 1; k <= m && j + k < ceil; k++)
			{
				dp[i][j] = min(dp[i][j], dp[i][j + k] + ins);
			}	
		}
	}
	return *min_element(dp.back().begin(), dp.back().end());
}

int main()
{
	ifstream in("in.txt");
	int tests;
	in >> tests;
	for(int test = 1; test <= tests; test++)
	{
		in >> del >> ins >> m >> n;
		a.resize(n);
		for(int i = 0; i < n; i++)
			in >> a[i];
		cout << "Case #" << test << ": " << Solve() << endl;
	}
	return 0;
}