#include <iostream>
#include <algorithm>
using namespace std;

const int n = 4;

bool winch(char ch, char target)
{
	return ch == target || ch == 'T';
}

bool win(string board[], char ch)
{
	for (int i = 0; i < n; i++)
	{
		bool flag = true;
		for (int j = 0; j < n; j++)
			if (!winch(board[i][j], ch))
			{
				flag = false;
				break;
			}
		if (flag)
			return true;
	}
	for (int j = 0; j < n; j++)
	{
		bool flag = true;
		for (int i = 0; i < n; i++)
			if (!winch(board[i][j], ch))
			{
				flag = false;
				break;
			}
		if (flag)
			return true;
	}
	
	for (int i = 0; i <= n; i++)
	{
		if (i == n)
			return true;
		if (!winch(board[i][i], ch))
			break;
	}

	for (int i = 0; i <= n; i++)
	{
		if (i == n)
			return true;
		if (!winch(board[i][n - 1 - i], ch))
			break;
	}
	
	return false;
}

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		string board[n];
		string ans;
		for (int i = 0; i < n; i++)
			cin >> board[i];
		if (win(board, 'X'))
			ans = "X won";
		else if (win(board, 'O'))
			ans = "O won";
		else
		{
			int blank = 0;
			for (int i = 0; i < n; i++)
				blank += count(board[i].begin(), board[i].end(), '.');
			if (blank)
				ans = "Game has not completed";
			else
				ans = "Draw";
		}
		
		cout << "Case #" << caseI << ": " << ans << endl;
	}
	return 0;
}
