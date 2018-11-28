#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILE_PREFIX "A-large"

int a[1001][11];
int f[1001];

int search(int i) 
{
	int j;
	
	if ( f[i] ) return 1;
	f[i] = 1;
	for ( j = 1; j <= a[i][0]; j++ ) {
		if ( search(a[i][j]) ) {
			fprintf(stderr, "*%d\n", a[i][j]);
			return 1;
		}
	}
	return 0;
}

int main()
{
	int T, kase;
	int i, j, k, m, n, res;

#ifdef FILE_PREFIX
	freopen(FILE_PREFIX".in", "r", stdin);
	freopen(FILE_PREFIX".out", "w", stdout);
#endif
	scanf("%d", &T);
	for ( kase = 1; kase <= T; kase++ ) {
		scanf("%d", &n);
		for ( i = 1; i <= n; i++ ) {
			scanf("%d", &m);
			a[i][0] = m;
			for ( j = 1; j <= m; j++ ) {
				scanf("%d", &k);
				a[i][j] = k;
			}
		} 
		res = 0;
		for ( i = 1; i <= n; i++ ) {
			memset(f, 0, sizeof(f));
			if ( search(i) ) {
				res = 1;
				break;
			}
		}
		printf("Case #%d: %s\n", kase, res?"Yes":"No");
	}

	fflush(stdout);
	fprintf(stderr, "Done.\n");
	while(1);

	return 0;
}
