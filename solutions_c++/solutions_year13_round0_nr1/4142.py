#include <cstdio>
#include <cstring>

char s[6][6];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);

	for (int test = 0; test < t; test++)
	{
		printf("Case #%d: ", test + 1);
		gets(s[0]);
		for (int i = 0; i < 4; i++)
			gets(s[i]);

		bool filled = true, fix;
		char won = 0;
		int tx = 5, ty = 5;

		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (s[i][j] == '.')
					filled = false;
				else
					if (s[i][j] == 'T')
					{
						tx = i;
						ty = j;
					}

		for (int k = 0; k < 2; k++)
		{
			s[tx][ty] = k?'X':'O';
			for (int i = 0; i < 4; i++)
			{
				fix = true;
				if (s[i][0] != s[tx][ty])
					fix = false;
				else
					for (int j = 0; j < 4; j++)
						if (s[i][j] != s[i][0])
							fix = false;
				if (fix)
				{
					won = s[tx][ty];
					break;
				}

				fix = true;
				if (s[0][i] != s[tx][ty])
					fix = false;
				else
					for (int j = 0; j < 4; j++)
						if (s[0][i] != s[j][i])
							fix = false;
				if (fix)
				{
					won = s[tx][ty];
					break;
				}
			}

			fix = true;
			if (s[0][0] != s[tx][ty])
				fix = false;
			else
				for (int i = 0; i < 4; i++)
					if (s[0][0] != s[i][i])
						fix = false;
			if (fix)
			{
				won = s[tx][ty];
				break;
			}
			
			fix = true;
			if (s[0][3] != s[tx][ty])
				fix = false;
			else
				for (int i = 0; i < 4; i++)
					if (s[0][3] != s[i][4-i-1])
						fix = false;

			if (fix)
			{
				won = s[tx][ty];
				break;
			}
		}

		if (won)
			printf("%c won\n", won);
		else
			if (!filled)
				puts("Game has not completed");
			else
				puts("Draw");

	}

	return 0;
}