#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

char b[4][4];
bool full;

bool check(char c, int x, int y)
{
	int ch = 0;
	int i, j;

	for (i = 0; i < 4; i += 1)
	{
		if (b[x][i] == 'T' || b[x][i] == c)
		{
			ch += 1;
		}
	}

	if (ch == 4)
	{
		return true;
	}

	ch = 0;
	for (i = 0; i < 4; i += 1)
	{
		if (b[i][y] == 'T' || b[i][y] == c)
		{
			ch += 1;
		}
	}

	if (ch == 4)
	{
		return true;
	}

	ch = 0;

	if (x + y == 3)
	{
		for (i = 0; i < 4; i += 1)
		{
			for (j = 0; j < 4; j += 1)
			{
				if (i + j == 3)
				{
					if (b[i][j] == 'T' || b[i][j] == c)
					{
						ch += 1;
					}
				}
			}
		}

		if (ch == 4)
			return true;
	}

	if (x == y)
	{
		for (i = 0; i < 4; i += 1)
		{
			for (j = 0; j < 4; j += 1)
			{
				if (!(i-j))
				{
					if (b[i][j] == 'T' || b[i][j] == c)
					{
						ch += 1;
					}
				}
			}
		}

		if (ch == 4)
			return true;
	}

	return false;

}

int main()
{
	int test, count = 1, i, j, k;
	scanf("%d", &test);

	for (i = 0; i < test; i += 1)
	{
		memset(b, 0, sizeof(b));

		for (j = 0; j < 4; j += 1)
		{
			scanf("%s", b[j]);
		}
	

		string winner = "Draw";
		full = true;

		for (j = 0; j < 4; j += 1)
		{
			for (k = 0; k < 4; k += 1)
			{
				if (b[j][k] == '.')
					full = false;
				if (b[j][k] == 'X' || b[j][k] == 'O')
				{
					bool ch = check(b[j][k], j, k);

					if (ch)
					{
						winner = "";
						winner += b[j][k];
						break;
					}
				}
			}
		}

		printf("Case #%d: ", count++);


		if (winner == "X" || winner == "O")
			printf("%s won\n", winner.c_str());

		if (winner == "Draw")
		{
			if (full) puts("Draw");
			else puts("Game has not completed");
		}

	}

	return 0;
}
