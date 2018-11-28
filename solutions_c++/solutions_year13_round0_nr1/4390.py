#include <cstdio>

int t, counter, T_i = 4, T_j = 4;
char in[5][5];

bool check_win(char sign)
{	
	for (int i = 0; i < 4; i++)
		if (
				(in[i][0] == sign && in[i][1] == sign && in[i][2] == sign && in[i][3] == sign)
			  	|| (in[0][i] == sign && in[1][i] == sign && in[2][i] == sign && in[3][i] == sign) 
			)
			return true;
	if ((in[0][0] == sign && in[1][1] == sign && in[2][2] == sign && in[3][3] == sign)
		  	|| (in[0][3] == sign && in[1][2] == sign && in[2][1] == sign && in[3][0] == sign))
		return true;
	return false;
}

bool check_fill()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (in[i][j] == '.')
				return false;
	return true;
}

int check()
{
	/*for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++)
			printf ("%c", in[i][j]);
		printf ("\n");
	}*/

	bool O_win = false, X_win = false;
	in[T_i][T_j] = 'O';
	O_win = check_win('O');
	in[T_i][T_j] = 'X';
	X_win = check_win('X');
	
	if (O_win && X_win)
		return 3;
	if (O_win)
		return 2;
	if (X_win)
		return 1;
	if (check_fill())
		return 3;
	return 4;
}

int main()
{
	scanf("%d\n", &t);
	while(t--)
	{
		counter++;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%c\n", &in[i][j]);
				if (in[i][j] == 'T')
				{
					T_i = i; 
					T_j = j;
				}
			}
			scanf("\n");
		}

		int result = check();
		if (result == 1)
			printf("Case #%d: X won\n", counter);
		else if (result == 2)
			printf("Case #%d: O won\n", counter);
		else if (result == 3)
			printf("Case #%d: Draw\n", counter);
		else
			printf("Case #%d: Game has not completed\n", counter);
		T_i = T_j = 4;
	}

		return 0;
}
