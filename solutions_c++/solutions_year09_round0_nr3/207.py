#include <iostream>
#include <vector>
#include <string>

using namespace std;

int mod = 10000;
string t = "welcome to code jam";

int dp[555][20];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt; scanf("%d\n", &tt);
	for(int z = 1; z <= tt; ++z)
	{
		string s; getline(cin, s);
		memset(dp, 0, sizeof dp);
		dp[0][0] = 1;
		int n = s.length();
		int m = t.length();
		for(int i = 1; i <= n; ++i)
		{
			
			for(int j = 0; j < m; ++j)
				if(t[j] == s[i - 1])
				{
					for(int k = 0; k < i; ++k)
						dp[i][j + 1] += dp[k][j],
						dp[i][j + 1] %= mod;
				}
		}
		/*
		cerr << "#" << endl;
		for(int j = 0; j < m + 1; ++j)
		{
			for(int i = 0; i <= n; ++i)
				cout << dp[i][j] << " ";
			cout << endl;
		}

		*/	
		int res = 0;
		for(int i = 0; i <= n; ++i)
			res += dp[i][m],
			res %= mod;
		printf("Case #%d: %04d\n", z, res);
	}
	return 0;
}