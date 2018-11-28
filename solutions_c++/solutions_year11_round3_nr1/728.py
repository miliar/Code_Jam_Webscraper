#include <stdio.h>


int t, i, j, n, m, solvable;
int a[60][60];


void read() {

	freopen("a.in", "r", stdin);
	freopen("a.out","w",stdout);

	scanf("%d ", &t);

}

void write(int test);

void solve() {

	for (int test=1; test<=t; ++test) {

		scanf("%d %d ", &n, &m);

		int tmp;
		for (i=0; i<n; ++i) {
			for (j=0; j<m; ++j) {
				scanf("%c", &a[i][j]);
			}
			scanf("%c", &tmp);
		}

		solvable = 1;

		for (i=0; i<n && solvable; ++i) {
			for (j=0; j<m && solvable; ++j) {
				if (a[i][j] == '#') {
					if (a[i+1][j] == '#' && a[i+1][j+1] == '#' 
						&& a[i][j+1] == '#' && i<(n-1) && j<(m-1)) {
						a[i][j] = '/';
						a[i+1][j+1] = '/';
						a[i][j+1] = '\\';
						a[i+1][j] = '\\';
					} else {
						solvable = 0;
					}
				}
			}
		}

		write(test);

	}

}


void write(int test) {

	printf("Case #%d:\n", test);
	if (solvable) {
		for (i=0; i<n; ++i) {
			for (j=0; j<m; ++j) {
				printf("%c", a[i][j]);
			}
			printf("\n");
		}
	} else {
		printf("Impossible\n");
	}

}


int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}

