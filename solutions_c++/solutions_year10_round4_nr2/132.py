#include <cstdio>
#include <algorithm>
using namespace std;
#define IINF ((int)1e9)
int P;
int A[1024], B[1024], M[1024];

int solve() {
	scanf("%d", &P);
	for (int i = 0; i < (1 << P); i++) scanf("%d", &A[i]);
	for (int i = 0; i < (1 << P) - 1; i++) scanf("%d", &B[i]);
	M[0] = 0;
	for (int i = 1; i < (1 << P); i++) M[i] = IINF;
	// DP
	for (int i = 0; i < (1 << P); i++) {
		int m = ~((i - 1) & ~i);
		for (int j = 0; j < (1 << P); j++) {
			M[j & m] = min(M[j], M[j & m]);
			if (j != (j & m)) M[j] = IINF;
		}
		for (int j = 0; j < (1 << P); j++) {
			for (int k = 0; k < P; k++) {
				int ty = (-1 - ((1 << (P - k)) - 1)) & ((1 << P) - 1);
				int tx = i / (2 << k);
				int tt = ty + tx;
				M[j | (1 << k)] = min(M[j | (1 << k)], M[j] + B[tt]);
			}
		}
		for (int j = 0; j < (1 << P); j++) {
			if (__builtin_popcount(j) < P - A[i]) M[j] = IINF;
		}
	}
	int mini = IINF;
	for (int i = 0; i < (1 << P); i++) mini = min(mini, M[i]);
	return mini;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	 printf("Case #%d: %d\n", case_x, solve());
	return 0;
}
