#include <iostream>
#include <vector>
#include <string>
#include <boost/format.hpp>

using namespace std;

int solve(string s)
{
	string wtcj = "welcome to code jam";
	int wtcjlen = (int) wtcj.length();
	int len = (int) s.length();
	vector< vector<int> > dp(20, vector<int>(len + 1));
	dp[0][0] = 1;
	for (int i = 0; i < len; ++i) {
		for (int j = 0; j <= wtcjlen; ++j) {
			if (dp[j][i]) {
				if (j < wtcjlen && s[i] == wtcj[j]) {
					dp[j + 1][i + 1] += dp[j][i];
					dp[j + 1][i + 1] %= 10000;
				}
				dp[j][i + 1] += dp[j][i];
				dp[j][i + 1] %= 10000;
			}
		}
	}
	return dp[wtcjlen][len];
}

int main()
{
	int n;
	cin >> n;
	string s;
	getline(cin, s);
	for (int i = 0; i < n; ++i) {
		getline(cin, s);
		cout << "Case #" << (i + 1) << ": " << (boost::format("%04d") % solve(s)).str() << endl;
	}
}
