#include <stdio.h>
#include <string.h>

int N, K, A[100][25], B[100][100];

int solve() {
	memset(B, 0, sizeof(B));
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++)
		 scanf("%d", &A[i][j]);
		for (int j = 0; j < i; j++) {
			int touched = 0;
			if (A[i][0] < A[j][0]) {
				for (int k = 0; k < K; k++)
				 if (A[i][k] >= A[j][k]) touched = 1;
			} else if (A[i][0] > A[j][0]) {
				for (int k = 0; k < K; k++)
				 if (A[i][k] <= A[j][k]) touched = 1;
			} else touched = 1;
			B[i][j] = B[j][i] = touched;
		}
	}
	// 最大クリーク
	int mnum = 0;
	for (int i = 0; i < (1 << N); i++) {
		int num = 0, failed = 0;
		for (int j = 0; j < N; j++) if (i & (1 << j)) num++;
		for (int j = 0; j < N; j++) if (i & (1 << j))
		 for (int k = j + 1; k < N; k++) if (i & (1 << k))
		  if (!B[j][k]) failed = 1, j = k = N;
		if (failed) continue;
		if (mnum < num) mnum = num;
	}
	return mnum;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	 printf("Case #%d: %d\n", case_x, solve());
	return 0;
}
