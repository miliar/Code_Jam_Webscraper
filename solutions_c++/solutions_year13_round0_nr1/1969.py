#include<iostream>
#include<queue>
#include<map>
#include<cstring>
#include<utility>
#include<vector>
#include<climits>
#include<iomanip>
#include<set>
#include<algorithm>
#include<string>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<stack>
#include<cstdio>
#include<stdio.h>
using namespace std;
char board[5][5];
bool row(char ch, int r)
{
	for(int i = 0; i < 4; i++)
		if(board[r][i] != ch && board[r][i] != 'T')
			return false;

	return true;
}

bool column(char ch, int c)
{
	for(int i = 0; i < 4; i++)
		if(board[i][c] != ch && board[i][c] != 'T')
			return false;
	return true;
}

bool diagonal1(char ch)
{
	for(int i = 0; i < 4; i++)
		if(board[i][i] != ch && board[i][i] != 'T')
			return false;
	return true;
}

bool diagonal2(char ch)
{
	for(int i = 0; i < 4; i++)
		if(board[3 - i][i] != ch && board[3 - i][i] != 'T')
			return false;
	return true;
}


bool won(char ch)
{
	if(diagonal1(ch) || diagonal2(ch))
		return true;
	for(int i = 0; i < 4; i++)
		if(row(ch, i) || column(ch, i))
			return true;

	return false;
}

bool complete()
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(board[i][j] == '.')
				return false;
	return true;
}
int main()
{
	freopen("output.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++)
				cin >> board[j][k];

		cout << "Case #" << i << ": ";
		if(won('X'))
			cout <<"X won";
		else if(won('O'))
			cout << "O won";
		else if(complete())
			cout << "Draw";
		else
			cout << "Game has not completed";

		cout << endl;

	}
	return 0;
		
}	