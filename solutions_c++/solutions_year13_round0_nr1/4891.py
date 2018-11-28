#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

char a[5][5];

int main()
{
	int t, cas = 1;
	int i, j, k, flag, nx, no, fx, fo;
	scanf("%d", &t);
	while (t --)
	{
		flag = nx = no = 0;
		for (i = 0; i < 4; i ++)
			scanf("%s", &a[i]);
		for (i = 0; i < 4; i ++)
		{
			for (j = 0; j < 4; j ++)
				if (a[i][j] == '.')
				{	flag = 1; break;}
				else if (a[i][j] == 'X')
					nx ++;
				else if (a[i][j] == 'O')
					no ++;
			if (j < 4)
				break;
		}
		printf("Case #%d: ", cas++);
		fx = fo = 0;
		for (i = 0; i < 4; i ++)
		{
			if (a[i][0]==a[i][1] && a[i][1] == a[i][2] && a[i][2] == a[i][3])
			{
				if (a[i][0] == 'X')
					fx = 1;
				else if (a[i][0] == 'O')
					fo = 1;
			}
			if ((a[i][0]==a[i][1] && a[i][1] == a[i][2] && a[i][3] == 'T')
					||(a[i][0]==a[i][1] && a[i][1] == a[i][3] && a[i][2] == 'T')
					||(a[i][0]==a[i][3] && a[i][3] == a[i][2] && a[i][1] == 'T')
					||(a[i][3]==a[i][1] && a[i][1] == a[i][2] && a[i][0] == 'T'))
			{
				if (a[i][0] == 'T')
				{
					if (a[i][1] == 'X') fx = 1;
					else if (a[i][1] == 'O') fo = 1;
				}
				else
				{
					if (a[i][0] == 'X') fx = 1;
					else if (a[i][0] == 'O') fo = 1;
				}
			}
			if (a[0][i]==a[1][i] && a[1][i] == a[2][i] && a[2][i] == a[3][i])
			{
				if (a[0][i] == 'X')
					fx = 1;
				else if (a[0][i] == 'O')
					fo = 1;
			}
			if ((a[0][i]==a[1][i] && a[1][i] == a[2][i] && a[3][i] == 'T')
					||(a[0][i]==a[1][i] && a[1][i] == a[3][i] && a[2][i] == 'T')
					||(a[0][i]==a[3][i] && a[3][i] == a[2][i] && a[1][i] == 'T')
					||(a[3][i]==a[1][i] && a[1][i] == a[2][i] && a[0][i] == 'T'))
			{
				if (a[0][i] == 'T')
				{
					if (a[2][i] == 'X') fx = 1;
					else if (a[2][i] == 'O') fo = 1;
				}
				else
				{
					if (a[0][i] == 'X') fx = 1;
					else if (a[0][i] == 'O') fo = 1;
				}
			}
		}
		if (a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3])
		{
			if (a[0][0] == 'X')	fx = 1;
			else if (a[0][0] == 'O')	fo = 1;
		}
		if (a[0][3]==a[1][2] && a[1][2]==a[2][1] && a[2][1]==a[3][0])
		{
			if (a[0][3] == 'X')	fx = 1;
			else if (a[0][3] == 'O')	fo = 1;
		}
		if ((a[0][0]==a[1][1] && a[1][1] == a[2][2] && a[3][3] == 'T')
				||(a[0][0]==a[1][1] && a[1][1] == a[3][3] && a[2][2] == 'T')
				||(a[0][0]==a[3][3] && a[3][3] == a[2][2] && a[1][1] == 'T')
				||(a[3][3]==a[1][1] && a[1][1] == a[2][2] && a[0][0] == 'T'))
		{
			if (a[0][0] == 'T')
			{
				if (a[2][2] == 'X') fx = 1;
				else if (a[2][2] == 'O') fo = 1;
			}
			else
			{
				if (a[0][0] == 'X') fx = 1;
				else if (a[0][0] == 'O') fo = 1;
			}
		}
		if ((a[0][3]==a[1][2] && a[1][2] == a[2][1] && a[3][0] == 'T')
				||(a[0][3]==a[1][2] && a[1][2] == a[3][0] && a[2][1] == 'T')
				||(a[0][3]==a[3][0] && a[3][0] == a[2][1] && a[1][2] == 'T')
				||(a[3][0]==a[1][2] && a[1][2] == a[2][1] && a[0][3] == 'T'))
		{
			if (a[0][3] == 'T')
			{
				if (a[2][1] == 'X') fx = 1;
				else if (a[2][1] == 'O') fo = 1;
			}
			else
			{
				if (a[0][3] == 'X') fx = 1;
				else if (a[0][3] == 'O') fo = 1;
			}
		}
		if (fx && !fo)
			puts("X won");
		else if (!fx && fo)
			puts("O won");
		else if (fx && fo)
		{
			if (nx <= no)
				puts("X won");
			else puts("O won");
		}
		else if (flag)
			puts("Game has not completed");
		else
			puts("Draw");
	}
	return 0;
}
