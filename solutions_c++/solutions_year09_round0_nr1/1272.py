#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define I(c) ((int)((c) - 'a'))

vector<string> a;
int b[20][30];

int main() {
	#ifndef ONLINE_JUDGE
	freopen("solution.in", "rt", stdin);
	freopen("solution.out", "wt", stdout);
	#endif
	int m, n, tests;
	scanf("%d%d%d\n", &m, &n, &tests);
	for (int i = 0; i < n; i++) {
		string s;
		getline(cin, s);
		a.push_back(s);
	}
	for (int test = 1; test <= tests; test++) {
		string s;
		getline(cin, s);
		memset(b, 0, sizeof(b));
		for (int i = 0; i < m; i++) {
			if (s[0] != '(') {
				b[i][I(s[0])] = 1;
				s = s.substr(1);
			} else {
				int x = 1;
				while (s[x] != ')') x++;
				for (int j = 1; j < x; j++) {
					b[i][I(s[j])] = 1;
				}
				s = s.substr(x + 1);
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int good = 1;
			for (int j = 0; j < m; j++) {
				if (!b[j][I(a[i][j])]) {
					good = 0;
					break;
				}
			}
			if (good) ans++;
		}
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
