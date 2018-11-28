#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

vector<long long> d, l;
vector<vector<bool> > dp;
queue<pair<int, int> > q;

bool solve() {
	int n;
	cin >> n;
	d.resize(n + 2);
	l.resize(n + 2);
	for (int i = 1; i <= n; ++i) {
		cin >> d[i] >> l[i];
	}
	dp.assign(n + 2, vector<bool> (n + 2, false)); 
	d[0] = 0;
	l[0] = 0;
	cin >> d[n + 1];
	l[n + 1] = 0;

	n += 2;

	dp[0][1] = true;
	q.push(make_pair(0, 1));
	while (!q.empty()) {
		int place = q.front().first;
		int take = q.front().second;
		q.pop();
		if (place == n - 1) return true;
		long long max_len = min(llabs(d[place] - d[take]), l[take]);
		if (!dp[take][place]) {
			dp[take][place] = true;
			q.push(make_pair(take, place));
		}

		int di = place < take ? 1 : -1;
		for (int i = place + di; i < n && i >= 0; i += di) {
			long long cur_len = labs(d[i] - d[take]);
			if (cur_len > max_len) break;
			if (dp[take][i] || i == take) continue;
			dp[take][i] = true;
			q.push(make_pair(take, i));
		}
	}
	return false;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		cout << (solve() ? "YES" : "NO") << endl;
	}
	return 0;
}