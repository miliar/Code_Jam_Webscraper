#include <stdio.h>

#define N 8

char board[N][N];

bool judge(char w, int r, int c)
{
	int i, j, cnt;
	//row
	cnt = 0;
	i = r; j = c;
	while(j >= 0)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			j--;
			cnt++;
		}
		else break;
	}
	i = r; j = c;
	while(j < 4)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			j++;
			cnt++;
		}
		else break;
	}
	if(cnt == 5) return true;
	//col
	cnt = 0;
	i = r; j = c;
	while(i >= 0)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i--;
			cnt++;
		}
		else break;
	}
	i = r; j = c;
	while(i < 4)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i++;
			cnt++;
		}
		else break;
	}
	if(cnt == 5) return true;
	//dia1
	cnt = 0;
	i = r; j = c;
	while(i >= 0 && j >= 0)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i--;
			j--;
			cnt++;
		}
		else break;
	}
	i = r; j = c;
	while(i < 4 && j < 4)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i++;
			j++;
			cnt++;
		}
		else break;
	}
	if(cnt == 5) return true;
	//dia2
	cnt = 0;
	i = r; j = c;
	while(i >= 0 && j < 4)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i--;
			j++;
			cnt++;
		}
		else break;
	}
	i = r; j = c;
	while(i < 4 && j >= 0)
	{
		if(board[i][j] == w || board[i][j] == 'T')
		{
			i++;
			j--;
			cnt++;
		}
		else break;
	}
	if(cnt == 5) return true;
	return false;
}

int main()
{
	int T, t, i, j;
	bool is_completed = true, is_over = false;
	char winner = '.';
	scanf("%d", &T);
	for(t = 0; t < T; t++)
	{
		for(i = 0; i < 4; i++)
		{
			scanf("%s", board[i]);
		}
		is_completed = true;
		is_over = false;
		for(i = 0; i < 4 && !is_over; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(board[i][j] == '.')
					is_completed = false;
				else if(board[i][j] == 'X' || board[i][j] == 'O')
				{
					if(judge(board[i][j], i, j))
					{
						is_over = true;
						winner = board[i][j];
						break;
					}
				}
			}
		}
		printf("Case #%d: ", t + 1);
		if(is_over)
		{
			printf("%c won\n", winner);
		}
		else
		{
			if(is_completed) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}

	return 0;
}