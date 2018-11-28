#include <vector>
#include <stdio.h>

static void runTest() {
	int N, K, B, T;
	scanf("%d%d%d%d", &N, &K, &B, &T);
	std::vector<int> X(N), V(N);
	for (int i=0; i<N; i++) {
		int x;
		scanf("%d", &x);
		X[i] = x;
	}
	for (int i=0; i<N; i++) {
		int x;
		scanf("%d", &x);
		V[i] = x;
	}
	int lateCount = 0;
	int res = 0;
	int count = 0;
	for (int i=N-1; i>=0; i--) {
		bool late = X[i]+V[i]*T < B;
		if (late)
			lateCount++;
		else {
			res += lateCount;
			count++;
			if (count>=K)
				break;
		}
	}
	if (count<K)
		puts("IMPOSSIBLE");
	else
		printf("%d\n", res);
}

int main() {
	int C;
	scanf("%d", &C);
	for (int i=0; i<C; i++) {
		printf("Case #%d: ", i+1);
		runTest();
	}
	return 0;
}

