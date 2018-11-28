#include <iostream>
#include <vector>
#include <string>

using namespace std;

int nbits(int mask)
{
	int res = 0;
	for (int i = 0; i < 11; ++i) if (mask & (1 << i)) ++res;
	return res;
}

int solve(int m, int n, const vector<string>& v)
{
	cerr << "solve(" << m << ", " << n << ")\n";

	int dp[10][1024];
	for (int line = 0; line < m; ++line) {
		for (int mask = 0; mask < (1 << n); ++mask) {
			bool sat = true;
			for (int i = 0; i < n; ++i) if ((mask & (1 << i)) && v[line][i] == 'x') sat = false;
			for (int i = 0; i < n - 1; ++i) if ((mask & (1 << i)) && (mask & (1 << (i + 1)))) sat = false;
			if (sat) {
				if (line == 0) {
					dp[line][mask] = nbits(mask);
				} else {
					int mx = 0;
					for (int prevmask = 0; prevmask < (1 << n); ++prevmask) {
						bool compat = true;
						for (int i = 0; i < n - 1; ++i) if ((mask & (1 << i)) && (prevmask & (1 << (i + 1)))) compat = false;
						for (int i = 1; i < n; ++i)     if ((mask & (1 << i)) && (prevmask & (1 << (i - 1)))) compat = false;
						if (compat && nbits(mask) + dp[line-1][prevmask] > mx) mx = nbits(mask) + dp[line-1][prevmask];
					}
					dp[line][mask] = mx;
				}
			}
		}
	}

	int result = 0;
	for (int mask = 0; mask < (1 << n); ++mask) if (dp[m - 1][mask] > result) result = dp[m - 1][mask];
	return result;
}

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int m, n;
		cin >> m >> n;
		vector<string> v(m);
		string s;
		/*
		getline(cin, s);
		cerr << s.length() << endl;
		for (int i = 0; i < m; ++i) {
			getline(cin, v[i]);
			cerr << " " << v[i].length() << endl;
		}
		//getline(cin, s);
		cerr << s.length() << endl;
		*/
		for (int i = 0; i < m; ++i) cin >> v[i];
		for (int i = 0; i < m; ++i) cerr << v[i] << endl;

		cout << "Case #" << (test + 1) << ": " << solve(m, n, v) << endl;
	}
	return 0;
}
