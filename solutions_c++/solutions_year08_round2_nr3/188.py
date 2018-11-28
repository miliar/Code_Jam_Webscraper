#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int K, n, p, result[5001];

void solve(int case_number) {
	int i, j;
	for(i=0; i<K; i++) {
		result[i] = 0;
	}
	int position = 0;
	result[0] = 1;
	for(i=2; i<=K; i++) {
		for(j=0; j<i; ) {
			position = (position + 1)%K;
			if(result[position] == 0) {
				j++;
			}
		}
		result[position] = i;
	}
	printf("Case #%d:", case_number);
	scanf("%d",&n);
	for(i=0; i<n; i++) {
		scanf("%d",&p);
		printf(" %d", result[p-1]);
	}
	printf("\n");
}

int main(void) {
	freopen("C-small-attempt2.in", "rt", stdin);
	freopen("C.out", "wt", stdout);

	int i, T;
	scanf("%d",&T);
	for(i=1; i<=T; i++) {
		scanf("%d", &K);
		solve(i);
	}

	return 0;
}