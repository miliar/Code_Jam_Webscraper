#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int vs[40], wss[40];

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < 40; ++i) wss[i] = vs[i] = -1;
	for(int i = 0; i <= 10; ++i) {
		for(int j = 0; j <= 10; ++j) if(abs(i - j) <= 2) {
			for(int k = 0; k <= 10; ++k) if(abs(i - k) <= 2 && abs(j - k) <= 2) {
				if(abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2) {
					vs[i + j + k] = max(vs[i + j + k], max(i, max(j, k)));
				} else {
					wss[i + j + k] = max(wss[i + j + k], max(i, max(j, k)));
				}
			}
		}
	}
	for(int c = 1; c <= T; ++c) {
		int res = 0;
		int n, s, p;
		cin >> n >> s >> p;
		for(int i = 0; i < n; ++i) {
			int t;
			cin >> t;
			if(wss[t] >= p) ++res;
			else if(vs[t] >= p && s) {
				++res;
				--s;
			}
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
