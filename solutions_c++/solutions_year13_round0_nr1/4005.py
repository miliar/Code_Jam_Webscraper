//Jakub "Cubix651" Cisło
//Task: Tic-Tac-Toe-Tomek
#include <cstdio>

int t;
char board[4][6];

bool display(int x, int o, int t)
{
	if(x == 4 || (x == 3 && t == 1))
	{
		printf("X won\n");
		return true;
	}
	if(o == 4 || (o == 3 && t == 1))
	{
		printf("O won\n");
		return true;
	}
	
	return false;
}

bool checkVer(int col)
{
	int x = 0, o = 0, t = 0;
	
	for(int i = 0; i < 4; ++i)
	{
		if(board[i][col] == 'X')
			++x;
		else if(board[i][col] == 'O')
			++o;
		else if(board[i][col] == 'T')
			++t;
	}
	return display(x, o, t);
}

bool checkHor(int row)
{
	int x = 0, o = 0, t = 0;
	
	for(int i = 0; i < 4; ++i)
	{
		if(board[row][i] == 'X')
			++x;
		else if(board[row][i] == 'O')
			++o;
		else if(board[row][i] == 'T')
			++t;
	}
	return display(x, o, t);
}

bool checkDia1()
{
	int x = 0, o = 0, t = 0;
	
	for(int i = 0; i < 4; ++i)
	{
		if(board[i][i] == 'X')
			++x;
		else if(board[i][i] == 'O')
			++o;
		else if(board[i][i] == 'T')
			++t;
	}
	return display(x, o, t);
}

bool checkDia2()
{
	int x = 0, o = 0, t = 0;
	
	for(int i = 0; i < 4; ++i)
	{
		if(board[3-i][i] == 'X')
			++x;
		else if(board[3-i][i] == 'O')
			++o;
		else if(board[3-i][i] == 'T')
			++t;
	}
	return display(x, o, t);
}

bool checkDraw()
{
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(board[i][j] == '.')
				return false;
	printf("Draw\n");
	return true;
}

int main()
{
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		for(int i = 0; i < 4; ++i)
			scanf("%s", board[i]);
		
		printf("Case #%d: ", tt);
		bool end = false;
		for(int i = 0; i < 4; ++i)
		{
			end = end || checkVer(i);
			end = end || checkHor(i);
		}
		end = end || checkDia1();
		end = end || checkDia2();
		end = end || checkDraw();
		if(!end)
			printf("Game has not completed\n");
	}
	return 0;
}
