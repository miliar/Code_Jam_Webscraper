#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

const int MOD = 10000;
const string target = "$welcome to code jam"; // '$' is dummy

int main() {
	int t; cin>>t;
	string str;
	getline(cin, str); // skip first line
	for (int tc = 1; tc <= t; tc++) {
		getline(cin, str);
		vector<vector<int> > dp(str.size(), vector<int>(target.size(),0));
		for (int i = 0; i < str.size(); i++) dp[i][0] = 1;
		for (int i = 0; i < str.size(); i++) {
			for (int j = 1; j < target.size(); j++) {
				if (i) dp[i][j] += dp[i-1][j];
				if (str[i] == target[j]) dp[i][j] += dp[i][j-1];
				dp[i][j] %= MOD;
			}
		}
		
		printf("Case #%d: %04d\n", tc, dp[str.size()-1][target.size()-1]%MOD);
	}
	return 0;
}