#include <iostream>
#include <cstdio>

using namespace std;

int getState(char c)
{
	if (c == 'O')
		return 0;
	if (c == 'X')
		return 1;
	if (c == 'T')
		return 2;
	if (c == '.')
		return -1;
	return -10;	
}

int checkHorizontal(char b[][5])
{
	int winner=-1;
	for (int i=0;i<4;++i)
	{
		int state = getState(b[i][0]);
		if (state < 0) continue;
		for (int j=1;j<4;++j)
		{
			int temp = getState(b[i][j]);
			if (temp < 0 )
			{
				state = -1;
			}
			else if (temp < 2)
			{
				if (state == 2)
				{
					state = temp;
				}
				else if (state < 2 && state >= 0)
				{
					if (state != temp)
					{
						state = -1;
					}
				}
			}
			else if (temp == 2)
			{
				
			}

		}
		if (state < 0) continue;
		else 
		{
			winner = state;
			break;
		}
	}
	return winner;
}

int checkVertical(char b[][5])
{
	int winner=-1;
	for (int i=0;i<4;++i)
	{
		int state = getState(b[0][i]);
		if (state < 0) continue;
		for (int j=1;j<4;++j)
		{
			int temp = getState(b[j][i]);
			if (temp < 0 )
				state = -1;
			else if (temp < 2)
			{
				if (state == 2)
				{
					state = temp;
				}
				else if (state < 2 && state >= 0)
				{
					if (state != temp)
					{
						state = -1;
					}
				}
			}
			else if (temp == 2)
			{
			}
			//cout << j << ':' << state << ':' << b[i][j] <<  endl;
		}
		if (state < 0) continue;
		else 
		{
			winner = state;
			break;
		}
	}
	return winner;
}

int checkDiagonal(char b[][5])
{
	int winner=-1;
	int state = getState(b[0][0]);
	if (state >= 0)
	{
		for (int i=1;i<4;++i)
		{
			int temp = getState(b[i][i]);
				if (temp < 0 )
					state = -1;
				else if (temp < 2)
				{
					if (state == 2)
					{
						state = temp;
					}
					else if (state < 2 && state >= 0)
					{
						if (state != temp)
						{
							state = -1;
						}
					}
				}
				else if (temp == 2)
				{
				}
		}
		if (state >= 0) winner = state;
	}
	if (winner >= 0) return winner;
	
	state = getState(b[0][3]);
	if (state >= 0)
	{
		for (int i=1;i<4;++i)
		{
			int temp = getState(b[i][3-i]);
				if (temp < 0 )
					state = -1;
				else if (temp < 2)
				{
					if (state == 2)
					{
						state = temp;
					}
					else if (state < 2 && state >= 0)
					{
						if (state != temp)
						{
							state = -1;
						}
					}
				}
				else if (temp == 2)
				{
				}
		}
		if (state >= 0) winner = state;
	}
	
	return winner;
	
}


int main()
{
	int T;
	char board[5][5];
	
	cin >> T;
	for (int i=0;i<T;++i)
	{
		int sum = 0;
		for (int j=0;j<4;++j)
		{
			cin >> board[j];
			for (int k=0;k<4;++k)
			{	
				if (board[j][k] == 'X' || board[j][k]=='O' || board[j][k] == 'T') sum++;
			}
		}
		int winner = checkHorizontal(board);
		cout << "Case #" << i+1 << ": ";
		if (winner >= 0 && winner <2)
		{
			if (winner == 0) cout << "O won\n";
			else if (winner == 1) cout << "X won\n";
		}
		else 
		{
			winner = checkVertical(board);
			if (winner == 0) cout << "O won\n";
			else if (winner == 1) cout << "X won\n";
			else
			{
				winner = checkDiagonal(board);
				if (winner == 0) cout << "O won\n";
				else if (winner == 1) cout << "X won\n";
				else
				{
						if (sum < 16) cout << "Game has not completed\n";
						else cout << "Draw\n";
				}
			}
		}
	}
	return 0;
}