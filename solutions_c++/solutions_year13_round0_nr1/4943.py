#include <stdio.h>
#include <string.h>

char map[5][5];

bool isWin_Row(char x, int r)
{
	int i;
	for (i = 0; i < 4; i++)
		if (map[r][i] != x && map[r][i] != 'T')
			return false;
	return true;
}

bool isWin_Col(char x, int r)
{
	int i;
	for (i = 0; i < 4; i++)
		if (map[i][r] != x && map[i][r] != 'T')
			return false;
	return true;
}

bool isWin_Diag(char x)
{
	int i;
	bool f1 = true, f2 = true;
	for (i = 0; i < 4; i++)
		if (map[i][i] != x && map[i][i] != 'T')
		{
			f1 = false;
			break;
		}
	for (i = 0; i < 4; i++)
		if (map[i][3 - i] != x && map[i][3 - i] != 'T')
		{
			f2 = false;
			break;
		}
	return f1 || f2;
}

bool isWin(char x)
{
	int i;
	bool ret = false;
	for (i = 0; i < 4; i++)
	{
		if (isWin_Row(x, i)) return true;
		if (isWin_Col(x, i)) return true;
		if (isWin_Diag(x)) return true;
	}
	return false;
}

int main()
{
	int cas, t, i, j, ret;
	bool isOver;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		ret = 0;
		for (i = 0; i < 4; i++)
			scanf("%s", map[i]);
		if (isWin('X')) ret = 1;
		else if (isWin('O')) ret = 2;
		else
		{
			isOver = true;
			for (i = 0; i < 4; i++) for (j = 0; j < 4; j++)
				if (map[i][j] == '.')
					isOver = false;
		}
		printf("Case #%d: ", cas);
		if (ret == 1)
			printf("X won\n");
		else if (ret == 2)
			printf("O won\n");
		else if (isOver)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
