#include <cstdio>

int h, w;
char str[60][60];

void Scan()
{
	scanf("%d%d", &h, &w);
	for (int i = 0 ; i < h; i++)
		scanf("%s", str[i]);
}

char out[60][60];

void Solve()
{

	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
			out[i][j] = '.';

	for (int i = 0; i < h; i++)
		for (int j = 0; j < w; j++)
		{
			if (str[i][j] == '#')
			{
				if (i == 0 || str[i-1][j] == '.' && j == 0 || str[i][j-1] == '.')
				{
					if (i+1 == h || j+1 == w)
					{
						printf("Impossible\n");
						return;
					}
				}
				if (str[i][j] == '#' && str[i][j+1] == '#' &&
					str[i+1][j] == '#' && str[i+1][j+1] == '#')
				{
					out[i][j] = '/';
					out[i][j+1] = '\\';
					out[i+1][j] = '\\';
					out[i+1][j+1] = '//';
					str[i][j] = '/';
					str[i][j+1] = '\\';
					str[i+1][j] = '\\';
					str[i+1][j+1] = '//';
				}
				else
				{
					printf("Impossible\n");
					return;
				}
			}
		}

	for (int i = 0; i < h; i++){
		for (int j = 0; j < w; j++)
			printf("%c", out[i][j]);
			printf("\n");
		}

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		Scan();
		printf("Case #%d:\n", i+1);
		Solve();
	}
	return 0;
}