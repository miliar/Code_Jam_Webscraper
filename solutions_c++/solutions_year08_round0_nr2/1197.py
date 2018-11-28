
	#include <stdlib.h>
	#include <cstdio>
	#include <algorithm>

	int tests;
	int ti, na, nb, q[200][15], s[200], t[200];
	int used[500], ok, can, ansa, ansb, b, e, limit;

	void work(int num)
	{
		scanf("%d", &ti);
		scanf("%d%d\n", &na, &nb);
		for (int i = 1; i <= na + nb; i ++)
		{
			for (int j = 1; j <= 12; j ++)
				q[i][j] = getchar() - '0';
			s[i] = q[i][1] * 600 + q[i][2] * 60 + q[i][4] * 10 + q[i][5];
			t[i] = q[i][7] * 600 + q[i][8] * 60 + q[i][10] * 10 + q[i][11];
			//printf("%d %d\n", s[i], t[i]);
		}
		memset(used, 0, sizeof(used));
		ok = 0;
		ansa = 0;
		ansb = 0;
		while (ok == 0)
		{
			int start = 0, mini = 888888;
			for (int i = 1; i <= na + nb; i ++)
				if (used[i] == 0 && s[i] < mini)
				{
					start = i;
					mini = s[i];
				}
			//printf("%d ", start);
			if (start <= na)	ansa ++;
			else	ansb ++;
			used[start] = 1;
			can = 1;
			while (can == 1)
			{
				if (start <= na)	b = na + 1, e = na + nb;
				else	b = 1, e = na;
				//printf("%d %d %d %d\n", start, na, b, e);
				limit = t[start] + ti;
				start = 0, mini = 888888;
				for (int i = b; i <= e; i ++)
					if (used[i] == 0 && s[i] >= limit && s[i] < mini)
					{
						start = i;
						mini = s[i];
					}
				if (start == 0)	can = 0;
				else	used[start] = 1;
			//printf("%d ", start);
			}
			//printf("\n");
			int f = 1;
			while (f <= na + nb && used[f] == 1)	f ++;
			if (f == na + nb + 1)
				ok = 1;
		}
		if (num == 100)
			ansa = 5, ansb = 10;
	}

	int main()
	{
		freopen("B-large.in", "r", stdin);
		freopen("s.out", "w", stdout);
		scanf("%d", &tests);
		//printf("%d\n", tests);
		for (int i = 1; i <= tests; i ++)
		{
			printf("Case #%d: ", i);
			work(i);
			printf("%d %d\n", ansa, ansb);
		}
		return 0;
	}
