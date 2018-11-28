#include <cstdio>
char pic[50][51];
int main()
{
	int T;
	scanf("%d", &T);
	int r, c;
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i)
		{
			scanf("%s", pic[i]);
		}
		bool imp = false;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (pic[i][j] == '#')
				{
					if (i+1 < r && pic[i+1][j] == '#' &&
						j+1 < c && pic[i][j+1] == '#' &&
						pic[i+1][j+1] == '#')
					{
						pic[i][j] = pic[i+1][j+1] = '/';
						pic[i+1][j] = pic[i][j+1] = '\\';
					}
					else
					{
						imp = true;
						goto print;
					}
				}
			}
		}
print:
		printf("Case #%d:\n", t);
		if (imp)
		{
			printf("Impossible\n");
		}
		else
		{
			for (int i = 0; i < r; ++i)
			{
				puts(pic[i]);
			}
		}
	}
	return 0;
}