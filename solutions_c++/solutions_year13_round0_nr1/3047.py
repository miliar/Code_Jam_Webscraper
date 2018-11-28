#include <iostream>
#include <string>

using namespace std;

int check_status(string board[4],char player)
{
	int count;
	//Row Wise
	for (int i = 0; i < 4; ++i)
	{
		count=0;
		for (int j = 0; j < 4; ++j)
		{
			if(board[i][j]=='T' || board[i][j]==player)++count;
		}
		if(count==4)return 1;
	}
	//Col Wise
	for (int i = 0; i < 4; ++i)
	{
		count=0;
		for (int j = 0; j < 4; ++j)
		{
			if(board[j][i]=='T' || board[j][i]==player)++count;
		}
		if(count==4)return 1;
	}
	//Dia Wise
	count=0;
	for (int i = 0; i < 4; ++i)
	{
		if(board[i][i]=='T' || board[i][i]==player)++count;
	}
	if(count==4)return 1;
	count=0;
	for (int i = 0; i < 4; ++i)
	{
		if(board[i][3-i]=='T' || board[i][3-i]==player)++count;
	}
	if(count==4)return 1;
	return -1;
}

int main()
{
	int T;
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
		//input
		string board[4];
		for (int j = 0; j < 4; ++j)
		{
			cin>>board[j];
		}

		//count
		int count=0;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if(board[j][k]=='.')++count;
			}
		}

		//calc
		if(check_status(board,'X')==1)
		{
			cout<<"Case #"<<i+1<<": X won\n";
		}
		else if(check_status(board,'O')==1)
		{
			cout<<"Case #"<<i+1<<": O won\n";
		}
		else if(count==0)
		{
			cout<<"Case #"<<i+1<<": Draw\n";
		}
		else
		{
			cout<<"Case #"<<i+1<<": Game has not completed\n";	
		}
	}
	return 0;
}