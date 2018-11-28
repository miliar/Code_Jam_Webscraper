#include <stdio.h>

char board[4][4];

void readBoard()
{
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			scanf(" %c", &board[i][j]);
		}
}

bool playerField(char player, int row, int kol)
{
	return board[row][kol] == 'T' || board[row][kol] == player;
}

bool hasDiag1(char player)
{
	for(int i=0; i<4; i++)
	{
		if(!playerField(player, i, i)) return false;
	}
	return true;
}

bool hasDiag2(char player)
{
	for(int i=0; i<4; i++)
	{
		if(!playerField(player, i, 3-i)) return false;
	}
	return true;
}

bool hasDiag(char player)
{
	return hasDiag1(player) || hasDiag2(player);
}

bool has4inKol(char player, int kol)
{
	for(int row=0; row<4; row++)
	{
		if(!playerField(player, row, kol)) return false;
	}
	return true;
}
bool has4inKol(char player)
{
	for(int kol=0; kol<4; kol++)
		if(has4inKol(player, kol)) return true;
	return false;		
}

bool has4inRow(char player, int row)
{
	for(int kol=0; kol<4; kol++)
	{
		if(!playerField(player, row, kol)) return false;
	}
	return true;
}
bool has4inRow(char player)
{
	for(int row=0; row<4; row++)
		if(has4inRow(player, row)) return true;
	return false;		
}

bool hasWon(char player)
{	
	return (has4inRow(player) || has4inKol(player) || hasDiag(player));
}

bool isBoardFull()
{
	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
		{
			if(board[i][j] == '.') return false;
		}

	return true;
}

char* resolveGame()
{
	readBoard();
	if(hasWon('X'))
		return "X won";

	if(hasWon('O'))
		return "O won";

	if(isBoardFull())
		return "Draw";

	return "Game has not completed";
}

int main()
{
	int count;
	scanf("%d", &count);

	for(int i=0; i<count; i++)
	{
		printf("Case #%d: %s\n", i+1, resolveGame());
	}
	return 0;
}

