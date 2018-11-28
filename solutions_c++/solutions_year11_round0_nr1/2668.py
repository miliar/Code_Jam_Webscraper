#include <stdio.h>

int abs(int a)
{
	if (a<0)
		return -a;
	else
		return a;
}

int main()
{
	char ch;
	int i, j, n, t, T, m, on, bn, to, tb, ans;
	int mv[2][110];

	freopen("1.txt", "rb", stdin);
	freopen("out.txt", "wb", stdout);

	scanf("%d", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d", &n);

		for (i=1; i<=n; i++)
		{
			scanf("%c", &ch);
			while (ch == ' ')
				scanf("%c", &ch);
			scanf("%d", &mv[0][i]);
			if (ch == 'O')
				mv[1][i] = 0;
			else
				mv[1][i] = 1;
		}

		on = 1;
		bn = 1;
		to = 0;
		tb = 0;
		ans = 0;
		for (i=1; i<=n; i++)
		{
			if (mv[1][i] == 0)
			{
				if (abs(mv[0][i] - on) > tb)
				{
					to = to + abs(mv[0][i] - on) - tb + 1;
					ans += abs(mv[0][i] - on) - tb + 1;
					tb = 0;
				}
				else
				{
					to = 1;
					tb = 0;
					ans += 1;
				}
				on = mv[0][i];
			}
			else
			{
				if (abs(mv[0][i] - bn) > to)
				{
					tb = tb + abs(mv[0][i] - bn) - to + 1;
					ans += abs(mv[0][i] - bn) - to + 1;
					to = 0;
				}
				else
				{
					tb = 1;
					to = 0;
					ans += 1;
				}
				bn = mv[0][i];
			}
		}

		printf("Case #%d: %d\n", t, ans);
			
	}

	return 0;
}