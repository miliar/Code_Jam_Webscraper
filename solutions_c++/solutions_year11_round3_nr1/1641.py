#include <cstdio>

int main()
{
	int T, t, i, R, C, j, k;
	bool b, b2;
	char v[51][51];

	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &R);
		scanf("%d", &C);

		for (i = 0; i < R; i++)
		{
			scanf("%s", v[i]);
		}

		b = true;
		while (b)
		{
			b = false;

			for (i = 0; i < R - 1; i++)
			{
				for (j = 0; j < C - 1; j++)
				{
					if (v[i][j] == '#' && v[i][j+1] == '#' &&
						v[i+1][j] == '#' && v[i+1][j+1] == '#')
					{
						v[i][j] = '/';
						v[i][j+1] = '\\';
						v[i+1][j] = '\\';
						v[i+1][j+1] = '/';

						b = true;
					}
				}
			}
		}

		b2 = true;
		for (i = 0; i < R; i++)
		{
			for (j = 0; j < C; j++)
			{
				if (v[i][j] == '#')
				{
					b2 = false;
				}
			}
		}

		if (b2)
		{
			printf("Case #%d:\n", t);
			for (i = 0; i < R; i++)
			{
				for (j = 0; j < C; j++)
				{
					printf("%c", v[i][j]);
				}
				printf("\n");
			}
		}
		else
		{
			printf("Case #%d:\nImpossible\n", t);
		}
	}

	return 0;
}

