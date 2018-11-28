#include <stdio.h>

int candies[100];
int N;
int maxRes;

void doit(int lev, int s, int p, int sact, int pact) {
	if (lev == N) {
		if (sact && pact && s == p) {
			if (pact > sact) sact = pact;
			if (maxRes < sact) maxRes = sact;
		}
		return;
	}
	doit(lev+1, s ^ candies[lev], p, sact + candies[lev], pact);
	doit(lev+1, s, p ^ candies[lev], sact, pact + candies[lev]);
}

int main() {
	int ntc, tc;
	int i, j, k;
	scanf("%d", &ntc);
	for (tc = 1; tc <= ntc; tc++) {
		scanf("%d", &N);
		for (i = 0; i < N; i++) scanf("%d", &candies[i]);
		maxRes = -1;
		doit(0, 0, 0, 0, 0);
		if (maxRes == -1) 
			printf("Case #%d: NO\n", tc);
		else
			printf("Case #%d: %d\n", tc, maxRes);
	}
	return 0;
}

