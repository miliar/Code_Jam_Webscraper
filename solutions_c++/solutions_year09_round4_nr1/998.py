#include <cstdio>

using namespace std;

char mtx[45][45];
int a[45];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int nCase, n;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf("%d", &n);
		for (int r = 0; r < n; r++) scanf(" %s", mtx[r]);
		//for (int r = 0; r < n; r++) printf("%s\n", mtx[r]);
		for (int c, r = 0; r < n; r++) {
			//printf("ok\n");
			c = n - 1;
			while (c >= 0 && mtx[r][c] == '0') c--;
			a[r] = c;
		}

		int cnt = 0;
		for (int i, r = 0; r < n; r++) {
			//printf("ok\n");
			if (a[r] <= r) continue;
			for (i = r + 1; i < n && a[i] > r; i++);
			int b = a[i];
			for (int j = i; j > r; a[j] = a[j - 1], j--);
			a[r] = b;
			cnt += i - r;
		}

		printf("Case #%d: %d\n", t, cnt);
	}

	return 0;
}
