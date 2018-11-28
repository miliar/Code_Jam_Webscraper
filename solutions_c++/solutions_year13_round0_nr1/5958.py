#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char board[4][4];
char win(char *a)
{
	char result;
	int i,index=4;
	for (i=0; i<4; i++)
	{
		if (a[i] == 'T')
		{
			index = i;
		}
	}

	if ( index < 4)
	{
		a[index] = 'X';
		if (a[0]=='X' && a[1]=='X' && a[2]=='X' && a[3]=='X')
		{
			result = 'X';			
		}
		else
		{
			a[index] = 'O';
			if (a[0]=='O' && a[1]=='O' && a[2]=='O' && a[3]=='O')
			{
				result = 'O';
			}else
			{
				result = 0;
			}
		}
		a[index] = 'T';
	}
	else
	{
		if (a[0]=='X' && a[1]=='X' && a[2]=='X' && a[3]=='X')
		{
			result = 'X';
		}
		else if (a[0]=='O' && a[1]=='O' && a[2]=='O' && a[3]=='O')
		{
			result = 'O';
		}
		else
		{
			result = 0;
		}
	}
	return result;
}

int main(void)
{
	ifstream infile("d:\\A-large.in");
	ofstream outfile("d:\\o.out");
	int nDataCount;
	infile >> nDataCount;
	int i,j,k;
	char a[4],result;
	string outp;
	for (k = 0; k < nDataCount; k++)
	{
		infile.ignore();
		infile.getline(board[0],5);
		infile.getline(board[1],5);
		infile.getline(board[2],5);
		infile.getline(board[3],5);
		result = 0;
		for (i = 0; i < 4; i++)
		{
			result = win(board[i]);
			if (result != 0)
			{
				break;
			}
			a[0] = board[0][i];
			a[1] = board[1][i];
			a[2] = board[2][i];
			a[3] = board[3][i];
			result = win(a);
			if (result != 0)
			{
				break;
			}
		}
		if (result == 0)
		{
			a[0] = board[0][0];
			a[1] = board[1][1];
			a[2] = board[2][2];
			a[3] = board[3][3];
			result = win(a);
		}
		if (result == 0)
		{
			a[0] = board[0][3];
			a[1] = board[1][2];
			a[2] = board[2][1];
			a[3] = board[3][0];
			result = win(a);
		}
		if (result == 'X')
		{
			outp = "X won";
		} 
		else if(result == 'O')
		{
			outp = "O won";
		}
		else
		{
			bool empty = false;
			for (i = 0; i < 4; i++)
			{
				for (j = 0; j < 4; j++)
				{
					if (board[i][j] == '.')
					{
						empty = true;
						break;
					}
				}
			}
			if (empty == true)
			{
				outp = "Game has not completed";
			} 
			else
			{
				outp = "Draw";
			}
		}
		outfile << "Case #"<<k+1<<": "<< outp <<endl;
	}
	return 0;
}
