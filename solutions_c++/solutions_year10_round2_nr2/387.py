#include <stdio.h>
#include <algorithm>
using namespace std;

int N, K, B, T;
int X[100], V[100], C[100];

int solve() {
	scanf("%d%d%d%d", &N, &K, &B, &T);
	for (int i = 0; i < N; i++) scanf("%d", &X[i]);
	for (int i = 0; i < N; i++) X[i] = B - X[i];
	for (int i = 0; i < N; i++) scanf("%d", &V[i]);
	for (int i = 0; i < N; i++) C[i] = 0;
	reverse(X, X + N);
	reverse(V, V + N);
	int operation = 0;
	for (int i = 0; i < N; i++) {
		if (K == 0) return operation;
		if (X[i] <= T * V[i]) {
			for (int j = 0; j < i; j++) operation += C[j];
			K--;
		} else C[i] = 1;
	}
	if (K == 0) return operation;
	return -1;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int case_x = 1; case_x <= n; case_x++) {
		printf("Case #%d: ", case_x);
		int ret = solve();
		if (ret < 0) printf("IMPOSSIBLE");
		else printf("%d", ret);
		puts("");
	}
	return 0;
}