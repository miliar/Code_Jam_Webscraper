#include <stdio.h>


int t, i, j, n, l, h;
int sol;
int a[110];


void read() {

	freopen("c.in", "r", stdin);
	freopen("c.out","w",stdout);

	scanf("%d ", &t);

}

void write(int test);

int check(int p) {

	for (int i=0; i<n; ++i) {
		if (a[i] > p) {
			if (a[i] %p !=0)
				return 0;
		} else {
			if (p % a[i] != 0)
				return 0;
		}
	}

	return 1;

}

void solve() {

	for (int test=1; test<=t; ++test) {

		scanf("%d %d %d ", &n, &l, &h);

		for (i=0; i<n; ++i) {
			scanf("%d ", &a[i]);
		}

		sol = -1;

		for (i=l; i<=h; ++i) {
			if (check(i)) {
				sol = i;
				i = h+1;
			}
		}

		write(test);

	}

}


void write(int test) {

	printf("Case #%d: ", test);
	if (sol == -1) {
		printf("NO\n");
	} else {
		printf("%d\n", sol);
	}

}


int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}

