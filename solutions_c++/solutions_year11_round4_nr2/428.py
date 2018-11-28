#include <stdio.h>
#include <assert.h>

int g[500][500];
int n, m, d;

bool good (int i, int len, int n) {
    if (len % 2 == 0) {
	return (i + len / 2 <= n);
    }
    if (len % 2 == 1) {
	return (i + len / 2 < n);
    }
}

bool oke (int x, int y, int len) {
    len /= 2;
    int sum = 0;
    for (int i = x - len; i <= x + len - 1; ++i) {
	for (int j = 1; j <= len; ++j) {
	    if ((i != x - len && i != x + len - 1) || (j != len)) {
		sum += j * (g[i][y - j] - g[i][y + j - 1]);
	    }
	}
    }
    if (sum != 0)
	return false;
    sum = 0;
    for (int i = 1; i <= len; ++i) {
	for (int j = y - len; j <= y + len - 1; ++j) {
	    if ((i != len) || (j != y - len && j != y + len - 1)) {
		sum += i * (g[x - i][j] - g[x + i - 1][j]);
	    }
	}
    }
    return sum == 0;
}

bool ok (int x, int y, int len) {
    if (len % 2 == 0) return oke(x, y, len);
    len /= 2;
    int sum = 0;
    for (int i = x - len; i <= x + len; ++i) {
	for (int j = 1; j <= len; ++j) {
	    if ((i != x - len && i != x + len) || (j != len)) {
		sum += j * (g[i][y - j] - g[i][y + j]);
	    }
	}
    }
    if (sum != 0)
	return false;
    sum = 0;
    for (int i = 1; i <= len; ++i) {
	for (int j = y - len; j <= y + len; ++j) {
	    if ((i != len) || (j != y - len && j != y + len)) {
		sum += i * (g[x - i][j] - g[x + i][j]);
	    }
	}
    }
    return sum == 0;
}

int main (void) {
    int T;
    int scanned = scanf("%d", &T);
    FILE *fl = fopen("log", "w");
    for (int currentcase = 1; currentcase <= T; ++currentcase) {
	scanf("%d %d %d", &n, &m, &d);
	for (int i = 0; i < n; ++i) {
	    for (int j = 0; j < m; ++j) {
		while ((g[i][j] = getchar()) == '\n');
		g[i][j] -= '0';
	    }
	}
	for (int len = (n < m) ? n : m; 3 <= len; --len) {
	    for (int i = len / 2; good(i, len, n); ++i) {
		for (int j = len /2; good(j, len, m); ++j) {
		    if (ok(i, j, len)) {
			fprintf(fl, "%d %d\n", i, j);
			printf("Case #%d: %d\n", currentcase, len);
			goto win;
		    }
		}
	    }
	}
	printf("Case #%d: IMPOSSIBLE\n", currentcase);
win:;
    }
    return 0;
}
