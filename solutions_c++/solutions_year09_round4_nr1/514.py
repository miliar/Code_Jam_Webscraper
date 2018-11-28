#include <stdio.h>

int S, A[50];

int solve() {
	int cost = 0;
	scanf("%d", &S);
	for (int y = 0; y < S; y++) {
		A[y] = 0;
		for (int x = 0; x < S; x++) {
			char c; scanf(" %c", &c);
			if (c - '0') A[y] = x;
		}
	}
	for (int y = 0; y < S; y++) if (y < A[y]) {
		int fy = y + 1;
		for (; fy < S; fy++) if (A[fy] <= y) break;
		cost += fy - y;
		// printf("%d %d\n", fy, y);
		int n = A[fy];
		for (; y < fy; fy--) A[fy] = A[fy - 1];
		A[y] = n;
	}
	return cost;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	 printf("Case #%d: %d\n", case_x, solve());
	return 0;
}