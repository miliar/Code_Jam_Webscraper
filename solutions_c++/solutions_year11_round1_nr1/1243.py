#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int n, pd, pg, ok = 0;
		scanf("%d%d%d", &n, &pd, &pg);
		for(int d = 1; d <= n; d++)
		{
			int wd = d*pd;
			if(wd%100) continue;
			wd /= 100;
			for(int g = 0; g <= 10000; g++)
				if((g+d)*pg >= 100*wd &&
				 !(((g+d)*pg)%100) && ((g+d)*pg-100*wd)/100 <= g)
					ok = 1;
		}
		printf("Case #%d: %s\n", t, ok?"Possible":"Broken");
	}
	return 0;
}
