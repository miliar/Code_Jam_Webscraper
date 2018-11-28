#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int mod = 10000;

int main()
{
	freopen("large.in",  "r", stdin);
	freopen("output.txt", "w", stdout);

	string temp;
	int N;
	cin >> N;
	getline(cin, temp);

	string pattern = "welcome to code jam";
	int pl = pattern.length();
	for (int numCase = 1; numCase <= N; numCase++)
	{
		string str;
		getline(cin, str);
		int len = str.length();

		vector< vector<int> > dp(len + 1, vector<int> (pl + 1, 0) );

		for (int i = 0; i <= len; i++) 
			dp[i][0] = 1;

		for (int j = 1; j <= pl; j++)
			for (int i = 1; i <= len; i++)
				dp[i][j] = (dp[i - 1][j] + (pattern[j - 1] == str[i - 1]) * dp[i - 1][j - 1] ) % mod;

		int ans = dp[len][pl];
		cout << "Case #" << numCase << ": ";
		int t = 1000;
		while (t > ans && t > 1)
		{
			cout << "0";
			t = t / 10;
		}
		cout << ans << endl;
	}

	return 0;
}