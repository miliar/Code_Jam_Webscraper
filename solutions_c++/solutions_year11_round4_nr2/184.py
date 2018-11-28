#include <stdio.h>
#include <string.h>

int cs, ct, r, c, d;
int a[512][512];
struct {
	long long x, y;
} mass[512][512];
long long g[512][512];
long long max;

int main()
{
//	freopen("b.in", "r", stdin);
	int i, j, k, u, v;
	long long mx, my, m;
	char s[512];
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d%d%d", &r, &c, &d);
		for (i = 1; i <= r; i++) {
			scanf("%s", s);
			for (j = 1; j <= c; j++)
				a[i][j] = (s[j - 1] - '0') + d;
		}

		for (i = 0; i <= r; i++) {
			mass[i][0].x = mass[i][0].y = 0;
			g[i][0] = 0;
		}
		for (j = 0; j <= c; j++) {
			mass[0][j].x = mass[0][j].y = 0;
			g[0][j] = 0;
		}

		for (i = 1; i <= r; i++)
		for (j = 1; j <= c; j++) {
			mass[i][j].x = mass[i - 1][j].x + mass[i][j - 1].x - mass[i - 1][j - 1].x + a[i][j] * i;
			mass[i][j].y = mass[i - 1][j].y + mass[i][j - 1].y - mass[i - 1][j - 1].y + a[i][j] * j;
			g[i][j] = g[i - 1][j] + g[i][j - 1] - g[i - 1][j - 1] + a[i][j];
		}

		max = 0;
		for (i = 1; i <= r; i++)
		for (j = 1; j <= c; j++)
		for (k = 3; i + k - 1 <= r && j + k - 1 <= c; k++) {
			if (k <= max) continue;

			u = i + k - 1;
			v = j + k - 1;

			mx = mass[u][v].x - mass[i - 1][v].x - mass[u][j - 1].x + mass[i - 1][j - 1].x - a[i][j] * i - a[u][v] * u - a[i][v] * i - a[u][j] * u;
			my = mass[u][v].y - mass[i - 1][v].y - mass[u][j - 1].y + mass[i - 1][j - 1].y - a[i][j] * j - a[u][v] * v - a[i][v] * v - a[u][j] * j;
			m = g[u][v] - g[i - 1][v] - g[u][j - 1] + g[i - 1][j - 1] - a[i][j] - a[u][v] - a[i][v] - a[u][j];

			if (mx * 2 == (i * 2 + (k - 1)) * m && my * 2 == (j * 2 + (k - 1)) * m) max = k;
		}

		if (max > 0) printf("Case #%d: %lld\n", cs, max);
		else printf("Case #%d: IMPOSSIBLE\n", cs);
	}
	return 0;
}
