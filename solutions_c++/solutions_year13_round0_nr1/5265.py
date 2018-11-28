#include <fstream>
#include <string>
#include <iostream>

using namespace std;

void print(char board[4][4])
{
	for(int i=0; i<4; i++)
	{
		for (int j= 0; j<4; j++)
		{
			cout << board[i][j];
		}
		cout <<endl;
	}
	cout <<endl;
}

int main()
{
	ofstream output;
	ifstream input ("A-small-attempt0.in");
	output.open("A-small-attempt0.out");

	int t;

	input >> t;

	for (int i=0; i<t; i++)
	{
		char board[4][4];
		bool has_empty = false;
		bool x_win = false;
		bool o_win = false;

		int t_row, t_col;
		t_row = -1;
		t_col = -1;
		for (int j=0; j<4; j++)
			for (int k=0; k<4; k++)
			{
				board[j][k] = '.';
			}

		output << "Case #"<<i+1<<": ";

		string str;
		getline(input, str); //get the fisrt dummy line
		for (int j=0; j<4; j++)
		{
			getline(input, str);
			for (int k=0; k < 4; k++)
			{
				board[j][k] = str[k];
				if (str[k] == '.')
				{
					has_empty = true;
				}
				else if (str[k] == 'T')
				{
					t_row = j;
					t_col = k;
				}
			}
		}

//		print(board);

		//detect for "X" win
		if (t_row != -1)
			board[t_row][t_col] = 'X';	
		//detect row for "X" win
		for (int j = 0; j<4; j++)
		{
			int k;
			for (k=0; k<4; k++)
			{
				if (board[j][k] != 'X')
					break;
			}
			if (k == 4)
			{
				x_win = true;
				goto end;
			}
		}

		//detect col for "X" win
		for (int j = 0; j<4; j++)
		{
			int k;
			for (k=0; k<4; k++)
			{
				if (board[k][j] != 'X')
					break;
			}
			if (k == 4)
			{
				x_win = true;
				goto end;
			}
		}

		//detect diagnoal for "X" win
		{
			int j;
			for (j=0; j<4; j++)
			{
				if (board[j][j] != 'X')
					break;
			}
			if (j == 4)
			{
				x_win = true;
				goto end;
			}	
			for (j=0; j<4; j++)
			{
				if (board[3-j][j] != 'X')
					break;
			}
			if (j==4)
			{
				x_win = true;
				goto end;
			}
		}
			
		//detect for "O" win
		if (t_row != -1)
			board[t_row][t_col] = 'O';	
		//detect row for "O" win
		for (int j = 0; j<4; j++)
		{
			int k;
			for (k=0; k<4; k++)
			{
				if (board[j][k] != 'O')
					break;
			}
			if (k == 4)
			{
				o_win = true;
				goto end;
			}
		}

		//detect col for "O" win
		for (int j = 0; j<4; j++)
		{
			int k;
			for (k=0; k<4; k++)
			{
				if (board[k][j] != 'O')
					break;
			}
			if (k == 4)
			{
				o_win = true;
				goto end;
			}
		}

		//detect diagnoal for "O" win
		{
			int j;
			for (j=0; j<4; j++)
			{
				if (board[j][j] != 'O')
					break;
			}
			if (j == 4)
			{
				o_win = true;
				goto end;
			}	
			for (j=0; j<4; j++)
			{
				if (board[3-j][j] != 'O')
					break;
			}
			if (j==4)
			{
				o_win = true;
				goto end;
			}
		}
				
end:
		if (x_win)
		{
			output << "X won";
		}
		else if (o_win)
		{
			output << "O won";
		}
		else if (has_empty)
		{
			output << "Game has not completed";
		}
		else
		{
			output << "Draw";
		}
		output << endl;
	}
	return 0;
}

