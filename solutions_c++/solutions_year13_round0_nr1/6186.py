#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;

char board[5][5];

char checkRows()
{
	char win='.';
	for(int i=0;i<4;i++)
	{
		bool ok=true;
		win=board[i][0];

		if(board[i][0]=='.')
			continue;

		if(win=='T')
			win=board[i][1];

		for(int j=1;j<4;j++)
		{
			if(!(win==board[i][j] || board[i][j]=='T') || (board[i][j]=='.'))
			{
				ok=false;
				
				win='.';
				break;
			}
		}

		if(ok)
		{
			return win;
		}
	}
	return win;
}

char checkCols()
{
	char win='.';
	for(int i=0;i<4;i++)
	{
		bool ok=true;
		win=board[0][i];

		if(board[0][i]=='.')
			continue;


		if(win=='T')
			win=board[1][i];

		for(int j=1;j<4;j++)
		{
			if(!(win==board[j][i] || board[j][i]=='T') || (board[j][i]=='.'))
			{
				ok=false;
				win='.';
				break;
			}
		}

		if(ok)
		{
			return win;
		}
	}
	return win;
}

char checkDia()
{
	char win='.';
	bool ok=true;
	win=board[0][0];
	if(win=='T')
		win=board[1][1];
	if(board[0][0]!='.')
	{
		for(int i=1;i<4;i++)
		{
			if(!(board[i][i]==win || board[i][i]=='T'))
			{
				ok=false;
				win='.';
				break;
			}

		}
		if(win!='.')
			return win;
	}
	win=board[0][3];
	if(win=='T')
		win=board[1][2];
	if(board[0][3]!='.')
	{
		for(int i=1,j=2;i<4;i++,j--)
		{
			if(!(board[i][j]==win || board[i][j]=='T'))
			{
				ok=false;
				win='.';
				break;
			}

		}
		if(win!='.')
			return win;
	}
	return win;
}

int main()
{
	//ifstream cin("A-small-attempt0.in");
	//ofstream cout("A-small.out");
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");


	int test;
	cin>>test;

	for(int k=0;k<test;k++)
	{
		bool complete=true;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>board[i][j];
				if(board[i][j]=='.')
					complete=false;
			}
		}

		
		char row=checkRows();
		if(row!='.')
			cout<<"Case #"<<(k+1)<<": "<<row<<" "<<"won"<<endl;
		else
		{
			char col=checkCols();
			if(col!='.')
				cout<<"Case #"<<(k+1)<<": "<<col<<" "<<"won"<<endl;
			else
			{
				char dia=checkDia();
				if(dia!='.')
					cout<<"Case #"<<(k+1)<<": "<<dia<<" "<<"won"<<endl;
				else
				{
					if(complete)
						cout<<"Case #"<<(k+1)<<": Draw"<<endl;
					else 
						cout<<"Case #"<<(k+1)<<": Game has not completed"<<endl;
				}
			}
			

		}
		
	}

	system("pause");
	return 0;
}