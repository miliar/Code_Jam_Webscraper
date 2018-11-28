#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<algorithm>
#include<sstream>
#include<iomanip>
#include<cstring>
#include<bitset>
#include<fstream>
#include<cmath>
#include<cassert>
#include <stdio.h>
#include<ctype.h>
using namespace std;
char board[4][4];
bool won(char c)
{
	for(int i = 0; i < 4; ++i)
	{
		int co = 0;
		for(int j = 0; j < 4; ++j)
			co += board[i][j] == c || board[i][j] == 'T';
		if(co == 4)
			return true;
	}
	for(int j = 0; j < 4; ++j)
	{
		int co = 0;
		for(int i = 0; i < 4; ++i)
			co += board[i][j] == c || board[i][j] == 'T';
		if(co == 4)
			return true;
	}
	int co = 0;
	for(int i = 0; i < 4; ++i)
		co += board[i][i] == c || board[i][i] == 'T';
	if(co == 4)
		return true;
	co = 0;
	for(int i = 0; i < 4; ++i)
		co += board[i][4 - i - 1] == c || board[i][4 - i - 1] == 'T';
	return co == 4;
}
int main() 
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int ti = 1; ti <= T; ++ti)
	{
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> board[i][j];
		bool ok = true;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				if(board[i][j] == '.')
				{
					ok = false;
					break;
				}
			}
		}
		cout << "Case " << "#" << ti << ": ";
		bool o = won('O');
		bool x = won('X');
		if(x)
			cout << "X won" << endl;
		else if(o)
			cout << "O won" << endl;
		else if(!ok)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
}