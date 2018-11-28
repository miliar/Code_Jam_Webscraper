#include <iostream>
#include <string>
using namespace std;

static const int SIZE = 4;
class Board
{
public:
	char b[SIZE][SIZE];

public:
	static string getline()
	{
		string res;
		while (true)
		{
			std::getline(cin, res);
			if (res != "") break;
		}
		return res;
	}

	void input()
	{
		for (int r = 0; r < SIZE; r++)
		{
			string s = getline();
			for (int c = 0; c < SIZE; c++)
				b[r][c] = s[c];
		}
	}
	void debug()
	{
		for (int r = 0; r < SIZE; r++)
		{
			for (int c = 0; c < SIZE; c++)
				cout << b[r][c];
			cout << endl;
		}
	}

	bool isWin(char p)
	{
		bool res;
		//
		// row check
		//
		for (int r = 0; r < SIZE; r++)
		{
			res = true;
			for (int c = 0; c < SIZE; c++)
			{
				if (b[r][c] != p && b[r][c] != 'T')
				{
					res = false;
					break;
				}
			}
			if (res) return true;
		}
		
		//
		// col check
		//
		for (int c = 0; c < SIZE; c++)
		{
			res = true;
			for (int r = 0; r < SIZE; r++)
			{
				if (b[r][c] != p && b[r][c] != 'T')
				{
					res = false;
					break;
				}
			}
			if (res) return true;
		}

		//
		// bias(\) check;
		//
		res = true;
		for (int i = 0; i < SIZE; i++)
		{
			if (b[i][i] != p && b[i][i] != 'T')
			{
				res = false;
				break;
			}
		}
		if (res) return true;

		//
		// bias(/) check;
		//
		res = true;
		for (int i = 0; i < SIZE; i++)
		{
			if (b[i][SIZE - i - 1] != p && b[i][SIZE - i - 1] != 'T')
			{
				res = false;
				break;
			}
		}
		if (res) return true;

		return false;
	}
	bool isDraw()
	{
		for (int r = 0; r < SIZE; r++)
		{
			for (int c = 0; c < SIZE; c++)
				if (b[r][c] == '.') return false;
		}
		return true;
	}
};

void tttt(int t)
{
	Board b;
	string msg;
	b.input();
	if (b.isWin('X'))      msg = "X won";
	else if (b.isWin('O')) msg = "O won";
	else if (b.isDraw())   msg = "Draw";
	else                   msg = "Game has not completed";
	cout << "Case #" << t << ": " << msg << endl;
}
int main()
{
	int T; cin >> T;
	for (int t = 1; t <= T; t++)
		tttt(t);
	return 0;
}