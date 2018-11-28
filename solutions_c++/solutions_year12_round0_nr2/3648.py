#include <cstdio>
using namespace std;

int main()
{
	int ans, i, n;
	int g, s, t, p, j;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		ans = 0;
		scanf("%d %d %d", &g, &s, &t);
		for (j = 0; j < g; j++)
		{
			scanf("%d", &p);
			if (t == 0)
				ans++;
			else if (p) {
				if ((p >= (t * 3 - 2)))
					ans++;
				else if (s && (p >= (t * 3 - 4)))
				{
					s--;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}