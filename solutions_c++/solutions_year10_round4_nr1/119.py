#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

int A[60][60], N;

int axis(int d = 0) {
	for (int i = 0; i < N; i++)
	for (int ii = -1; ii <= 1; ii += 2) {
		int j = i * ii;
		int failed = 0;
		for (int y = 0; y < N; y++)
		 for (int x = 0; x < N; x++) {
			int tx = x, ty = y - j;
			swap(tx, ty);
			ty += j;
			if (0 <= tx && tx < N && 0 <= ty && ty < N) {
				if (!d) {
					if (A[x][y] != A[tx][ty]) goto failed;
				} else {
					if (A[N - 1 - x][y] != A[N - 1 - tx][ty]) goto failed;
				}
			}
		}
		return i;
	  failed:
		continue;
	}
}

int solve() {
	scanf("%d", &N);
	int x = 0, y = 0;
	for (int i = 0; i < N * N; i++) {
		scanf("%d", &A[x][y]);
		x--; y++;
		if (N <= y) y = x + 2, x = N - 1;
		if (x < 0) x = y, y = 0;
	}
	int size = N + axis(0) + axis(1);
	/*
	printf("Debug: \n");
	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			printf("%d", A[x][y]);
		}
		puts("");
	}
	puts("");
	*/
	return size * size - N * N;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int i = 1; i <= case_n; i++) {
		printf("Case #%d: ", i);
		printf("%d\n", solve());
	}
	return 0;
}
