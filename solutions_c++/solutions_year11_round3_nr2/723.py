#include <stdio.h>

#define F_MAX 10010

int t, i, j, n, mn, tt, l, c, s;
int a[1010];

void read() {

	freopen("b.in", "r", stdin);
	freopen("b.out","w",stdout);

	scanf("%d ", &t);

}

void write(int test);


int calculate(int x, int y) {

	int s = 0;
	int i, j;

	for (i=1, j=0; i<=n; ++i, ++j) {
		if (j >=c )
			j=0;
		/*if (((i == x || i+1 == x) && (s>=tt)) ||
			((i == y || i+1 == y) && (s>=tt))) {
			s += a[j];
		} else if (((i == x || i+1 == x) && (s<tt)) ||
			((i == y || i+1 == y) && (s<tt)) && (tt-s ) {
*/
		if (((i-1 == x) && (s>=tt)) ||
			((i-1 == y) && (s>=tt))) {
			s += a[j];
		} else if (((i-1 == x) && (s<tt)) ||
			((i-1 == y) && (s<tt)) && (tt-s < a[j])) {
			int tmp = s;
			int tmp2 = (tt-tmp)/2;
			s += (tt-tmp) + (a[j] - tmp2);

		} else {
			s += (a[j] * 2);
		}
	}

	return s;

}


void solve() {

	
	for (int test=1; test<=t; ++test) {

		scanf("%d %d %d %d", &l, &tt, &n, &c);

		mn = 0;
		for (i=0; i<c; ++i) {
			scanf("%d ", &a[i]);
		}

		for (i=1, j=0; i<=n; ++i, ++j) {
			if (j >=c )
				j=0;
			mn += (a[j] * 2);
		}

		if (l == 2) {
		for (i=0; i<n; ++i) {
			for (j=i+1; j<=n; ++j) {
				s = calculate(i, j);
				if (s < mn) {
					mn = s;
				}
			}
		}
		} else if (l == 1) {
			for (i=0; i<=n; ++i) {
				s = calculate(i, i);
				if (s<mn) {
					mn = s;
				}
			}
		}

		write(test);

	}

}


void write(int test) {

	printf("Case #%d: %d\n", test, mn);

}


int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}

