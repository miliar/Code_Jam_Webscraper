#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;
#define MAXN 60

int n;
char a[60][60];

void sw(int i, int j) {
	for (int k = 0; k < n; k++) swap(a[i][k], a[j][k]);
}

int solve() {
	int i, j, k, t, ct = 0;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", a[i]);
	}
	for (i = 0; i < n; i++) {
		for (j = i + 1; j < n; j++) if (a[i][j] == '1') break;
		if (j < n) {
			for (k = i + 1; k < n; k++) {
				for (t = i + 1; t < n; t++) if (a[k][t] == '1') break;
				if (t == n) break;
			}
			if (k < n) {
				for (t = k - 1; t >= i; t--) {
					sw(t, t + 1);
					ct++;
				}
			}
		}
	}

	/*
	for (i = n - 1; i >= 0; i--) {
		while (1) {
			for (j = 0; j < i; j++) if (a[j][i] == '1') break;
			if (j < i) {
				for (k = i; k <= n - 1; k++) {
					if (a[k][i] == '0') {
						for (t = i + 1; t < n; t++) if (a[k][t] == '1') break;
						if (t == n) {
							for (t = j; t < k; t++) {
								sw(t, t + 1);
								ct++;
							}
							break;
						}
					}
				}
			}
			else {
				break;
			}
		}
	}
	*/
	return ct;
}

int main() {
	int testcase;

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &testcase);
	for (int TT = 1; TT <= testcase; TT++) {
		printf("Case #%d: %d\n",  TT, solve());
	}

	return 0;
}
