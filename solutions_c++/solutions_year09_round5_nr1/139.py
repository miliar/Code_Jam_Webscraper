#include <cstdio>
#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <string>

void initialize() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
}

int n, m;
vector<string> a;
typedef pair<int, int> pii;

struct field {
	vector<string> a;
friend bool operator <(const field &a, const field &b) {
	return a.a < b.a;
}
};


bool good(const field &a) {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if ((a.a[i][j] == 'x') || (a.a[i][j] == 'o'))
				return false;
	return true;
}

bool stable(const field &a) {
	vector<pii> u;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if ((a.a[i][j] == 'w') || (a.a[i][j] == 'o'))
				u.push_back(pii(i, j));
	if (u.size() == 1)
		return true;
	if ((abs(u[0].first - u[1].first) + abs(u[0].second - u[1].second)) == 1)
		return true;
	else
		return false;
}

bool canmove(int i, int j, int di, int dj, const field &a) {
	if ((i < 0) || (i >= n) || (j < 0) || (j >= m)) return false;
	if ((i + di < 0) || (i + di >= n) || (j + dj < 0) || (j + dj >= m)) return false;
	if ((i - di < 0) || (i - di >= n) || (j - dj < 0) || (j - dj >= m)) return false;
	if ((a.a[i][j] != 'o') && (a.a[i][j] != 'w'))
		return false;
	if ((a.a[i + di][j + dj] == 'o') || (a.a[i + di][j + dj] == 'w') || (a.a[i + di][j + dj] == '#'))
		return false;
	if ((a.a[i - di][j - dj] == 'o') || (a.a[i - di][j - dj] == 'w') || (a.a[i - di][j - dj] == '#'))
		return false;
	return true;
}

void print(const field &a) {
	for (int i = 0; i < n; ++i)
		cout << a.a[i] << endl;
	cout << endl;
}

field move(int i, int j, int di, int dj, field a) {
	assert(canmove(i, j, di, dj, a));
	if (a.a[i][j] == 'w')
		a.a[i][j] = 'x';
	else
		a.a[i][j] = '.';
	if (a.a[i + di][j + dj] == 'x')
		a.a[i + di][j + dj] = 'w';
	else
		a.a[i + di][j + dj] = 'o';
	return a;
}

set<field> can;
vector<pair<field, int>> bfs;

void solve() {
	cin >> n >> m;
	field a;
	a.a.resize(n);
	for (int i = 0; i < n; ++i)
		cin >> a.a[i];

	can.clear();
	bfs.clear();
	can.insert(a);
	bfs.push_back(make_pair(a, 0));
//	print(a);

	for (int i = 0; i < bfs.size(); ++i) {
		field tmp = bfs[i].first;
		int LEN = bfs[i].second;
		if (good(tmp)) {
			cout << LEN << endl;
			return;
		}
//		cout << "NOW = " << endl;
//		print(tmp);
		bool STABLE = stable(tmp);
//		if (!STABLE)
//			cout << "non-stable\n\n";
		for (int p = 0; p < n; ++p)
			for (int q = 0; q < m; ++q)
				for (int dp = -1; dp <= 1; ++dp)
					for (int dq = -1; dq <= 1; ++dq)
						if (abs(dp) + abs(dq) == 1)
							if (canmove(p, q, dp, dq, tmp)) {
								field _new = move(p, q, dp, dq, tmp);
								if ((!stable(_new)) && (!STABLE))
									continue;
								if (can.count(_new) == 0) {
//									print(_new);
									can.insert(_new);
									bfs.push_back(make_pair(_new, LEN + 1));
								}
							}
	}
	cout << "-1" << endl;

}

int main() {
	initialize();
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		cerr << i + 1 << endl;
		solve();
	}
	return 0;
}
