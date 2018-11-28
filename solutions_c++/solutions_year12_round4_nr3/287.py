#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int INF = 1000000000;
const int P[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59};

int T, n;
int a[2001], h[2001];
int dp[2001];

bool check() {
	for (int i = 0; i < n - 1; ++i) {
		if (a[i] <= i) {
			return false;
		}
		for (int j = i + 1; j < a[i]; ++j) {
			if (a[j] > a[i]) {
				return false;
			}
		}
	}
	return true;
}

bool gao() {
	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < n - 1; ++i) {
		if (dp[a[i]] == -1) {
			dp[a[i]] = i;
		}
	}
	memset(h, -1, sizeof(h));
	for (int i = n - 1; i != 0; i = dp[i]) {
		h[i] = INF;
	}
	h[0] = INF;
	for (int i = 0; i < n; ++i) {
		if (h[i] == -1) {
			h[i] = INF - 1;
		}
	}
	for (int i = 0; i < 100000; ++i) {
		vector<int> f(n, 0);
		for (int j = 0; j < n - 1; ++j) {
			f[j] = j + 1;
			for (int k = j + 2; k < n; ++k) {
				long long t = (long long)(k - j) * (h[f[j]] - h[j]) - (long long)(f[j] - j) * (h[k] - h[j]);
				if (t < 0) {
					f[j] = k;
				}
			}
		}
		bool succ = true;
		for (int j = 0; j < n - 1 && succ; ++j) {
			succ = f[j] == a[j];
		}
		if (succ) {
			return true;
		}
		for (int j = 0; j < n; ++j) {
			if (f[j] < a[j] && h[f[j]] != INF) {
				h[f[j]] -= P[f[j]];
			} else if (f[j] > a[j]) {
				if (h[j] == INF && h[f[j]] == INF) {
					continue;
				}
				if (h[j] != INF && h[f[j]] != INF) {
					if (rand() % 2 == 0) {
						h[j] -= P[j];
					} else {
						h[f[j]] -= P[f[j]];
					}
				} else if (h[j] != INF) {
					h[j] -= P[j];
				} else if (h[f[j]] != INF) {
					h[f[j]] -= P[f[j]];
				}
			}
		}
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d", &n);
		for (int i = 0; i < n - 1; ++i) {
			scanf("%d", &a[i]);
			--a[i];
		}
		if (!check() || !gao()) {
			printf("Case #%d: Impossible\n", caseNum);
		} else {
			printf("Case #%d:", caseNum);
			for (int i = 0; i < n; ++i) {
				printf(" %d", h[i]);
			}
			printf("\n");
		}
	}
	return 0;
}
