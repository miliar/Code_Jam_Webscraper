#include<iostream>

using namespace std;
char getWinner(char board[4][4])
{
	//horizontal
	bool flag = true;
		for(int i=0 ; i<4 ; i++)
		{
			flag = true;
			int j = 1;
			char x = board[i][0];
			if(x=='T')
			{
				j=2;
				x = board[i][1];
			}
			for(j ; j<4 ; j++)
			if(((board[i][j]!=x)&&(board[i][j]!='T'))||(board[i][j]=='.'))
			{
				flag = false;
				break;
			}
			if(flag==true)
			{
			return x;
			}
		}
		for(int i=0 ; i<4 ; i++)
		{//vertical
			flag = true;
			int j = 1;
			char x = board[0][i];
			if(x=='T')
			{
				j=2;
				x = board[1][i];
			}
			for(j ; j<4 ; j++)
			if(((board[j][i]!=x)&&(board[j][i]!='T'))||(board[j][i]=='.'))
			{
				flag = false;
				break;
			}
			if(flag==true)
			{
			return x;
			}
		}
		if(board[0][0]!='.')
		{//main diagonal
			bool flag = true;
			char x = board[0][0];
			int i = 1;
			if(x == 'T')
			{
				x == board[1][1];
				i = 2;
			}
			for(i ; i<4  ; i++)
			{
				if(((board[i][i]!=x)&&(board[i][i]!='T'))||(board[i][i]=='.'))
				{
				flag = false;
				break;
				}
			}
			if(flag==true)
			{
			return x;
			}
		}
			//2nd diagonal
		if(board[0][3]!='.')
		{
			bool flag = true;
			char x = board[0][3];
			int i = 1;
			if(x == 'T')
			{
				x == board[1][2];
				i = 2;
			}
			for(i ; i<4  ; i++)
			{
				if(((board[i][3-i]!=x)&&(board[i][3-i]!='T'))||(board[i][3-i]=='.'))
				{
				flag = false;
				break;
				}
			}
			if(flag==true)
			{
			return x;
			}
			
		}
		return 'q';
	
}
bool isDraw(char board[4][4])
{
	for(int i=0 ; i<4 ; i++)
	for(int j=0 ; j<4 ; j++)
	{
		if(board[i][j]=='.')
		{
			return false;
		}
	}
	return true;
}
int main()
{
	int cases;
	cin>>cases;
	
	for(int q=0 ; q<cases ; q++)
	{
		char board[4][4];
		for(int i=0 ; i<4 ; i++)
		for(int j=0 ; j<4 ; j++)
		cin >> board[i][j];
		cout << "Case #" << q+1 << ": ";
		
		char winner;
		winner = getWinner(board);
		if(winner!='q')
		cout<<winner<<" won\n";
		else
		if(isDraw(board))
			cout<<"Draw\n";
		else
			cout<<"Game has not completed\n";
	}
	
	return 0;
}
