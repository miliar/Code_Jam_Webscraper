# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <string>

using namespace std;

int kase = 0;

char p[10][8] = {"XXXX", "XXXT", "XXTX", "XTXX", "TXXX", "OOOO", "OOOT", "OOTO", "OTOO", "TOOO"};
char ans[10] = {'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'};

char r[8][8];
int test;

void print(char c)
{
	if (c == 'X') printf("X won\n"); else
	if (c == 'D') printf("Draw\n"); else
	if (c == 'O') printf("O won\n"); else
	if (c == 'G') printf("Game has not completed\n");
}

char checkRow()
{
	for (int i = 0; i < 4; i ++)
	{
		for (int j = 0; j < 10; j ++)
			if (strcmp(r[i], p[j]) == 0) return ans[j];
	}

	return 0;
}

char checkCol()
{
	for (int i = 0; i < 4; i ++)
	{
		char c[6] = {0};

		for (int j = 0; j < 4; j ++) c[j] = r[j][i];

		for (int j = 0; j < 10; j ++)
			if (strcmp(c, p[j]) == 0) return ans[j];
	}

	return 0;
}

char checkDiag1()
{
	char c[6] = {0};

	for (int i = 0; i < 4; i ++)
	{
		c[i] = r[i][i];
	}

	for (int j = 0; j < 10; j ++)
			if (strcmp(c, p[j]) == 0) return ans[j];

	return 0;
}

char checkDiag2()
{
	char c[6] = {0};

	for (int i = 0; i < 4; i ++)
	{
		c[i] = r[i][3 - i];
	}

	// printf("%s\n", c);

	for (int j = 0; j < 10; j ++)
		if (strcmp(c, p[j]) == 0) return ans[j];

	return 0;
}

int main()
{
	// freopen("a.txt", "r", stdin);
	// freopen("b.txt", "w", stdout);

	scanf("%d", &test);

	while (test --)
	{
		printf("Case #%d: ", ++ kase);

		bool emp = 0;

		for (int i = 0; i < 4; i ++)
		{
			scanf("%s", r[i]);
			for (int j = 0; j < 4; j ++)
			{
				if (r[i][j] == '.') emp = 1;
			}
		}

		char c;

		c = checkRow();
		if (c == 0) c = checkCol(); else { print(c); continue; }
		if (c == 0) c = checkDiag1(); else { print(c); continue; }
		if (c == 0) c = checkDiag2(); else { print(c); continue; }
		if (c == 0)
		{
			if (emp) print('G'); else print('D');
		} else
		{
			print(c);
			continue;
		}
	}
}