#include <stdio.h>

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);

	int ca;
	scanf("%d" , &ca);
	for (int cas = 1; cas <= ca; cas ++)
	{
		__int64 n;
		int pd , pg;
		int ok = 1;
		scanf("%I64d %d %d" , &n , &pd , &pg);
		if (n < 100)
		{
			ok = 0;
			for (int i = 1; i <= n; i ++)
			{
				for (int j = 0; j <= i; j ++)
					if (j * 100 == pd * i)
					{
						ok = 1; break;
					}
				if (ok) break;
			}
		}
		if (ok == 1)
		{
			if ((pd < 100 && pg == 100) || (pd > 0 && pg == 0)) ok = 0;
		}
		printf("Case #%d: " , cas);
		if (ok) printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}