#include <iostream>
#include <string>
#include <vector>

using namespace std;
char check(string line)
{
	int X = 0, O = 0, T = 0;
	for (int i = 0; i < line.length(); ++i)
	{
		if (line[i] == 'X')
			++X;
		if(line[i] == 'O')
			++O;
		if(line[i] == 'T')
			++T;
	}
	if(X == 4 || (X == 3 && T == 1))
	{
		return 'X';
	}
	if(O == 4 || (O == 3 && T == 1))
	{
		return 'O';
	}
	if(X + O + T != 4)
	{
		return '.';
	}
	return '*';
}
string solve()
{
	vector<string> board(4);
	for (int i = 0; i < 4; ++i)
	{
		cin >> board[i];
	}

	char ans = '*';
	for (int i = 0; i < 4; ++i)
	{
		char res = check(board[i]);
		if(res == 'X' || res == 'O')
		{
			ans = res;
			break;
		} else if(res == '.') 
		{
			ans = res;
		}
		string col = "....";
		for (int j = 0; j < 4; ++j)
		{
			col[j] = board[j][i];
		}
		res = check(col);
		if(res == 'X' || res == 'O')
		{
			ans = res;
			break;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	string diag1 = "....";
	string diag2 = "....";
	for (int i = 0; i < 4; ++i)
	{
		diag1[i] = board[i][i];
		diag2[i] = board[i][3 - i];
	}
	if(ans != 'X' && ans != 'O')
	{
		char res = check(diag1);
		if (res == 'X' || res == 'O')
		{
			ans = res;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	if(ans != 'X' && ans != 'O')
	{
		char res = check(diag2);
		if (res == 'X' || res == 'O')
		{
			ans = res;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	if (ans == '.') {
		return "Game has not completed";
	} else if(ans == '*')
	{
		return "Draw";
	} else if(ans == 'X')
	{
		return "X won";
	} else
	{
		return "O won";
	}
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt.", "w", stdout);
	int t; cin >> t;
	for (int test = 0; test < t; ++test)
	{
		cout << "Case #" << test + 1 << ": " << solve() << endl;
	}
}