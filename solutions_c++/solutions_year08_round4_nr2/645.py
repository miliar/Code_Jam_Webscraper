#include <stdio.h>
#include <math.h>

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int k, cs;
	scanf("%d", &cs);
	for (k = 0; k < cs; k++) {
		int n, m, a;
		scanf("%d%d%d", &n, &m, &a);
		int u, v, x, y;
		bool flag = false;
		for (u = 0; u <= n; u++) {
			for (v = 0; v <= m; v++) {
				for (x = 0; x <= n; x++) {
					for (y = 0; y <= m; y++) {
						if (abs((u * y - x * v)) == a) {
							printf("Case #%d: 0 0 %d %d %d %d\n", k, u, v, x, y);
							flag = true;
							break;
						}
					}
					if (flag) break;
				}
				if (flag) break;
			}
			if (flag) break;
		}
		if (!flag) {
			printf("Case #%d: IMPOSSIBLE\n", k);
		}
	}

	return 0;
}