#include <stdio.h>

char s[5][5];
bool win(char c)
{
	for (int i = 0; i < 4; ++i)
	{
		int j;
		for (j = 0; j < 4; ++j)
			if (s[i][j] != c && s[i][j] != 'T')
				break;
		if (j == 4)
			return true;
	}
	for (int i = 0; i < 4; ++i)
	{
		int j;
		for (j = 0; j < 4; ++j)
			if (s[j][i] != c && s[j][i] != 'T')
				break;
		if (j == 4)
			return true;
	}
	int i;
	for (i = 0; i < 4; ++i)
		if (s[i][i] != c && s[i][i] != 'T')
			break;
	if (i == 4)
		return true;
	for (i = 0; i < 4; ++i)
		if (s[i][3-i] != c && s[i][3-i] != 'T')
			return false;
	return true;
}
bool emptyCells()
{
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (s[i][j] == '.')
				return true;
	return false;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		for (int i = 0; i < 4; ++i)
			scanf("%s", s[i]);
		printf("Case #%d: ", t);
		if (win('X') && win('O'))
			printf("Draw\n");
		else if (win('X'))
			printf("X won\n");
		else if (win('O'))
			printf("O won\n");
		else if (!emptyCells())
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
