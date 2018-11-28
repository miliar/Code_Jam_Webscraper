#include <iostream>
#include <cstdio>
using namespace std;

const int maxn = 105;

int main()
{
	int i, t, s, p, n, score[maxn], a, mod, ans, cas = 1, stan;
	
	freopen("B-large.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> t;
	while (t--)
	{
		scanf("%d%d%d", &n, &s, &p);
		for (i = 0; i < n; i++)
			scanf("%d", &score[i]);

		stan = ans = 0;
		for (i = 0; i < n; i++)
		{
			if (score[i] == 0)
			{
				if (p == 0)
					ans++;
				continue;
			}

			mod = score[i] % 3;
			if (mod == 0)
			{
				a = score[i] / 3;
				if (a >= p)
					ans++, stan++;
				else
				{
					a++;
					if (s && a >= p && a <= 10)
					{
						ans++;
						s--;
					}
				}
			}
			else if (mod == 1)
			{
				a = score[i] / 3 + 1;
				if (a >= p)
					ans++;
			}
			else
			{
				a = score[i] / 3 + 1;
				if (a >= p)
					ans++, stan++;
				else
				{
					a++;
					if (s && a >= p && a <= 10)
					{
						ans++;
						s--;
					}
				}
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}

	return 0;
}