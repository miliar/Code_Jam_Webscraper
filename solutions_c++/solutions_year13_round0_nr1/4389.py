#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>
using namespace std;
char board[4][4];
bool checkWin(char player)
{
	for (int i = 0; i < 4 ; i++)
	{
		if((board[i][0]==player||board[i][0]=='T')&&(board[i][1]==player||board[i][1]=='T')
			&&(board[i][2]==player||board[i][2]=='T')&&(board[i][3]==player||board[i][3]=='T'))
			return true;
		if((board[0][i]==player||board[0][i]=='T')&&(board[1][i]==player||board[1][i]=='T')
			&&(board[2][i]==player||board[2][i]=='T')&&(board[3][i]==player||board[3][i]=='T'))
			return true;
	}
	if((board[0][0]==player||board[0][0]=='T')&&(board[1][1]==player||board[1][1]=='T')
		&&(board[2][2]==player||board[2][2]=='T')&&(board[3][3]==player||board[3][3]=='T'))
		return true;
	if((board[0][3]==player||board[0][3]=='T')&&(board[1][2]==player||board[1][2]=='T')
		&&(board[2][1]==player||board[2][1]=='T')&&(board[3][0]==player||board[3][0]=='T'))
		return true;
	return false;
}
int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int T;
	cin>>T;
	int k=1;
	while(T--)
	{
		bool notCompleted= false;
		for (int i = 0; i < 4 ; i++)
		{
			for (int j = 0; j < 4 ; j++)
			{
				cin>>board[i][j];
				if(board[i][j]=='.')
					notCompleted=true;
			}
		}
		string outcome;
		if(checkWin('X'))
			outcome = "X won";
		else if(checkWin('O'))
		{
			outcome = "O won";
		}
		else if(notCompleted)
			outcome = "Game has not completed";
		else
		{
			outcome = "Draw";
		}
		cout<<"Case #"<<k++<<": "<<outcome<<endl;
	}
	return 0;
}