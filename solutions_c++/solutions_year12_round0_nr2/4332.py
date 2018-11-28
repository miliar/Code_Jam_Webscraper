#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#pragma comment(linker, "/STACK:16000000")

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 1e9;
const double EPS = 1e-8;
const double PI = 2 * acos(0.);

bool bp[200];
bool bps[200];
bool sr[200];
bool color[200];

void solve() {
	memset(bp, 0, sizeof(bp));
	memset(bps, 0, sizeof(bps));
	memset(sr, 0, sizeof(sr));
	memset(color, 0, sizeof(sr));
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0; i < n; ++i) {
		int a;
		scanf("%d", &a);
		for (int q = 0; q <= 10; ++q) {
			for (int w = max(0, q - 2); w <= min(10, q + 2); ++w) {
				int e = a - q - w;
				if (e >= 0 && abs(e - q) <= 2 && abs(e - w) <= 2) {
					if (abs(e - q) <= 1 && abs(w - q) <= 1 && abs(e - w) <= 1) {
						if (q >= p || w >= p || e >= p)
							bp[i] = 1;
					} else {
						sr[i] = 1;
						if (q >= p || w >= p || e >= p)
							bps[i] = 1;
					}
				}
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (!color[i] && bps[i] && !bp[i]) {
			color[i] = 1;
			if (s > 0) {
				--s;
				++ans;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		if (!color[i] && sr[i] && s > 0 && (!bp[i] || bps[i])) {
			color[i] = 1;
			--s;
			if (bps[i]) {
				++ans;
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		if (!color[i] && sr[i] && s > 0) {
			--s;
			color[i] = 1;
		}
	}

	for (int i = 0; i < n; ++i) {
		if (!color[i] && bp[i]) {
			++ans;
		}
	}

	printf("%d\n", ans);
}

int main() {
#ifdef _DBG1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}