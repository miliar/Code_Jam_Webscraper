#include <cstdio>

int main()
{
	int cases;
	bool flag;
	scanf("%d", &cases);
	for (int T = 1; T <= cases; T++)
	{
		int i, j, pd, pg;
		long long unsigned  n;
		scanf("%llu %d %d", &n, &pd, &pg);
		flag = false;
		for (i = 1; i <= n && i <=100 && !flag; i++)
		{
			if (!((i * pd)%100))
			{
				int vd = (i*pd)/100, ld = i - vd;
				
				for (j = 0; j <= pg && !flag; j++)
				{
						if ((pg == 0 && pd == 0) || pg != 0 && !(((vd+j)*100)%pg) && (vd+j)*100/pg >= i+j)
						{
							flag = true;
							//printf("%d %d %d\n", vd, j, pg);
						}
				}
			}
		}
		
		if (flag)
			printf("Case #%d: Possible\n", T);
		else
			printf("Case #%d: Broken\n", T);
	}
	return 0;
}