
#include <cstdio>

int A[1010];
int B[1010];

int main() {
	
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {

		int N;
		scanf("%d", &N);
		for (int j = 0; j < N; j++) {
			scanf("%d %d", &A[j], &B[j]);
		}

		int num = 0;

		for (int x = 0; x < N; x++) {
			for (int y = x + 1; y < N; y++) {
				if (A[x] < A[y] && B[x] > B[y])
					num++;
				else if (A[x] > A[y] && B[x] < B[y])
					num++;
			}
		}

		printf("Case #%d: %d\n", i+1, num);

	}

}

