
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	#define maxn 10005

	int n;
	int d[maxn], l[maxn];
	int maxp[maxn];

	void work()
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i ++)
		{
			scanf("%d%d", &d[i], &l[i]);
			maxp[i] = -1;
		}
		scanf("%d", &d[n]);
		maxp[n] = -1;
		maxp[0] = d[0];
		for (int i = 1; i <= n; i ++)
		{
			for (int j = 0; j < i; j ++)
			{
				if (maxp[j] > l[j])	maxp[j] = l[j];
				if (maxp[j] + d[j] >= d[i])
				{
					int v = d[i] - d[j];
					if (v > maxp[i])
						maxp[i] = v;
				}
				//if (i == 2)	printf("%d\t%d\t%d\t%d\t%d\n", j, maxp[i], d[i], maxp[j], d[j]);
			}
		}
		//for (int i = 0; i <= n; i ++)
		//	printf("%d\t", maxp[i]);
		if (maxp[n] >= 0)	printf("YES\n");
		else	printf("NO\n");
	}

	int main()
	{
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
