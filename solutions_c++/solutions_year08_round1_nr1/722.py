/// Windows XP / Dev-C++ 4.9.9.2
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define nsize 800

int a[nsize], b[nsize], m;

int less(const void *a, const void *b) {
	int *aa = (int *)a;
	int *bb = (int *)b;
	return *aa - *bb;
}

int large(const void *a, const void *b) {
	int *aa = (int *)a;
	int *bb = (int *)b;
	return *bb - *aa;
}

int main() {
	//*
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-0.out", "w", stdout);
	//*/
	/*
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//*/	
	
	int n, i;
	long long res;	
	scanf("%d", &n);
	for ( int kase = 1; kase <= n; kase++ ) {
		scanf("%d", &m);
		for ( i = 0; i < m; i++ ) {
			scanf("%d", a+i);
		}
		for ( i = 0; i < m; i++ ) {
			scanf("%d", b+i);
		}
		qsort(a, m, sizeof(int), less);
		qsort(b, m, sizeof(int), large);
		res = 0;
		for ( i = 0; i < m; i++ ) {
			res += a[i]*b[i];
		}
		printf("Case #%d: %lld\n", kase, res);
	}
	return 0;
}
