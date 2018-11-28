#include <stdio.h>
#include <string.h>

int T, cs;
int n, k, b, t, ans;
int x[200], y[200], v[200];
int mark[200];

int main()
{
	int i, j, count;
	scanf("%d", &T);
	for (cs = 1; cs <= T; cs++) {
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for (i = 0; i < n; i++)
			scanf("%d", &v[i]);
		printf("Case #%d: ", cs);
		count = 0;
		memset(mark, 0, sizeof(mark));
		for (i = 0; i < n; i++)
			if (x[i] + v[i] * t >= b) mark[i] = 1;

		ans = 0;
		count = 0;
		for (i = n - 1; i >= 0; i--)
		if (mark[i]) {
			for (j = i + 1; j < n; j++)
				if (!mark[j]) ans++;
			count++;
			if (count == k) break;
		}

		if (count < k) printf("IMPOSSIBLE\n");
			else printf("%d\n", ans);
	}
	return 0;
}
