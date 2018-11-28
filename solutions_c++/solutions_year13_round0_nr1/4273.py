#include <cstdio>
char s[4][5];
int checkDiagonal()
{
	int ret = 0;
	bool flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][i] != 'O' && s[i][i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag)
		ret = 1;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][i] != 'X' && s[i][i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag)
		ret = 2;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][3 - i] != 'O' && s[i][3 - i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag)
		ret |= 1;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][3 - i] != 'X' && s[i][3 - i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag)
		ret |= 2;
	return ret;
}
int checkRow(int x)
{
	bool flag = 1;
	int ret = 0;
	for (int i = 0; i < 4; ++ i)
		if (s[x][i] != 'O' && s[x][i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag) 
		ret = 1;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[x][i] != 'X' && s[x][i] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag) 
		ret = 2;
	return ret;
}
int checkColumn(int x)
{
	bool flag = 1;
	int ret = 0;
	for (int i = 0; i < 4; ++ i)
		if (s[i][x] != 'O' && s[i][x] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag) 
		ret = 1;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][x] != 'X' && s[i][x] != 'T')
		{
			flag = 0;
			break;
		}
	if (flag) 
		ret = 2;
	return ret;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++ cas)
	{
		for (int i = 0; i < 4; ++ i)
			scanf("%s", s[i]);
		int flag = checkDiagonal();
		for (int i = 0; i < 4; ++ i)
		{
			flag |= checkRow(i);
			flag |= checkColumn(i);
		}
		if (!flag)
		{
			bool tmp = 0;
			for (int i = 0; i < 4; ++ i)
			{
				for (int j = 0; j < 4; ++ j)
					if (s[i][j] == '.')
					{
						tmp = 1;
						break;
					}
				if (tmp)
					break;
			}
			if (!tmp)
				flag = 3;
		}
		printf("Case #%d: ", cas);
		if (!flag)
			puts("Game has not completed");
		else if (flag == 1)
			puts("O won");
		else if (flag == 2)
			puts("X won");
		else
			puts("Draw");
	}
	return 0;
}
		

