#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	int n, m,  T, t = 1, i, z, j, k, AA, flag;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d%d%d", &n, &m, &AA);
		flag = 0;
		printf("Case #%d:", t ++);
		for (i = 0; i <= n; i ++)
		{
			for (z = 0; z <= n; z ++)
			{
				for (j = 0; j <= m; j ++)
				{
					for (k = 0; k <= m; k ++)
					{
						if (abs(i * k - z * j) == AA)
						{
							flag = 1;
							printf(" 0 0 %d %d %d %d\n", i, j, z, k);
							break;
						}
					}
					if (flag)
						break;
				}
				if (flag )
					break;
			}
			if (flag)
				break;
		}
		if (!flag )
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}
