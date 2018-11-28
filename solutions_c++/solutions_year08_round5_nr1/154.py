#include <iostream>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

const int	dx[4] = {1, 0, -1, 0};
const int	dy[4] = {0, -1, 0, 1};
const int	X_LIMIT = 6000;

int		N, T, L;
int		lower[X_LIMIT + 1], upper[X_LIMIT + 1];
char		S[60];

int	main()
{
	int nCase;
	scanf("%d", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d", &L);

		for (int i = 0; i <= X_LIMIT; ++i) upper[i] = -1, lower[i] = X_LIMIT + 1;

		lower[3000] = upper[3000] = 3000;
		
		int x = 3000, y = 3000, d = 0, area = 0;

		while (L--)
		{
			scanf("%s%d", &S, &T);
			
			if (T <= 10000)
			{
				while (T--)
				{
					for (int i = 0; i < strlen(S); ++i)
					{
						if (S[i] == 'F')
						{
							x += dx[d], y += dy[d];
							area += dx[d] * y;
						}
						else if (S[i] == 'R')
							d = (d + 1) % 4;
						else if (S[i] == 'L')
							d = (d + 3) % 4;

						upper[x] >?= y;
						lower[x] <?= y;
					}
				}
			}	else
			{
				T *= strlen(S);

				if (d & 1)
				{
					y += dy[d] * T;
					upper[x] >?= y;
					lower[x] <?= y;
				}	else
				{
					for (int i = min(x, x + dx[d] * T); i <= max(x, x + dx[d] * T); ++i)
						upper[i] >?= y, lower[i] <?= y;
					x = x + dx[d] * T;
					area += dx[d] * T * y;
				}
			}
		}

		int u = 0, v = 0;
		for (int i = 0; i <= 6000; ++i) 
		{
			if (upper[i] > upper[u]) u = i;
			if (lower[i] < lower[v]) v = i;
		}
		
		for (int i = 6000; i > u; --i) upper[i - 1] >?= upper[i];
		for (int i = 0; i < u; ++i) upper[i + 1] >?= upper[i];
		for (int i = 6000; i > v; --i) lower[i - 1] <?= lower[i];
		for (int i = 0; i < v; ++i) lower[i + 1] <?= lower[i];

		int totalArea = 0;
		for (int i = 0; i < 6000; ++i) 
		{
			int p = max(lower[i], lower[i + 1]);
			int q = min(upper[i], upper[i + 1]);
			if (p <= q) totalArea += q - p;
		}
/*		for (int i = -5; i <= 5; ++i)
			printf("%d : %d %d\n", i, lower[3000 + i], upper[3000 + i]);

		printf("%d %d\n", x, y);
		printf("%d %d\n", totalArea, area);
*/		printf("Case #%d: %d\n", nowCase, totalArea - abs(area));
	}
	return 0;
}
