#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int f[2048][16];
int cost[2048];
int M[1024];

int solve() {
	memset(f, 60, sizeof(f));
	int P;
	scanf("%d", &P);
	int n = 1 << P;
	for (int i = 0; i < n; ++i)
		scanf("%d", M + n - 1 - i);
	for (int i = 0; i < n - 1; ++i)
		scanf("%d", cost + n - 2 - i);
	int s = n - 1;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j <= M[i]; ++j)
			f[s+i][j] = 0;
	for (int i = n - 2; i >= 0; --i) {
		for (int j = 0; j <= P; ++j) {
			f[i][j] = min(min(f[i*2+2][j+1] + f[i*2+1][j+1], f[i*2+2][j] + f[i*2+1][j] + cost[i]), f[i][j] );
		}
	}

	return f[0][0];
}

int main() {
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T-- ) {
		printf("Case #%d: %d\n", ++tc, solve());
	}
	return 0;
}
