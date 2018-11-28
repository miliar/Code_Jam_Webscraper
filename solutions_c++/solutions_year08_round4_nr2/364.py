#include <stdio.h>
#include <algorithm>

#define nmax 10001

using namespace std;

int T, a, n, m, gasit;
bool c[nmax * nmax];

int main()
{
	freopen("b.in", "r", stdin);

	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d%d%d", &n, &m, &a);
		gasit = 0;
		for(int i = 1; i <= n; i++)
			if(a % i == 0 && a / i <= m)
			{
				printf("0 0 %d 0 0 %d\n", i, a / i);
				gasit = 1;
				break;
			}
		if(gasit) continue;

		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				c[i * j] = 1;

		for(int x2 = 1; x2 <= n; x2++)
			for(int y1 = 1; y1 <= m; y1++)
				if(c[a + x2 * y1] == 1)
				{
					for(int i = 1; i <= n; i++)
					{
						for(int j = 1; j <= m; j++)
							if(i * j == a + x2 * y1)
							{
								gasit = 1;
								printf("%d %d %d %d %d %d\n", 0, 0, i, y1, x2, j);
								break;
							}
						if(gasit) break;
					}
					break;
				}

		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				c[i * j] = 0;

		if(!gasit) printf("IMPOSSIBLE\n");
	}
}
