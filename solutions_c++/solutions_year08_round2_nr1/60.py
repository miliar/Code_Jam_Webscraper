#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int x[100000], y[100000], a[3][3];
__int64 ct;

__int64 go(int t, int times) {
	__int64 k = a[t/3][t%3], ret = 1;
	int i;
	for (i = 1; i <= times; i++) {
		ret = ret * (k - i + 1) / i;
	}
	return ret;
}

__int64 func(int t1, int t2, int t3) {
	int b[9], i;
	__int64 ret = 1;
	for (i = 0; i < 9; i++) b[i] = 0;
	b[t1]++, b[t2]++, b[t3]++;
	for (i = 0; i < 9; i++) {
		ret *= go(i, b[i]);
	}
	return ret;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int i, j, k;
	int testcases, r, n, A, B, C, D, x0, y0, M;
	scanf("%d", &testcases);
	for (r = 0; r < testcases; r++) {
		printf("Case #%d:", r + 1);
		scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		x[0] = x0;
		y[0] = y0;
		for (i = 1; i < n; i++) {
			x[i] = ((__int64)A * x[i - 1] + B) % M;
			y[i] = ((__int64)C * y[i - 1] + D) % M;
		}
		memset(a, 0, sizeof(a));
		for (i = 0; i < n; i++) {
			a[x[i]%3][y[i]%3]++;
		}
		ct = 0;
		for (i = 0; i < 9; i++) {
			for (j = i; j < 9; j++) {
				for (k = j; k < 9; k++) {
					if ( (i%3 + j%3 + k%3) % 3 != 0) continue;
					if ( (i/3 + j/3 + k/3) % 3 != 0) continue;
					ct += func(i, j, k);
				}
			}
		}
		printf(" %I64d\n", ct);
	}
	return 0;
}
