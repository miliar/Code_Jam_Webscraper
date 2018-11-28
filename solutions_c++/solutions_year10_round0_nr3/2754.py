#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int g[1024];

int main() {
	//freopen("input.txt", "r", stdin);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		int R, k, N;
		cin >> R >> k >> N;
		for (int n = 0; n < N; ++n) {
			cin >> g[n];
		}
		int res = 0;
		int cur = 0;
		for (int r = 0; r < R; ++r) {
			int rest = k;
			int curinit = cur;
			while (g[cur] <= rest) {
				res += g[cur];
				rest -= g[cur];
				++cur;
				if (cur == N) {
					cur = 0;
				}
				if (cur == curinit) {
					break;
				}
			}
		}
		printf("%d\n", res);
	}
}
