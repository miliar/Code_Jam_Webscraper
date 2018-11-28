	#include<iostream>

	#define BOARDSIZE 4
	using namespace std;

	char board[BOARDSIZE][BOARDSIZE];
	int emptyPoint;
	int checkRow(int i)
	{
		int x=1,y=1;
		for(int j=0;j<BOARDSIZE;j++)
			switch(board[i][j])
			{
				case 'X':	y=0; break;
				case 'O':   x=0; break;
				case 'T':	continue;
				default:	return 0;
			}
		if(x) return 1;
		if(y) return 2;
		return 0;
	}

	int checkCol(int i)
	{
		int x=1,y=1;
		for(int j=0;j<BOARDSIZE;j++)
			switch(board[j][i])
			{
				case 'X':	y=0; break;
				case 'O':   x=0; break;
				case 'T':	continue;
				default:	emptyPoint=1; return 0;
			}
		if(x) return 1;
		if(y) return 2;
		return 0;
	}

	int checkSlash()
	{
		int x=1,y=1;
		for(int i=0;i<BOARDSIZE;i++)
			switch(board[i][i])
			{
				case 'X':	y=0; break;
				case 'O':   x=0; break;
				case 'T':	continue;
				default:	emptyPoint=1; return 0;
			}
		if(x) return 1;
		if(y) return 2;
		return 0;
	}

	int checkBackSlash()
	{
		int x=1,y=1;
		for(int i=0;i<BOARDSIZE;i++)
			switch(board[i][BOARDSIZE-1-i])
			{
				case 'X':	y=0; break;
				case 'O':   x=0; break;
				case 'T':	continue;
				default:	emptyPoint=1; return 0;
			}
		if(x) return 1;
		if(y) return 2;
		return 0;
	}

	int submain()
	{
		emptyPoint=0;
		for(int i=0;i<BOARDSIZE;i++)
			for(int j=0;j<BOARDSIZE;j++)
				cin >> board[i][j];
		int x=0,y=0;
		int temp;
		for(int i=0;i<BOARDSIZE;i++)
		{
			temp=checkRow(i);
			if(temp==1)
				x=1;
			else if(temp==2)
				y=1;
			temp=checkCol(i);
			if(temp==1)
				x=1;
			else if(temp==2)
				y=1;
		}
		temp=checkSlash();
		if(temp==1)
			x=1;
		else if(temp==2)
			y=1;
		
		temp=checkBackSlash();
		if(temp==1)
			x=1;
		else if(temp==2)
			y=1;
		if (x==1&&y==0)
			cout << "X won" << endl;
		else if(x==0&&y==1)
			cout << "O won" << endl;
		else if (emptyPoint)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
		return 0;
	}
	
	int main()
	{
		int i;
		cin >> i;
		for(int j=1;j<=i;j++)
		{
			cout << "Case #" << j << ": ";
			submain();
		}
		return 0;
	}