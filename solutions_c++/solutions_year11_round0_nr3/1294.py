#include <cstdio>
#include <algorithm>
using namespace std;

int N, cand;
int A[100];

int main() {
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		scanf("%d", &N);

		int sum = 0, xsum = 0;
		for (int i=0; i<N; ++i) {
			scanf("%d", &A[i]);
			sum += A[i];
			xsum ^= A[i];
		}

		printf("Case #%d: ", t + 1);
		if (xsum != 0) printf("NO\n");
		else {
			sort(A, A+N);
			printf("%d\n", sum - A[0]);
		}
	}
	return 0;
}
