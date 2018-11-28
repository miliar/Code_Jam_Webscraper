#include <iostream>
#include <vector>

using namespace std;

const int M = 10007;

int solve(int w, int h, const vector<int>& rs, const vector<int>& cs)
{
	int nr = (int)rs.size();
	vector< vector<int> > dp(h, vector<int>(w, 0));
	dp[0][0] = 1;
	for (int j = 1; j < h; ++j) for (int i = 0; i < w; ++i) {
		bool isr = false;
		for (int k = 0; k < nr; ++k) if (j == rs[k] - 1 && i == cs[k] - 1) isr = true;
		if (isr) {
			dp[j][i] = 0;
		} else {
			int res = 0;
			if (i - 2 >= 0 && j - 1 >= 0) res += dp[j-1][i-2];
			if (i - 1 >= 0 && j - 2 >= 0) res += dp[j-2][i-1];
			dp[j][i] = /*(dp[j][i]*/ + res/*)*/ % M;
		}
	}
	return dp[h-1][w-1];
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int w, h, rocks;
		cin >> h >> w >> rocks;
		vector<int> rs(rocks), cs(rocks);
		for (int i = 0; i < rocks; ++i) cin >> rs[i] >> cs[i];
		
		cout << "Case #" << (test + 1) << ": " << solve(w, h, rs, cs) << endl;
	}
	return 0;
}
