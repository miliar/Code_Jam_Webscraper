#include <cstdio>
#include <algorithm>
#define MAXS 2000000

int S[MAXS];
int pred[MAXS];
int which[MAXS];

void goback(int n) {
	while(n != 0) {
		printf("%d", which[n]);
		if(pred[n]) {
			printf(" ");
			n = pred[n];
		} else {
			break;
		}
	}
	printf("\n");
}

int main() {
	int T, N, s;
	bool solution;

	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d:\n", i);

		scanf("%d", &N);
		for(int j = 0; j < N; ++j) {
			scanf("%d", &S[j]);
		}

		solution = false;
		std::fill(pred, pred + MAXS, -1);
		pred[0] = 0;
		for(int j = 0; j < N && !solution; ++j) {
			for(int k = S[j]; k < MAXS && !solution; ++k) {
				if(pred[k - S[j]] >= 0 && which[k - S[j]] != S[j]) {
					if(pred[k] >= 0) {
						goback(k);
						printf("%d ", S[j]);
						goback(k - S[j]);
						solution = true;
					} else {
						pred[k] = k - S[j];
						which[k] = S[j];
					}
				}
			}
		}

		if(!solution) {
			printf("Impossible\n");
		}
	}

	return 0;
}
