#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int solve3(int n, int pd, int pg, int d, int D, int g, int G)
{
	//printf("%d/%d | %d/%d\n", d, D, g, G);

	if(pg*G/100 > G - D + d)
		return -1;
		return (D <= G) && D <= n && D > 0 && G > 0;
}


int solve2(int n, int pd, int pg, int d, int D)
{
	//printf("%d/%d\n", d/100, D);
	for(int g = 0; true; g += 100)
	{
		//printf("g:%d\n", g);
		if((g + d - D*pg) % pg == 0)
		{
			int res = solve3(n, pd, pg, d/100, D, (g+d)/100, (g+d)/pg);
			if(res < 0)
				return 0;
			else if(res)
				return 1;
		}
	}
	return 0;
}

int solve(int n, int pd, int pg)
{
	if((pd == 0 && pg == 0))
		return 1;
	if(pg == 0)
		return 0;

	if(pd == 0)
		return pg != 100;

	int maxd = 100*n;
	for(int d = 100; d <= maxd; d += 100)
		if(d % pd == 0)
			if(solve2(n, pd, pg, d, d/pd))
				return 1;
	return 0;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		int pg, pd, n;
		scanf("%d%d%d", &n, &pd, &pg);

		printf("Case #%d: %s\n", i, solve(n, pd, pg) ? "Possible" : "Broken");
	}
	return 0;
}
