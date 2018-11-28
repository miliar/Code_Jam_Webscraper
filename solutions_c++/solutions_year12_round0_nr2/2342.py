#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>

using namespace std;

void solve(int test) {
	int n;
	int s;
	int p;
	cin >> n >> s >> p;
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		int minY = x % 3 == 0 ? x / 3 : x / 3 + 1;
		int maxY = x < 2 ? minY : x % 3 == 2 ? x / 3 + 2 : x / 3 + 1;
		if (minY >= p)
			++ans;
		else if (maxY >= p && s) {
			--s;
			++ans;
		}
	}
	cout << "Case #" << test << ": " << ans << endl;
}

void pre() {
}

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	pre();
	int n;
	cin >> n;
	string tmp;
	getline(cin, tmp);
	for (int i = 1; i <= n; ++i) {
		solve(i);
	}
	return 0;
}
