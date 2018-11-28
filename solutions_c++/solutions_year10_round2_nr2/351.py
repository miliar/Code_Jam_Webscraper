#include <cstdio>

int x[50], v[50];
bool vv[50];

int main()
{
	int T;
	scanf("%d", &T);
	for (int idx = 1; idx <= T; ++idx)
	{
		printf("Case #%d: ", idx);
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", x+i);
		}
		int vvv = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", v+i);
			if (b - x[i] > v[i] * t) // too slow
			{
				vv[i] = false;
			}
			else
			{
				vv[i] = true;
				++vvv;
			}
		}
		if (k == 0)
		{
			printf("0\n");
			continue;
		}
		else if (k > vvv)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		int res = 0;
		int ok = 0;
		for (int i = n-1; i >= 0 && ok != k; --i)
		{
			if (!vv[i])
			{
				res += k - ok;
			}
			else
			{
				++ok;
			}
		}
		printf("%d\n", res);
	}
	return 0;
}