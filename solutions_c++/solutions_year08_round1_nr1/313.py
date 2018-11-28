#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>

using namespace std;

const int MAXN = 1000;

int N = 0;
int a[MAXN] = {0};
int b[MAXN] = {0};

bool gt(int a, int b) {
	return a > b;
}

bool ls(int a, int b) {
	return a < b;
}

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", a + i);
	}
	for (int i = 0; i < N; ++i) {
		scanf("%d", b + i);
	}

	stable_sort(a, a + N, gt);
	stable_sort(b, b + N, ls);

	__int64 res = 0;
	for (int i = 0; i < N; ++i) {
		res += (__int64)a[i] * (__int64)b[i];
	}
	printf("%I64d\n", res);
}

int main(void) {
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int T = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
