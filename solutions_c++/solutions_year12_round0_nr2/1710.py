#include <stdio.h>
#include <math.h>
#include <algorithm>

const int normal = 1, surprising = 2;

int solve()
{
	int n, k, s, p, w = 0, C[4] = {0};
	scanf("%d %d %d", &n, &s, &p);
	while (n--)
	{
		scanf("%d", &k);
		int type = 0, ptype = 0;
		for (int x = 0; x <= 10; x++)
			for (int y = 0; y <= 10; y++)
			{
				int z = k - x - y;
				if (z < 0 || z > 10)
					continue;
				int d = std::max(abs(x - y), std::max(abs(x - z), abs(y - z)));
				if (d < 2)
				{
					type |= normal;
					if (std::max(z, std::max(x, y)) >= p)
						ptype |= normal;
				}
				else if (d == 2)
				{
					type |= surprising;
					if (std::max(z, std::max(x, y)) >= p)
						ptype |= surprising;
				}
			}
		if (type == surprising)
		{
			s--;
			if (ptype & surprising)
				w++;
		}
		else if (type == normal)
		{
			if (ptype & normal)
				w++;
		}
		else if (type == (normal | surprising))
			C[ptype]++;
		else
			s = -1000;
	}
	if (s < 0)
		w = 0;
	else if (s <= C[surprising])
		w += s + C[normal] + C[normal | surprising];
	else if (s <= C[surprising] + C[normal | surprising])
		w += C[normal] + C[surprising] + C[normal | surprising];
	else
		w += C[surprising] + C[normal | surprising] + C[normal] - std::max(0, s - C[surprising] - C[normal | surprising] - C[0]);
	return w;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, solve());
}