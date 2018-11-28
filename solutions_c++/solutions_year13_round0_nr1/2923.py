#include <stdio.h>
#include <string.h>

int board[4][4];

int isWin() {
	int e = 0;
	int c1;
	int c2;
	int p;
	for (int i = 0 ; i < 4 ; i++)
	{
		c1 = c2 = 0;
		for (int j = 0 ; j < 4 ; j++)
		{
			p = board[i][j];
			if (p == 1)
			{
				c1++;
			} 
			else if (p == 2)
			{
				c2++;
			} 
			else if (p == 3)
			{
				c1++;c2++;
			}else
			{
				e++;
			}
		}
		if (c1 == 4)
		{
			return 1;
		}
		if (c2 == 4)
		{
			return 2;
		}
	}

	for (int i = 0 ; i < 4 ; i++)
	{
		c1 = c2 = 0;
		for (int j = 0 ; j < 4 ; j++)
		{
			p = board[j][i];
			if (p == 1)
			{
				c1++;
			} 
			else if (p == 2)
			{
				c2++;
			} 
			else if (p == 3)
			{
				c1++;c2++;
			}else
			{
				e++;
			}
		}
		if (c1 == 4)
		{
			return 1;
		}
		if (c2 == 4)
		{
			return 2;
		}
	}

	c1 = c2 = 0;
	for (int j = 0 ; j < 4 ; j++)
	{
		p = board[j][j];
		if (p == 1)
		{
			c1++;
		} 
		else if (p == 2)
		{
			c2++;
		} 
		else if (p == 3)
		{
			c1++;c2++;
		}else
		{
			e++;
		}
	}
	if (c1 == 4)
	{
		return 1;
	}
	if (c2 == 4)
	{
		return 2;
	}

	c1 = c2 = 0;
	for (int j = 0 ; j < 4 ; j++)
	{
		p = board[3-j][j];
		if (p == 1)
		{
			c1++;
		} 
		else if (p == 2)
		{
			c2++;
		} 
		else if (p == 3)
		{
			c1++;c2++;
		}else
		{
			e++;
		}
	}
	if (c1 == 4)
	{
		return 1;
	}
	if (c2 == 4)
	{
		return 2;
	}

	if (e > 0)
	{
		return 3;
	}

	return 0;
}

int main() {
	int T;
	char c;
	scanf("%d\n", &T);
	for (int k = 1 ; k <= T ; k++)
	{
		memset(board, 0 , sizeof(board));
		for (int i = 0; i < 4 ; i++)
		{
			for (int j = 0 ; j < 4; j++)
			{
				scanf("%c", &c);
				if (c == 'X')
				{
					c = 1;
				} else if (c == 'O')
				{
					c = 2;
				} 
				else if (c == 'T')
				{
					c = 3;
				}
				else
				{
					c = 0;
				}
				board[i][j] = c;
			}
			scanf("\n");
		}
		scanf("\n");
		c = isWin();
		printf("Case #%d: ", k);
		switch(c) {
			case 0:
				printf("Draw\n");
				break;
			case 1:
				printf("X won\n");
				break;
			case 2:
				printf("O won\n");
				break;
			case 3:
				printf("Game has not completed\n");
				break;
		}
	}
	return 0;
}