#include <stdio.h>
int main()
{
	int t, T, n, i, m, ans;

	freopen("d.txt", "rb", stdin);
	freopen("outd.txt", "wb", stdout);
	scanf("%d", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d", &n);

		ans = 0;
		for (i=1; i<=n; i++)
		{
			scanf("%d", &m);
			if (m!=i)
				ans++;
		}

		printf("Case #%d: %d.00000000\n", t, ans);
	}
	return 0;
}