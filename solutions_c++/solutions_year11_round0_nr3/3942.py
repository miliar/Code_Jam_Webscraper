#include <cstdio>
#include <cstring>

using namespace std;

#define NMAX 1024

int a[NMAX];
int b[NMAX];
int t, n;
long max;

void read() {
	int i;

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
}

void solve() {
	int i;
	long x, y, yy;
	int ok;

	max = -1;
	memset(b, 0, (n + 1) * sizeof(b[0]));
	for (b[0] = 1; b[n] < 1;) {
		x = y = yy = ok = 0;
		for (i = 0; i < n; i++) {
			if (b[i] == 1) {
				x ^= a[i];
			}
			else {
				y += a[i];
				yy ^= a[i];
				ok = 1;
			}
		}

		if (x == yy && ok && y > max) {
			max = y;
		}

		b[0]++;
		i = 0;
		while (b[i] > 1) {
			b[i + 1]++;
			b[i] = 0;
			i++;
		}
	}
}

int main() {
	int i;

	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		read();
		solve();

		printf("Case #%d: ", i);
		if (max > 0) {
			printf("%ld\n", max);
		}
		else {
			printf("NO\n");
		}
	}

	return 0;
}


