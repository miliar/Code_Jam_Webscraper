#include <stdio.h>

int a[100][100];
int u[10000];
int r[10000];
char label[10000];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int ufind(int i) {
	return u[i] == i? i : u[i] = ufind(u[i]);
}

void unite(int a, int b) {
	a = ufind(a);
	b = ufind(b);
	if (r[a] < r[b])
		u[a] = b;
	else {
		u[b] = a;
		if (r[a] == r[b])
			++r[a];
	}
}

int main() {
	int tc, n, m;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				scanf("%d", &a[i][j]);
		for (int i=0; i<n*m; ++i) {
			u[i] = i;
			r[i] = 0;
		}
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j) {
				int mina = 10001;
				int bx, by;
				for (int d=0; d<4; ++d) {
					int tx = i + dx[d];
					int ty = j + dy[d];
					if (tx >= 0 && tx < n && ty >= 0 && ty < m && a[tx][ty] < mina) {
						mina = a[tx][ty];
						bx = tx;
						by = ty;
					}
				}
				if (mina < a[i][j])
					unite(i*m + j, bx * m + by);
			}
		char c = 'a';
		printf("Case #%d:\n", scen);
		for (int i=0; i<n; ++i) {
			for (int j=0; j<m; ++j) {
				int t = ufind(i*m + j);
				if (r[t] >= 0) {
					r[t] = -1;
					label[t] = c++;
				}
				if (j) putchar(' ');
				putchar(label[t]);
			}
			putchar('\n');
		}
	}
	return 0;
}
