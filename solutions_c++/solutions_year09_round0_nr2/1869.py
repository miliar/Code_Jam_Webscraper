#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int map[106][106] = {0};
int used[106][106] = {0};
int set[106][106] = {0};
int bucket[10006] = {0};
char sol[106][106] = {0};
int count;

int min(int a[], int n) {
	int m = INT_MAX;
	for (int i=0; i<n; i++)
		if (a[i] < m) m = a[i];
	return m;
}

int flows(int i, int j) {
	int a[4], m;
	if (used[i][j] > 0) {
		return set[i][j];
	}
	a[0] = map[i-1][j];
	a[1] = map[i][j-1];
	a[2] = map[i][j+1];
	a[3] = map[i+1][j];
	m = min(a, 4);
	if (m >= map[i][j]) { // sink
		used[i][j] = 1;
		return set[i][j];
	}
	if (m == a[0]) { // north
		set[i][j] = flows(i-1, j);
	} else if (m == a[1]) { // west
		set[i][j] = flows(i, j-1);
	} else if (m == a[2]) { // east
		set[i][j] = flows(i, j+1);
	} else { // south
		set[i][j] = flows(i+1, j);
	}
	used[i][j];
	return set[i][j];
}

void transform(int m, int n) {
	int region = 0;
	for (int i=1; i<=m; i++) {
		for (int j=1; j<=n; j++) {
			if (bucket[set[i][j]] == 0)
				bucket[set[i][j]] = ++region;
			sol[i][j] = bucket[set[i][j]] + 'a' - 1;
		}
	}
}

int main(void) {
	int t, m, n;
	freopen("D:/C_Prog/Contest/sink0.in", "r", stdin);
	freopen("D:/C_Prog/Contest/sink0.out", "w", stdout);
	scanf("%d", &t);
	for (int z=1; z<=t; z++) {
		count = 0;
		for (int i=0; i<106; i++) {
			for (int j=0; j<106; j++) {
				map[i][j] = used[i][j] = 0;
				set[i][j] = ++count;
			}
		}
		for (int i=0; i<10006; i++) bucket[i] = 0;
		scanf("%d %d", &m, &n);
		for (int i=0; i<=m+1; i++) map[i][0] = map[i][n+1] = INT_MAX;
		for (int i=0; i<=n+1; i++) map[0][i] = map[m+1][i] = INT_MAX;
		for (int i=1; i<=m; i++) 
			for (int j=1; j<=n; j++) 
				scanf("%d", &map[i][j]);
		for (int i=1; i<=m; i++) {
			for (int j=1; j<=n; j++) {
				if (used[i][j] == 0)
					set[i][j] = flows(i, j);
			}
		}
		transform(m, n);
		printf("Case #%d:\n", z);
		for (int i=1; i<=m; i++) {
			for (int j=1; j<=n; j++)
				printf("%c ", sol[i][j]);
			printf("\n");
		}
	}
	return 0;
}
