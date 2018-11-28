#include <stdio.h>

char a[4][4];

char check(char c0, char c1, char c2, char c3)
{
	int r[3] = {0, 0, 0};
	char c[4] = {c0, c1, c2, c3};
	for (int i = 0; i < 4; i++)
		switch (c[i])
		{
			case 'X':
				r[0]++;
				break;
			case 'O':
				r[1]++;
				break;
			case 'T':
				r[2]++;
				break;
		}
	if (r[0] + r[2] == 4)
		return 'X';
	if (r[1] + r[2] == 4)
		return 'O';
	return '.';
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	int lines[10][4][2] = {
		{{0, 0}, {0, 1}, {0, 2}, {0, 3}},
		{{1, 0}, {1, 1}, {1, 2}, {1, 3}},
		{{2, 0}, {2, 1}, {2, 2}, {2, 3}},
		{{3, 0}, {3, 1}, {3, 2}, {3, 3}},
		
		{{0, 0}, {1, 0}, {2, 0}, {3, 0}},
		{{0, 1}, {1, 1}, {2, 1}, {3, 1}},
		{{0, 2}, {1, 2}, {2, 2}, {3, 2}},
		{{0, 3}, {1, 3}, {2, 3}, {3, 3}},

		{{0, 0}, {1, 1}, {2, 2}, {3, 3}},
		{{0, 3}, {1, 2}, {2, 1}, {3, 0}}
	};

	for (int test = 0; test < t; test++)
	{
		bool dot = false;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%c", &a[i][j]);
				if (a[i][j] == '.')
					dot = true;
			}
			scanf("\n");
		}
		scanf("\n");

		bool win = false;
		for (int line = 0; line < 10; line++)
		{
			char res = check(
				a[lines[line][0][0]][lines[line][0][1]],
				a[lines[line][1][0]][lines[line][1][1]],
				a[lines[line][2][0]][lines[line][2][1]],
				a[lines[line][3][0]][lines[line][3][1]]
				);
			if (res != '.')
			{
				win = true;
				printf("Case #%d: %c won\n", test + 1, res);
				break;
			}
		}

		if (! win)
			printf(dot ? "Case #%d: Game has not completed\n" : "Case #%d: Draw\n", test + 1);
	}

	return 0;
}