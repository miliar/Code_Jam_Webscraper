#include <stdio.h>



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++)
	{
		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);

		int used = 0, res = 0;
		for (int i = 1; i <= n; i++)
		{
			int t;
			scanf("%d", &t);

			int k = t/3, l, q;
			l = q = t % 3;
			if (t % 3 == 2)
				l = 1;
			if (t % 3 == 0)
				q = 1;

			if (t == 0)
				l = q = 0;
			if (t == 29)
				l = q = 1;
			if (t == 30)
				l = q = 0;

			if (k + l >= p)
				res++;
			else
			{
				if (k + q >= p && used < s)
				{
					used++;
					res++;
				}
			}
		}
		

		printf("Case #%d: %d\n", testcase, res);
	}


	return 0;
}

