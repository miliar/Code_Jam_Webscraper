#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

void initialize() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

void solve() {
	int n;
	cin >> n;
	vector<string> s;
	vector<int> t;
	s.resize(n);
	t.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> s[i];
		t[i] = 0;
		for (int j = 0; j < s[i].size(); ++j)
			if (s[i][j] == '1')
				t[i] = j + 1;
	}
	int res = 0;
	for (int i = 0; i < n; ++i) {
		int need = i + 1;
		int u = i;
		while (t[u] > need) ++u;
		while (u != i) {
			swap(t[u], t[u - 1]);
			u--;
			res++;
		}
	}
	cout << res << endl;

}

int main() {
	initialize();
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
	return 0;
}
