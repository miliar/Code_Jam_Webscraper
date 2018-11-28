#include <stdio.h>
#include <memory.h>
char flavor[2001];
struct cus_t
{
	int t;
	int *x0;
	int x1;
}cus[2001];
int total;
bool try_select(int p)
{
	int i;
	for (i = 0; i < cus[p].t; i++)
	{
		if (flavor[cus[p].x0[i]] == -1)
		{
			flavor[cus[p].x0[i]] = 0;
			if (p == total - 1) return true;
			else if (p < total - 1 && try_select(p + 1)) return true;
			flavor[cus[p].x0[i]] = -1;
		}else if (flavor[cus[p].x0[i]] == 0)
		{
			if (p == total - 1) return true;
			else if (p < total - 1 && try_select(p + 1)) return true;
		}
	}
	if (cus[p].x1 > 0)
	{
		if (flavor[cus[p].x1] == -1)
		{
			flavor[cus[p].x1] = 1;
			if (p == total - 1) return true;
			else if (p < total - 1 && try_select(p + 1)) return true;
			flavor[cus[p].x1] = -1;
		}else if (flavor[cus[p].x1] == 1)
		{
			if (p == total - 1) return true;
			else if (p < total - 1 && try_select(p + 1)) return true;
		}
	}
	return false;
}
int main()
{
	int ncase;
	int pcase;
	int n, m;
	int i, j, x, y, t, p;
	bool possible;
	scanf("%d\n", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		total = 0;
		scanf("%d", &n);
		scanf("%d", &m);
		memset(flavor, -1, sizeof(flavor));
		possible = true;
		for (i = 0; i < m; i++)
		{
			scanf("%d", &t);
			if (t == 1)
			{
				scanf("%d %d", &x, &y);
				if (x < 1 || x > n)
				{
					possible = false;
				}else if (flavor[x] == -1)
				{
					flavor[x] = y;
				}else if (flavor[x] != y)
				{
					possible = false;
				}
			}else
			{
				cus[total].x0 = new int[t];
				cus[total].x1 = 0;
				p = 0;
				for (j = 0; j < t; j++)
				{
					scanf("%d %d", &x, &y);
					if (y == 1)
					{
						cus[total].x1 = x;
					}else
					{
						cus[total].x0[p++] = x;
					}
				}
				cus[total].t = p;
				total++;
			}
		}
		if (possible && total > 0)
		{
			possible = try_select(0);
		}
		printf("Case #%d:", pcase);
		if (possible)
		{
			
			for (i = 1; i <= n; i++)
			{	
				printf(" %d", flavor[i] < 0? 0: flavor[i]);
			}
			
		}else
		{
			printf(" IMPOSSIBLE");
		}
		printf("\n");
		for (i = 0; i < total; i++)
		{
			delete[] cus[i].x0;
		}
	}
	return 0;
}
