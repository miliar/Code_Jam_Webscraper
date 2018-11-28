#include <stdio.h>
#include <stdlib.h>

int convert(char c) {
	if (c >= '0' && c <= '9') return c - '0';
	return c - 'A' + 10;
}

int validPosition(int map[50][50], int used[50][50], int pi, int pj, int size) {
	int current = map[pi][pj];
	for (int i=0, k=0; i<size; i++, k=!k) {
		if (k == 0 && map[pi+i][pj] != current) return 0;
		if (k == 1 && map[pi+i][pj] == current) return 0;
		int last = !map[pi+i][pj];
		for (int j=0; j<size; j++) {
			int ci = pi + i;
			int cj = pj + j;
			if (used[ci][cj] == 1) return 0;
			if (map[ci][cj] == last) return 0;
			last = map[ci][cj];
		}
	}
	return 1;
}

void setUsedPosition(int map[50][50], int used[50][50], int pi, int pj, int size) {
	for (int i=0; i<size; i++) {
		for (int j=0; j<size; j++) {
			int ci = pi + i;
			int cj = pj + j;
			used[ci][cj] = 1;
		}
	}
}

int main(void) {
	int T;
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small0.out", "wt", stdout);
	scanf("%d", &T);
	for (int C=1; C<=T; C++) {
		int size[50] = {0};
		int count[50] = {0};
		int map[50][50] = {{0}};
		int used[50][50] = {{0}};
		int m, n, h, K;
		char s[50];

		scanf("%d %d", &m, &n);
		for (int i=0; i<m; i++) {
			scanf("%s", s);
			for (int j=0; j<n; j++) {
				h = convert(s[j]);
				int k = 3;
				while (h > 0) {
					int m = h % 2;
					map[i][4*j+k] = m;
					h /= 2;
					k--;
				}
			}
		}

		K = 0;
		for (int q=32; q>1; q--) {
			for (int i=0; i<=m-q; i++) {
				for (int j=0; j<=n-q; j++) {
					if (validPosition(map, used, i, j, q)) {
						size[K] = q;
						count[K]++;
						setUsedPosition(map, used, i, j, q);
					}
				}
			}
			if (count[K] > 0) K++;
		}

		size[K] = 1;
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
				if (used[i][j] == 0) count[K]++;
		if (count[K] > 0) K++;

		printf("Case #%d: %d\n", C, K);
		for (int i=0; i<K; i++) 
			printf("%d %d\n", size[i], count[i]);
	}
	return 0;
}
