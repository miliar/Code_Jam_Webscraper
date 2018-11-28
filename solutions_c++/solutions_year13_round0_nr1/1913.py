#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int checkdiag(char board[4][4], int i, int j)
{
	char a = board[i][j];
	if(a == '.')
		return 0;
	int k=i-1;
	int l=j-1;
	int count = 1;
	while(k >= 0 && l >= 0)
	{
		if(board[k][l] == a || board[k][l] == 'T')
			count++;
		else
			break;
		k--;
		l--;
	}
	k = i+1;
	l = j+1;
	while(k < 4 && l < 4)
	{
		if(board[k][l] == a || board[k][l] == 'T')
			count++;
		else
			break;
		k++;
		l++;
	}
	return count;
}

int checkdiag2(char board[4][4], int i, int j)
{
	char a = board[i][j];
	if(a == '.')
		return 0;
	int k=i+1;
	int l=j-1;
	int count = 1;
	while(k < 4 && l >= 0)
	{
		if(board[k][l] == a || board[k][l] == 'T')
			count++;
		else
			break;
		k++;
		l--;
	}
	k = i-1;
	l = j+1;
	while(k >= 0 && l < 4)
	{
		if(board[k][l] == a || board[k][l] == 'T')
			count++;
		else
			break;
		k--;
		l++;
	}
	return count;
}

int checkcol(char board[4][4], int i, int j)
{
	char a = board[i][j];
	if(a == '.')
		return 0;
	int k=i-1;
	int count = 1;
	while(k >= 0)
	{
		if(board[k][j] == a || board[k][j] == 'T')
			count++;
		else
			break;
		k--;
	}
	k = i+1;
	while(k < 4)
	{
		if(board[k][j] == a || board[k][j] == 'T')
			count++;
		else
			break;
		k++;
	}
	return count;
}

int checkrow(char board[4][4], int i, int j)
{
	char a = board[i][j];
	if(a == '.')
		return 0;
	int k=j-1;
	int count = 1;
	while(k >= 0)
	{
		if(board[i][k] == a || board[i][k] == 'T')
			count++;
		else
			break;
		k--;
	}
	k = j+1;
	while(k < 4)
	{
		if(board[i][k] == a || board[i][k] == 'T')
			count++;
		else
			break;
		k++;
	}
	return count;
}

string checkboard(char board[4][4])
{
	int maxX = 0;
	int maxO = 0;
	bool full = true;
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(board[i][j] == '.')
				full = false;
			int r = checkrow(board, i, j);
			int c = checkcol(board, i, j);
			int d = checkdiag(board, i, j);
			int d2 = checkdiag2(board, i, j);
			int m = r>c?r:c;
			m = m>d?m:d;
			m = m>d2?m:d2;
			if(board[i][j] == 'X')
				maxX = maxX>m?maxX:m;
			if(board[i][j] == 'O')
				maxO = maxO>m?maxO:m;
		}
	}
	string result("");
	if(maxX == 4 && maxO == 4)
	{
		result = "Draw";
	}
	else if(maxX == 4)
	{
		result = "X won";
	}
	else if(maxO == 4)
	{
		result = "O won";
	}
	else if(full == true)
	{
		result = "Draw";
	}
	else
	{
		result = "Game has not completed";
	}
	return result;
}

void main()
{
	ifstream infile;
	infile.open("input.txt");

	int T = 0;
	infile >> T;
	string tmp;
	getline(infile, tmp);
	string outstr("");
	ofstream outfile;
	outfile.open("output.txt");
	for(int i=0; i<T; i++)
	{
		char board[4][4];
		string line;
		outfile << "Case #" << i+1 << ": ";
		for(int j=0; j<4; j++)
		{
			getline(infile, line);
			for(int k=0; k<4; k++)
			{
				board[j][k] = line[k];
			}
		}
		string result = checkboard(board);
		outfile << result << endl;
		getline(infile, line);
	}

	infile.close();
	outfile.close();
}