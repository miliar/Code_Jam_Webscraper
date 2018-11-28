#include <stdio.h>
struct node
{
	int g;
	int c;
	int llmin[2];
} a[10000];
int m;
int m1;
int change(int p, int v)
{
	if (p >= m1)
	{
		if (v == a[p].g)
		{
			return 0;
		}else
		{
			return -1;
		}
	}
	if (a[p].llmin[v] > -2) return a[p].llmin[v];
	int t10, t11, t20, t21;

	t11 = change(p * 2 + 1, 1);
	t21 = change(p * 2 + 2, 1);
	t10 = change(p * 2 + 1, 0);
	t20 = change(p * 2 + 2, 0);
	int llmin = -1;
	if (a[p].g)
	{
		if (v == 1)
		{
			if (t11 > -1 && t21 > -1)
			{
				llmin = t11 + t21;
			}
			if (a[p].c)
			{
				if (t10 > -1 && t21 > -1)
				{
					if (llmin == -1 || llmin > t10 + t21 + 1)
						llmin = t10 + t21 + 1;
				}
				if (t11 > -1 && t20 > -1)
				{
					if (llmin == -1 || llmin > t11 + t20  + 1)
						llmin = t11 + t20 + 1;
				}
				if (t11 > -1 && t21 > -1)
				{
					if (llmin == -1 || llmin > t11 + t21 + 1)
						llmin = t11 + t21 + 1;
				}
			}
		}else
		{
			if (t10 > -1 && t20 > -1)
			{
				llmin = t10 + t20;
			}
			if (t10 > -1 && t21 > -1)
			{
				if (llmin == -1 || llmin > t10 + t21)
					llmin = t10 + t21;
			}
			if (t11 > -1 && t20 > -1)
			{
				if (llmin == -1 || llmin > t11 + t20)
					llmin = t11 + t20;
			}
			if (a[p].c)
			{
				if (t10 > -1 && t20 > -1)
				{
					if (llmin == -1 || llmin > t10 + t20 + 1)
						llmin = t10 + t20 + 1;
				}
			}
		}
	}else
	{
		if (v == 1)
		{
			if (t11 > -1 && t21 > -1)
			{
				llmin = t11 + t21;
			}
			if (t11 > -1 && t20 > -1)
			{
				if (llmin == -1 || llmin > t11 + t20)
					llmin = t11 + t20;
			}
			if (t10 > -1 && t21 > -1)
			{
				if (llmin == -1 || llmin > t10 + t21)
					llmin = t10 + t21;
			}
			if (a[p].c)
			{
				if (t11 > -1 && t21 > -1)
				{
					if (llmin == -1 || llmin > t11 + t21 + 1)
						llmin = t11 + t21 + 1;
				}
			}
		}else
		{
			if (t10 > -1 && t20 > -1)
			{
				llmin = t10 + t20;
			}
			if (a[p].c)
			{
				if (t10 > -1 && t20 > -1)
				{
					if (llmin == -1 || llmin > t10 + t20 + 1)
						llmin = t10 + t20 + 1;
				}
				if (t10 > -1 && t21 > -1)
				{
					if (llmin == -1 || llmin > t10 + t21 + 1)
						llmin = t10 + t21 + 1;
				}
				if (t11 > -1 && t20 > -1)
				{
					if (llmin == -1 || llmin > t11 + t20 + 1)
						llmin = t11 + t20 + 1;
				}
			}
		}
	}
	return a[p].llmin[v] = llmin;
}
int main()
{
	int ncase;
	int pp;
	int v, t;
	int i;
	freopen("c:/test.in", "r", stdin);
	freopen("c:/test.out", "w", stdout);
	scanf("%d", &ncase);
	for (pp = 1; pp <= ncase; pp++)
	{
		scanf("%d %d", &m, &v);
		m1 = (m - 1) / 2;
		for (i = 0; i < m1; i++)
		{
			scanf("%d %d", &a[i].g, &a[i].c);
			a[i].llmin[0] = -2;
			a[i].llmin[1] = -2;
		}
		for (i = m1; i < m; i++)
		{
			scanf("%d", &a[i].g);
		}
		printf("Case #%d: ", pp);
		if ((t = change(0, v)) < 0)
		{
			printf("IMPOSSIBLE\n");
		}else
		{
			printf("%d\n", t);
		}
	}
	return 0;
}