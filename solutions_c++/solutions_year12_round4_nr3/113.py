
	#include <stdio.h>
	#include <cstdlib>
	#include <algorithm>

	using namespace std;

	#define maxheight 1000000000

	int n, limit[2005];
	int height[2005];

	int solve(int l, int r, int maxh, int lastmaxh, int lastd, int lastrh)
	{
		if (l == r)	return 1;
		//printf("l = %d\tr=%d\tmaxh=%d\tlastmaxh=%d\tlast=%d\n", l, r, maxh, lastmaxh, lastd);
		for (int i = l; i < r; i ++)
		{
			if (limit[i] > r)	return 0;
			if (limit[i] == r)
			{
				if (lastd == -1)
					height[i] = maxh;
				else
				{
					long long delta = lastmaxh - lastrh;
					delta = (delta * (r - i)) / lastd + 1;
					height[i] = lastrh - delta;
					if (height[i] > maxh)	height[i] = maxh;
					if (height[i] < 0)	return 0;
				}
				int limit2 = maxh - 1;
				if (limit2 > height[i])	limit2 = height[i];
				if (solve(l, i, maxh, lastrh, r - i, height[i]) && solve(i + 1, r, limit2, lastmaxh, lastd, lastrh))	return 1;
				else	return 0;
			}
		}
		return 0;
	}

	void work()
	{
		scanf("%d", &n);
		for (int i = 0; i < n - 1; i ++)
		{
			scanf("%d", &limit[i]);
			limit[i] --;
		}
		int lastm = n - 1;
		height[n - 1] = maxheight;
		if (solve(0, n - 1, maxheight, 0, -1, maxheight))
		{
			for (int i = 0; i < n; i ++)
				printf(" %d", height[i]);
			printf("\n");
		}
		else	printf(" Impossible\n");
	}

	int main(int argc, char *argv[])
	{
		freopen("C-small-attempt3.in", "r", stdin);
		freopen("c.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 0; i < t; i ++)
		{
			printf("Case #%d:", i + 1);
			work();
		}
		return 0;
	}
