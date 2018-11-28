#include<iostream>
using namespace std;

int main()
{
int testCases;
char board[4][4];

cin>>testCases;


for(int p=0;p<testCases;p++)
{
int dotcounter=0;
for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		{
		cin>>board[i][j];
		if(board[i][j]=='.')
			dotcounter++;
		}

int x_o=0;
int counter;
int isvictory=0;
for(int i=0;i<4;i++)
{
	counter=1;
	if(board[i][0]=='T' && board[i][1]=='X')
	{
		x_o=0;
	}
	else if(board[i][0]=='T' && board[i][1]=='O')
	{
		x_o=1;
	}
	else if(board[i][0]=='X')
	{
		x_o=0;
	}
	else if(board[i][0]=='O')
	{
		x_o=1;
	}
	else
	{
		x_o=2;
	}
	if(x_o!=2)
	{
		for(int j=1;j<4;j++)
		{
			if(board[i][j]==board[i][j-1] || board[i][j]=='T' || board[i][j-1]=='T')
				counter++;
			else
				break;
		}
	}	
	
	if(counter==4)
	{
		if(x_o==0)
			{
			cout<<"Case #"<<p+1<<": "<<"X won"<<endl;
			isvictory=1;
			break;
			}
			
		else
			{
			cout<<"Case #"<<p+1<<": "<<"O won"<<endl;
			isvictory=1;
			break;
			}
	}	
}
if(isvictory==1)
	continue;


for(int i=0;i<4;i++)
{
	counter=1;
	if(board[0][i]=='T' && board[1][i]=='X')
	{
		x_o=0;
	}
	else if(board[0][i]=='T' && board[1][i]=='O')
	{
		x_o=1;
	}
	else if(board[0][i]=='X')
	{
		x_o=0;
	}
	else if(board[0][i]=='O')
	{
		x_o=1;
	}
	else
	{
		x_o=2;
	}
	if(x_o!=2)
	{
		for(int j=1;j<4;j++)
		{
			if(board[j][i]==board[j-1][i] || board[j][i]=='T' || board[j-1][i]=='T')
				counter++;
			else
				break;
		}
	}	
	
	if(counter==4)
	{
		if(x_o==0)
			{
			cout<<"Case #"<<p+1<<": "<<"X won"<<endl;
			isvictory=1;
			break;
			}
			
		else
			{
			cout<<"Case #"<<p+1<<": "<<"O won"<<endl;
			isvictory=1;
			break;
			}
	}	
}

if(isvictory==1)
	continue;

if(board[0][0]=='X')
	x_o=0;
else if(board[0][0]=='O')
	x_o=1;
else if(board[0][0]=='T')
{
	if(board[1][1]=='X')
		x_o=0;
	else if(board[1][1]=='O')
		x_o=1;	
}
else x_o=2;
counter=1;
if(x_o!=2)
for(int i=1;i<4;i++)
{
	if(board[i][i]==board[i-1][i-1] || board[i][i]=='T' || board[i-1][i-1]=='T')
	counter++;
}
if(counter==4)
	{
		if(x_o==0)
			{
			cout<<"Case #"<<p+1<<": "<<"X won"<<endl;
			isvictory=1;

			}
			
		else
			{
			cout<<"Case #"<<p+1<<": "<<"O won"<<endl;
			isvictory=1;

			}
	}
if(isvictory==1)
	continue;



if(board[0][3]=='X')
	x_o=0;
else if(board[0][3]=='O')
	x_o=1;
else if(board[0][3]=='T')
{
	if(board[1][2]=='X')
		x_o=0;
	else if(board[1][2]=='O')
		x_o=1;	
}
else x_o=2;
counter=1;
if(x_o!=2)
for(int i=1;i<4;i++)
{
	if(board[i][3-i]==board[i-1][4-i] || board[i][3-i]=='T' || board[i][4-i]=='T')
	counter++;
}
if(counter==4)
{
		if(x_o==0)
			{
			cout<<"Case #"<<p+1<<": "<<"X won"<<endl;
			isvictory=1;

			}
			
		else
			{
			cout<<"Case #"<<p+1<<": "<<"O won"<<endl;
			isvictory=1;

			}
}
if(isvictory!=1 && dotcounter>0)
cout<<"Case #"<<p+1<<": "<<"Game has not completed"<<endl;
if(isvictory!=1 && dotcounter==0)
cout<<"Case #"<<p+1<<": "<<"Draw"<<endl;

}
return 0;
}
	
