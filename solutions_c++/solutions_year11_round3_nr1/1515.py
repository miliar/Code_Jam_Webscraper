#include <iostream>

using namespace std;

int main()
{
	int t, r, c;
	bool success;
	char** board;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ":" << endl;
		cin >> r >> c;
		board = new char*[r];
		for(int j = 0; j < r; j++)
		{
			board[j] = new char[c];
			for(int k = 0; k < c; k++)
			{
				cin >> board[j][k];
			}
		}

		success = true;

		for(int j = 0; j < r; j++)
		{
			for(int k = 0; k < c; k++)
			{
				if(board[j][k] == '#')
				{
					if(j < r-1 && k < c-1 && board[j][k+1] == '#' && board[j+1][k] == '#' && board[j+1][k+1] == '#')
					{
						board[j][k] = '/';
						board[j][k+1] = '\\';
						board[j+1][k] = '\\';
						board[j+1][k+1] = '/';
					}
					else
					{
						success = false;
						break;
					}
				}
			}
			if(success == false) {break;}
		}

		if(success)
		{
			for(int j = 0; j < r; j++)
			{
				for(int k = 0; k < c; k++)
				{
					cout << board[j][k];
				}
				cout << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}
	}
}
