#include <stdio.h>

int main()
{
	int tc, tc0;
	scanf("%d", &tc0);
	for (int tc = 1; tc <= tc0; tc++)
	{
		bool ans = true;
		long long n;
		int pd, pg, qd, qg;
		qd = 100;
		scanf("%lld%d%d", &n, &pd, &pg);
		if (pg == 100)
		{
			if (pd == 100)
			{
				ans = true;
			}
			else
			{
				ans = false;
			}
			goto end;
		}
		if (pg == 0)
		{
			if (pd == 0)
			{
				ans = true;
			}
			else
			{
				ans = false;
			}
			goto end;
		}
		if (pd == 100 || pd == 0)
		{
			ans = true;
			goto end;
		}
		for (int i = 2; i <= 100; i++)
		{
			while (1)
			{
				if (pd % i == 0 && qd % i == 0)
				{
					pd /= i;
					qd /= i;
				}
				else
				{
					break;
				}
			}
		}
		if (qd > n)
		{
			ans = false;
			goto end;
		}
end:
		if (ans)
		{
			printf("Case #%d: Possible\n", tc);
		}
		else 
		{
			printf("Case #%d: Broken\n", tc);
		}
	}
	return 0;
}

