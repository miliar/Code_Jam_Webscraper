#include <stdio.h>
#include <stdlib.h>

int cmp1(const void *a, const void *b) {
	return *(int*)a - *(int*)b;
}

int cmp2(const void *a, const void *b) {
	return *(int*)b - *(int*)a;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int ZZ;
	scanf("%d", &ZZ);
	for(int zz = 1; zz <= ZZ; zz++) {
		int n, L1[1000], L2[1000];
		int res = 0;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) scanf("%d", &L1[i]);
		for(int i = 0; i < n; i++) scanf("%d", &L2[i]);
		qsort(L1, n, sizeof L1[0], cmp1);
		qsort(L2, n, sizeof L2[0], cmp2);
		for(int i = 0; i < n; i++) {
			res += L1[i]*L2[i];
		}
		printf("Case #%d: %d\n", zz, res);
	}
	return 0;
}