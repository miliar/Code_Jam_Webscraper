#include<stdio.h>
#include<string.h>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, i, j, dot, Case = 1, finish, x, y;
	char a[8][8];
	scanf("%d", &T);
	while (T--)
	{
		x = 4;
		y = 4;
		dot = 0;
		for (i=0;i<4;i++)
		{
			scanf(" %s", a[i]);
			for (j=0;j<4;j++)
			{
				if(a[i][j] == '.') dot = 1;
				if(a[i][j] == 'T') { x = i; y = j; }
			}
		}
		printf("Case #%d: ", Case++);

		//斜方向
		a[x][y] = 'O';
		if(a[0][0] == 'O' && a[1][1] == 'O' && a[2][2] == 'O' && a[3][3] == 'O' ||
			a[0][3] == 'O' && a[1][2] == 'O' && a[2][1] == 'O' && a[3][0] == 'O')
		{
			printf("O won\n");
			continue;
		}
		a[x][y] = 'X';
		if(a[0][0] == 'X' && a[1][1] == 'X' && a[2][2] == 'X' && a[3][3] == 'X' ||
			a[0][3] == 'X' && a[1][2] == 'X' && a[2][1] == 'X' && a[3][0] == 'X')
		{
			printf("X won\n");
			continue;
		}
		a[x][y] = 'T';

		//横方向
		finish = 0;
		for (i=0;i<4;i++)
		{
			a[x][y] = 'X';
			if(a[i][0] == 'X' && a[i][1] == 'X' && a[i][2] == 'X' && a[i][3] == 'X')
			{
				printf("X won\n");
				finish = 1;
				break;
			}
			a[x][y] = 'O';
			if(a[i][0] == 'O' && a[i][1] == 'O' && a[i][2] == 'O' && a[i][3] == 'O')
			{
				printf("O won\n");
				finish = 1;
				break;
			}
			a[x][y] = 'T';
		}
		if(finish == 1) continue;

		//竖方向
		for (i=0;i<4;i++)
		{
			a[x][y] = 'X';
			if(a[0][i] == 'X' && a[1][i] == 'X' && a[2][i] == 'X' && a[3][i] == 'X')
			{
				printf("X won\n");
				finish = 1;
				break;
			}
			a[x][y] = 'O';
			if(a[0][i] == 'O' && a[1][i] == 'O' && a[2][i] == 'O' && a[3][i] == 'O')
			{
				printf("O won\n");
				finish = 1;
				break;
			}
			a[x][y] = 'T';
		}
		if(finish == 1) continue;

		if(dot == 1) 
			printf("Game has not completed\n");
		else 
			printf("Draw\n");
	}
	return 0;
}