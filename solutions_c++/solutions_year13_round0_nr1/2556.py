#include <stdio.h>

int main()
{
	int maxTest;
	scanf("%d", &maxTest);
	for (int testN = 1; testN <= maxTest; testN++)
	{
		char map[4][5];
		int status = 0;
		for (int i = 0; i < 4; i++)
		{
			scanf("%s", map[i]);
		}

		for (int i = 0; i < 4; i++)
		{
			char chk = map[i][0];
			int j = 1;
			if (chk == 'T')
			{
				chk = map[i][1];
				j++;
			}
			for (j = 0; j < 4; j++)
			{
				//printf("%c ", map[i][j]);
				if ((map[i][j] != chk && map[i][j] != 'T') || map[i][j] == '.')
				{
					break;
				}
			}
			if (j == 4)
			{
				if (chk == 'X')
				{
					status = 1;
				}
				else
				{
					status = 2;
				}
			}
		}
		
		for (int i = 0; i < 4; i++)
		{
			char chk = map[0][i];
			int j = 1;
			if (chk == 'T')
			{
				chk = map[1][i];
				j++;
			}
			for (j = 0; j < 4; j++)
			{
				//printf("%c ", map[j][i]);
				if ((map[j][i] != chk && map[j][i] != 'T') || map[j][i] == '.')
				{
					break;
				}
			}
			if (j == 4)
			{
				if (chk == 'X')
				{
					if (status == 2)
					{
						status = 3;
					}
					else
					{
						status = 1;
					}
				}
				else
				{
					if (status == 1)
					{
						status = 3;
					}
					else
					{
						status = 2;
					}
				}
			}
		}
		
		int j = 1;
		char chk = map[0][0];
		if (chk == 'T')
		{
			chk = map[1][1];
			j++;
		}
		for (j = 0; j < 4; j++)
		{
			if ((map[j][j] != chk && map[j][j] != 'T') || map[j][j] == '.')
			{
				break;
			}
		}
		if (j == 4)
		{
			if (chk == 'X')
			{
				if (status == 2)
				{
					status = 3;
				}
				else
				{
					status = 1;
				}
			}
			else
			{
				if (status == 1)
				{
					status = 3;
				}
				else
				{
					status = 2;
				}
			}
		} 

		j = 1;
		chk = map[0][3];
		if (chk == 'T')
		{
			chk = map[j][3 - j];
			j++;
		}
		for (j = 0; j < 4; j++)
		{
			//printf("%c ", map[j][4 - j]);
			if ((map[j][3 - j] != chk && map[j][3 - j] != 'T') || map[j][3 - j] == '.')
			{
				break;
			}
		}
		if (j == 4)
		{
			if (chk == 'X')
			{
				if (status == 2)
				{
					status = 3;
				}
				else
				{
					status = 1;
				}
			}
			else
			{
				if (status == 1)
				{
					status = 3;
				}
				else
				{
					status = 2;
				}
			}
		}

		if (status == 0)
		{
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					if (map[i][j] == '.')
					{
						status = 3;
						i = 4;
						break;
					}
				}
			}
		}
		
		if (status == 1)
		{
			printf("Case #%d: X won\n", testN);
		}
		else if (status == 2)
		{
			printf("Case #%d: O won\n", testN);
		}
		else if (status == 0)
		{
			printf("Case #%d: Draw\n", testN);
		}
		else if (status == 3)
		{
			printf("Case #%d: Game has not completed\n", testN);
		}
	}
}