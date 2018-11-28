
#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int main()
{

	freopen("d:\\cj\\2.in", "r", stdin);
	freopen("d:\\cj\\A-large.out", "w", stdout);

	int l[MAX], r[MAX];

	int t, n, ca = 1, ans;

	scanf("%d", &t);

	while (t--)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &l[i], &r[i]);

		ans = 0;

		for (int i = 0; i < n-1; ++i)
		{
			for (int j = i+1; j < n; ++j)
			{
				if ((l[i] < l[j] && r[i] > r[j]) || (l[i] > l[j] && r[i] < r[j]))
					++ans;
			}
		}

		printf("Case #%d: %d\n", ca++, ans);
	}

	return 0;
}