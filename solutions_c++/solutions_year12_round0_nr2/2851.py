//Google Code Jam B; Dancing With the Googlers;
#include <cstdio>
#include <cstdlib>
#define N 100

int n, s, p, t, x, a, b, i, ans, cases;
bool ns[N + 1], su[N + 1];

int main()
{
//	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (cases = 1; cases <= t; ++cases)
	{
		scanf("%d%d%d", &n, &s, &p);
		for (i = 1; i <= n; ++i) ns[i] = su[i] = 0;
		for (i = 1; i <= n; ++i)
		{
			scanf("%d", &x);
			if (x)
			{
				a = x / 3;
				b = x - a * 3;
				if (b == 1) ns[i] = su[i] = a + 1 >= p;
				else if (b == 2) ns[i] = a + 1 >= p, su[i] = a + 2 >= p;
				else ns[i] = a >= p, su[i] = a + 1 >= p;
			}
			else
				ns[i] = p <= 0;
		}
		for (ans = 0, i = 1; i <= n; ++i)
			if (ns[i]) ++ans;
			else if (su[i] && s) ++ans, --s;
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
