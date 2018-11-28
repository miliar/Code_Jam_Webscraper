#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solve(string t, vector<string>& w, int l)
{
	int res = 0;
	vector<string> tt;
	bool in = false;
	for (int i = 0, len = (int) t.length(); i < len; ++i) {
		if (t[i] == '(') {
			in = true;
			tt.push_back("");
		} else if (t[i] == ')') {
			in = false;
			sort(tt.back().begin(), tt.back().end());
		} else {
			if (in) tt.back().push_back(t[i]);
			else tt.push_back(string(1, t[i]));
		}
	}
	for (int i = 0, count = (int) w.size(), j = 0; i < count; ++i) {
		for (j = 0; j < l; ++j) {
			if (!binary_search(tt[j].begin(), tt[j].end(), w[i][j])) break;
		}
		if (j == l) ++res;
	}
	return res;
}

int main()
{
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> w(d);
	for (int i = 0; i < d; ++i) cin >> w[i];
	vector<string> t(n);
	for (int i = 0; i < n; ++i) cin >> t[i];

	sort(w.begin(), w.end());

	for (int i = 0; i < n; ++i) {
		cout << "Case #" << (i + 1) << ": " << solve(t[i], w, l) << endl;
	}
}