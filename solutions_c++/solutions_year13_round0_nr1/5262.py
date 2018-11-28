#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int cases = 0;
	for(int i = 0; i < T; i++)
	{
		cases++;
		vector<vector<char> > board(4);
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				char c;
				cin >> c;
				board[j].push_back(c);
			}
		}
		bool resultx = false, resulto = false, completed = true;
		for(int j = 0; j < 4; j++)
		{
			bool ligne = true;
			bool col = true;
			for(int k = 0; k < 4; k++)
			{
				if((board[j][k] == 'O')||(board[j][k] == '.'))
					ligne = false;
				if((board[k][j] == 'O')||(board[k][j] == '.'))
					col = false;
			}
			if(col || ligne)
				resultx = true;
		}
		for(int j = 0; j < 4; j++)
		{
			bool ligne = true;
			bool col = true;
			for(int k = 0; k < 4; k++)
			{
				if((board[j][k] == 'X')||(board[j][k] == '.'))
					ligne = false;
				if((board[k][j] == 'X')||(board[k][j] == '.'))
					col = false;
			}
			if(col || ligne)
				resulto = true;
		}
		bool diago = true, antidiago = true;
		for(int j = 0; j < 4; j++)
		{
			if((board[j][j] == 'O')||(board[j][j] == '.'))
				diago = false;
			if((board[j][3-j] == 'O')||(board[j][3-j] == '.'))
				antidiago = false;
		}
		if(diago || antidiago)
			resultx = true;
		diago = true; antidiago = true;
		for(int j = 0; j < 4; j++)
		{
			if((board[j][j] == 'X')||(board[j][j] == '.'))
				diago = false;
			if((board[j][3-j] == 'X')||(board[j][3-j] == '.'))
				antidiago = false;
		}
		if(diago || antidiago)
			resulto = true;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(board[j][k] == '.')
					completed = false;
			}
		}
		if(resultx)
			cout << "Case #" << cases << ": X won\n";
		else
		{
			if(resulto)
				cout << "Case #" << cases << ": O won\n";
			else
			{
				if(completed)
					cout << "Case #" << cases << ": Draw\n";
				else
					cout << "Case #" << cases << ": Game has not completed\n";
			}
		}
	}
}
