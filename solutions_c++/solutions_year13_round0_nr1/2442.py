#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#define SIZE 4
using namespace std;
char input[10],board[SIZE+1][SIZE+1],i;
bool checkWin(int x, int y, char symbol)
{
	int counter=0,i=0;
	for(i=0;i<SIZE;i++)
	{
		if(x+i<SIZE && y+i<SIZE)
		{
			if(board[x+i][y+i]==symbol || board[x+i][y+i]=='T')
				counter++;
			else
				break;
		}
		else
			break;
	}
	if(counter==4)
		return true;
	//if(counter==3 && board[x+i][y+i]=='T')
	//	return true;
	counter=0;
	for(i=0;i<SIZE;i++)
	{
		if(x+i<SIZE)
		{
			if(board[x+i][y]==symbol || board[x+i][y]=='T')
				counter++;
			else
				break;
		}
		else
			break;
	}
	if(counter==4)
		return true;
	//if(counter==3 && board[x+i][y]=='T')
	//	return true;
		
	counter=0;
	for(i=0;i<SIZE;i++)
	{
		if(y+i<SIZE)
		{
			if(board[x][y+i]==symbol || board[x][y+i]=='T')
				counter++;
			else
				break;
		}
		else
			break;
	}
	if(counter==4)
		return true;
	//if(counter==3 && board[x][y+i]=='T')
	//	return true;
		
	counter=0;
	for(i=0;i<SIZE;i++)
	{
		if(y-i>=0 && x+i<SIZE)
		{
			if(board[x+i][y-i]==symbol || board[x+i][y-i]=='T')
				counter++;
			else
				break;
		}
		else
			break;
	}
	if(counter==4)
		return true;
	//if(counter==3 && board[x+i][y-i]=='T')
	//	return true;
	return false;
}
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("a.txt","w",stdout);
	
	int cases,t,i,j;
	bool empty,win;
	cin>>t;
	for(cases=1;cases<=t;cases++)
	{
		for(i=0;i<SIZE;i++)
			cin>>board[i];
		empty=false;
		for(i=0;i<SIZE;i++)
		{
			for(j=0;j<SIZE;j++)
			{
				if(board[i][j]=='.')
					empty=true;
				if(board[i][j]=='O' || board[i][j]=='X')
				{
					win=checkWin(i,j,board[i][j]);
					if(win)
						break;
				}
				if(board[i][j]=='T')
				{
					board[i][j]='O';
					win=checkWin(i,j,board[i][j]);
					if(win)
						break;
					board[i][j]='X';
					win=checkWin(i,j,board[i][j]);
					if(win)
						break;
					board[i][j]='T';
				}
			}
			if(win)
				break;
		}
		if(win)
		{
			if(board[i][j]=='O')
				printf("Case #%d: O won\n",cases);
			else
				printf("Case #%d: X won\n",cases);
		}
		else
		{
			if(!empty)
				printf("Case #%d: Draw\n",cases);
			else
				printf("Case #%d: Game has not completed\n",cases);
		}
	}
	return 0;
}