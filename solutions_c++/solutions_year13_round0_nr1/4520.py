#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N 4
char board[5][5];


bool CheckWin(char x)
{
	int i, j, k;
	int row_cnt, col_cnt, dia_cnt;
	//bool flag = false;
	char temp[5][5] = {};

	//check the 10 kind of situations
	for (i=0; i<N; i++)
		for (j=0; j<N; j++)
		{
			if (board[i][j] == 'T') temp[i][j] = x;
			else temp[i][j] = board[i][j];
		}
	
	for (i=0; i<N; i++)
	{
		row_cnt = 0;
		col_cnt = 0;
		for (j=0; j<N; j++)
		{
			if (temp[i][j] == x) row_cnt++;
			if (temp[j][i] == x) col_cnt++;
		}
		if ( (row_cnt==N) || (col_cnt==N)) return true;
	}

	dia_cnt = 0;
	for (i=0; i<N; i++)
		if (temp[i][i] == x) dia_cnt++;
	if (dia_cnt == N) return true;

	dia_cnt = 0;
	for (i=0; i<N; i++)
		if (temp[i][N-1-i] == x) dia_cnt++;
	if (dia_cnt == N) return true;

	return false;
}

int CheckStatus()
{
	int i, j;
	int ans;
	bool hasdot = false;   // if the board hasn't any dot, the status may be (4)not complete (&game not over)
	bool Xwin = false;
	bool Owin = false;

	Xwin = CheckWin('X');
	Owin = CheckWin('O');

	for (i=0; i<N && !hasdot; i++)
		for (j=0; j<N; j++)
			if (board[i][j] == '.')
			{
				hasdot = true;
				break;
			}


	//1: X win  2: O win  3: Draw  4: not completed
	if (Xwin && Owin)
	{
		ans = 3;
	}
	else if (Xwin && !Owin)
	{
		ans = 1;
	}
	else if (!Xwin && Owin)
	{
		ans = 2;
	}
	else // when Xwin==fasle  and  Owin==false
	{
		if (!hasdot) // there are not any empty square
			ans =3;
		else
			ans = 4;
	}

	return ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//=========code segment
	int T;
	scanf("%d", &T);

	int i, j, k;
	int status;
	for (k=0; k<T; k++)
	{
		for (i=0; i<N; i++)
			scanf("%s", board[i]);

		status = CheckStatus(); // board status

		printf("Case #%d: ", k+1);
		switch (status)
		{
			case 1: printf("X won\n");
					break;
			case 2: printf("O won\n");
					break;
			case 3: printf("Draw\n");
					break;
			case 4: printf("Game has not completed\n");
					break;
			default: break;
		}
	}

	//============================
	fclose(stdin);
	fclose(stdout);
	return 0;
}