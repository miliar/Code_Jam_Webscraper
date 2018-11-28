#include <stdio.h>

int i,j,k,p, pc,c,K;
int q[1000005];

int main() {
	scanf("%d", &pc);
	for (c = 1; c <= pc; c++) {
		printf("Case #%d:", c);
		scanf("%d", &K);
		for (i = 0; i <= K; i++) q[i] = 0;
		p = 0;
		for (i = 1; i <= K; i++) {
			for (j = 1; j <= i; j++) {
				do {
					p++; 
					if (p > K) p = 1;
				} while (q[p] != 0);
			}
			q[p] = i;
		}
		scanf("%d", &k);
		for (i = 0; i < k; i++) {
			scanf("%d", &j);
			printf(" %d", q[j]);
		}
		printf("\n");
	}
	return 0;
}
