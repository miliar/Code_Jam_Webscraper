#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 109;
const int INF = 0x3f3f3f3f;

int a[MAXN];
int P, Q;

int dfs(int a[], int n, int L) {
	if (n == 0) return 0;
	if (n == 1) return L - 1;
	int *left, *right;
	left = new int[MAXN];
	right = new int[MAXN];
	
	int i, j, k, min = INF;
	for (i = 0; i < n; ++i) {
		int l, r;
		int len;

		len = 0;
		for (j = 0; j < i; ++j)
			left[j] = a[j];
		len = j;
		l = dfs(left, len, a[i] - 1);

		for (j = i + 1; j < n; ++j)
			right[j - (i + 1)] = a[j] - a[i];
		len = j - (i + 1);
		r = dfs(right, len, L - a[i]);

		if (l + r + L - 1 < min)
			min = l + r + L - 1;
	}
	delete[] left;
	delete[] right;
	return min;
}

int main() {
	freopen("F:\\C-small-attempt0.in", "r", stdin);
	freopen("F:\\C-small-attempt0.out", "w", stdout);
	int i, j, k, cas = 0;
	int T;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &P, &Q);
		for (i = 0; i < Q; ++i)
			scanf("%d", &a[i]);
		sort(a, a + Q);
		printf("Case #%d: %d\n", ++cas, dfs(a, Q, P));
	}
	return 0;
}
