#include <cstdio>

int main()
{
	int T, t, C, D, N, i, j, k, s, l_size;
	bool b;
	char c[36][4], d[28][3], n[101], l[100];

	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &C);
		for (i = 0; i < C; i++)
		{
			scanf("%s", &c[i]);
		}

		scanf("%d", &D);
		for (i = 0; i < D; i++)
		{
			scanf("%s", &d[i]);
		}

		scanf("%d", &N);
		scanf("%s", n);

		l_size = 0;
		for (i = 0; i < N; i++)
		{
			b= true;

			if (l_size >= 1)
			{
				for (j = 0; (j < C) && b; j++)
				{
					if ((l[l_size-1] == c[j][0] && n[i] == c[j][1]) ||
						(l[l_size-1] == c[j][1] && n[i] == c[j][0]))
					{
						l[l_size-1] = c[j][2];
						b = false;
					}
				}
			}

			if (b && l_size >= 1)
			{
				for (j = 0; (j < l_size) && b; j++)
				{
					for (k = 0; (k < D) && b; k++)
					{
						if ((l[j] == d[k][0] && n[i] == d[k][1]) ||
							(l[j] == d[k][1] && n[i] == d[k][0]))
						{
							l_size = 0;
							b = false;
						}
					}
				}
			}

			if (b)
			{
				l[l_size++] = n[i];
			}
		}

		printf("Case #%d: [", t);
		for (i = 0; i < l_size; i++)
		{
			printf("%c%s", l[i], i < l_size - 1 ? ", " : "");
		}
		printf("]\n");
	}

	return 0;
}
