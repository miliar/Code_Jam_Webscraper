#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

int n, m;

map<string, int>H;

void solve() {
	H.clear();
	string inp;
	for (int i = 0; i < n; i++) {
		cin >> inp;
		H[inp] = 1;
	}

	int ans = 0;
	for (int i = 0; i < m; i++) {
		cin >> inp;
		string tmp = "";
		for (int i = 0; i < inp.size(); i++) {
			if (inp[i] == '/' && tmp != "") {
				if (!H[tmp]) {
					ans++;
					H[tmp] = 1;
				}
			}
			tmp += inp[i];
		}
		if (!H[inp]) {
			ans++;
			H[inp] = 1;
		}
	}

	printf("%d\n", ans);
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		scanf("%d %d", &n, &m);
		solve();
	}

	return 0;
}