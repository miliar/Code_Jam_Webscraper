#include<iostream>

//returns true if given player has 4 in row, column or diagonal OR 3 with 'T'
bool playerWins(char player, char board[4][4])
{
	int numPlayerSymbols;
	bool containsT;

	//check horizontal
	for(int row=0; row < 4; row++) 
	{
	
		numPlayerSymbols = 0;
		containsT = false;
		
		for(int col=0; col < 4; col++) 
		{
			if(board[row][col] == player)
			{
				numPlayerSymbols++;
			}
			else if(board[row][col] == 'T')
			{
				containsT = true;
			}
		}
		
		if(numPlayerSymbols + containsT == 4)
		{
			return true;
		}
		
	}
	
	//check vertical
	for(int col=0; col < 4; col++)
	{
		numPlayerSymbols = 0;
		containsT = false;
		
		for(int row=0; row < 4; row++) 
		{
			if(board[row][col] == player)
			{
				numPlayerSymbols++;
			}
			else if(board[row][col] == 'T')
			{
				containsT = true;
			}
		}
		
		if(numPlayerSymbols + containsT == 4)
		{
			return true;
		}
	}
	
	//check left horizontal
	numPlayerSymbols = 0;
	containsT = false;
	
	for(int rc=0; rc < 4; rc++)
	{
		if(board[rc][rc] == player)
		{
			numPlayerSymbols++;
		}
		else if(board[rc][rc] == 'T')
		{
			containsT = true;
		}
	}
	
	if(numPlayerSymbols + containsT == 4)
	{
		return true;
	}
	
	
	//check right horizontal
	numPlayerSymbols = 0;
	containsT = false;
	
	for(int rc=0; rc < 4; rc++)
	{
		if(board[rc][3 - rc] == player)
		{
			numPlayerSymbols++;
		}
		else if(board[rc][3 - rc] == 'T')
		{
			containsT = true;
		}
	}
	
	if(numPlayerSymbols + containsT == 4)
	{
		return true;
	}
	
	
	
	//else return false
	return false;
}

//returns true if board is full
bool boardFull(char board[4][4])
{
	for(int row=0; row < 4; row++)	{
	for(int col=0; col < 4; col++)	{
	
		if(board[row][col] == '.')
		{
			return false;
		}
	
	}
	}
	
	return true;
}

int main()
{
	int numTests;
	std::cin >> numTests;
	
	for(int testCase = 1; testCase <= numTests; testCase++)
	{
		//enter board
		char board[4][4];
		
		for(int row=0; row < 4; row++)	{
		for(int col=0; col < 4; col++)	{
		
			std::cin >> board[row][col];
		
		}
		}
		
		
		//get results
		bool xWins = playerWins('X', board);
		bool oWins = playerWins('O', board);
		
		//print results
		std::cout << "Case #" << testCase << ": ";
		
		if(xWins == oWins) //draw
		{
			if(boardFull(board) || xWins) //game is over OR both players have won
			{
				std::cout << "Draw";
			}
			else
			{
				std::cout << "Game has not completed";
			}
		}
		else if(xWins) //just X
		{
			std::cout << "X won";
		}
		else if(oWins) //just O
		{
			std::cout << "O won";
		}
		
		std::cout << std::endl;
		
	}
	
	
	return 0;
}