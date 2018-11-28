#include <stdio.h>
#include <string.h>

int P, Q, A[10003][10003], L[10002];

int saiki(int a, int b) {
	if (a == b) return 0;
	if (A[a][b] != -1) return A[a][b];
	int mini = (int)1e+9;
	for (int i = a; i < b; i++) {
		int sum = saiki(a, i) + saiki(i + 1, b);
		sum += L[b + 1] - L[a] - 2;
		if (sum < mini) mini = sum;
	}
	return A[a][b] = mini;
}

int solve() {
	int p, q; scanf("%d%d", &p, &q);
	for (int i = 1; i <= q; i++) scanf("%d", &L[i]);
	L[0] = 0; L[q + 1] = p + 1;
	memset(A, -1, sizeof(A));
	return saiki(0, q);
}

int main() {
	int n; scanf("%d", &n);
	for (int case_x = 1; case_x <= n; case_x++)
	 printf("Case #%d: %d\n", case_x, solve());
	return 0;
}
