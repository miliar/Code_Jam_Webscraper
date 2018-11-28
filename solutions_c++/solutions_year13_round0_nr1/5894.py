#include <fstream>
using namespace std;

#define DIM	4

char	chBoard[DIM][DIM];


bool checkforwinInCol(unsigned int nCol, bool bTFound, unsigned int TRow, char& chWinner)
{
	if (bTFound)
	{
		if (TRow == 0)
		{
			if ((chBoard[1][nCol] == chBoard[2][nCol]) && (chBoard[2][nCol] == chBoard[3][nCol]) && (chBoard[1][nCol] != '.'))
			{
				chWinner = chBoard[1][nCol];
				return true;
			}
		}
		if (TRow == 1)
		{
			if ((chBoard[0][nCol] == chBoard[2][nCol]) && (chBoard[2][nCol] == chBoard[3][nCol]) && (chBoard[0][nCol] != '.'))
			{
				chWinner = chBoard[0][nCol];
				return true;
			}
		}
		if (TRow == 2)
		{
			if ((chBoard[0][nCol] == chBoard[1][nCol]) && (chBoard[1][nCol] == chBoard[3][nCol])&& (chBoard[0][nCol] != '.'))
			{
				chWinner = chBoard[0][nCol];
				return true;
			}
		}
		if (TRow == 3)
		{
			if ((chBoard[0][nCol] == chBoard[1][nCol]) && (chBoard[1][nCol] == chBoard[2][nCol])&& (chBoard[0][nCol] != '.'))
			{
				chWinner = chBoard[0][nCol];
				return true;
			}
		}
	}
	else
	{
		if ((chBoard[0][nCol] == chBoard[1][nCol]) && (chBoard[2][nCol] == chBoard[3][nCol]) && (chBoard[1][nCol] == chBoard[2][nCol]) && (chBoard[0][nCol] != '.'))
		{
			chWinner = chBoard[0][nCol];
			return true;
		}
	}
	
	return false;
}

bool checkforWinInFirstDiag(bool bTFound, unsigned int TRow, char& chWinner)
{
	if (bTFound)
	{
		if (TRow == 0)
		{
			if ((chBoard[1][1] == chBoard[2][2]) && (chBoard[2][2] == chBoard[3][3]) && (chBoard[1][1] != '.'))
			{
				chWinner = chBoard[1][1];
				return true;
			}
		}
		if (TRow == 1)
		{
			if ((chBoard[0][0] == chBoard[2][2]) && (chBoard[2][2] == chBoard[3][3]) && (chBoard[0][0] != '.'))
			{
				chWinner = chBoard[0][0];
				return true;
			}
		}
		if (TRow == 2)
		{
			if ((chBoard[0][0] == chBoard[1][1]) && (chBoard[1][1] == chBoard[3][3])&& (chBoard[0][0] != '.'))
			{
				chWinner = chBoard[0][0];
				return true;
			}
		}
		if (TRow == 3)
		{
			if ((chBoard[0][0] == chBoard[1][1]) && (chBoard[1][1] == chBoard[2][2])&& (chBoard[0][0] != '.'))
			{
				chWinner = chBoard[0][0];
				return true;
			}
		}		
	}
	else
	{
		if ((chBoard[0][0] == chBoard[1][1]) && (chBoard[2][2] == chBoard[3][3]) && (chBoard[2][2] == chBoard[1][1]) && (chBoard[1][1] != '.'))
		{
			chWinner = chBoard[0][0];
			return true;
		}
	}
	
	return false;
}

bool checkforTInSecDiag(unsigned int TRow, unsigned int TCol)
{
	return ((TRow == 0) && (TCol == 3) ||
			(TRow == 1) && (TCol == 2) ||
			(TRow == 2) && (TCol == 1) ||
			(TRow == 3) && (TCol == 0));
}

bool checkforWinInSecDiag(bool bTFound, unsigned int TRow, char& chWinner)
{
	if (bTFound)
	{
		if (TRow == 0)
		{
			if ((chBoard[1][2] == chBoard[2][1]) && (chBoard[2][1] == chBoard[3][0]) && (chBoard[2][1] != '.'))
			{
				chWinner = chBoard[1][2];
				return true;
			}
		}
		else if (TRow == 1)
		{
			if ((chBoard[0][3] == chBoard[2][1]) && (chBoard[2][1] == chBoard[3][0]) && (chBoard[2][1] != '.'))
			{
				chWinner = chBoard[0][3];
				return true;
			}
		}
		else if (TRow == 2)
		{
			if ((chBoard[0][3] == chBoard[1][2]) && (chBoard[1][2] == chBoard[3][0]) && (chBoard[1][2] != '.'))
			{
				chWinner = chBoard[0][3];
				return true;
			}
		}
		else if (TRow == 3)
		{
			if ((chBoard[0][3] == chBoard[1][2]) && (chBoard[1][2] == chBoard[2][1]) && (chBoard[2][1] != '.'))
			{
				chWinner = chBoard[0][3];
				return true;
			}
		}
	}
	else 
	{
		if ((chBoard[0][3] == chBoard[1][2]) && (chBoard[2][1] == chBoard[3][3]) && (chBoard[2][1] == chBoard[1][2]) && (chBoard[1][2] != '.'))
		{
			chWinner = chBoard[0][3];
			return true;
		}
	}

	return false;
}

int main()
{

	unsigned int	nCases, nIndex = 0, nRow, nCol, nPlaysNum, TRow, TCol;
	bool			bXWin, bOWin, TFound, TTotalGame, bBoardEmpty, TColCheck;
	char			line[2];

	ifstream	InFile("A-small-attempt2.in");
	ofstream	OutFile("A-small-attempt2.out", ios_base::ate || ios_base::out);
	
	InFile >> nCases;

	if (OutFile.is_open())
	{
		while (nCases--)
		{
			bBoardEmpty = false;
			bXWin = false;
			bOWin = false;
			TFound = false;
			TTotalGame = false;
			TColCheck = false;
			nPlaysNum = 0;
			
			for (nRow = 0; nRow < DIM; ++nRow)
			{
				for (nCol = 0; nCol < DIM; ++nCol)
				{
					InFile >> chBoard[nRow][nCol];

					if (chBoard[nRow][nCol] == 'T')
					{
						TTotalGame = true; TColCheck = true; TRow = nRow; TCol = nCol;
					}
					else if (chBoard[nRow][nCol] == '.')
					{
						bBoardEmpty = true;
					}
				}

				if (!bXWin && !bOWin)
				{
					if (TColCheck)
					{
						TColCheck = false;
						
						if (TCol == 0)
						{
							if ((chBoard[nRow][1] == chBoard[nRow][2]) && (chBoard[nRow][2] == chBoard[nRow][3]) && (chBoard[nRow][2] != '.'))
							{
								if (chBoard[nRow][1] == 'X')
									bXWin = true;
								else
									bOWin = true;
							}
						}
						else if (TCol == 1)
						{
							if ((chBoard[nRow][0] == chBoard[nRow][2]) && (chBoard[nRow][2] == chBoard[nRow][3]) && (chBoard[nRow][3] != '.'))
							{
								if (chBoard[nRow][0] == 'X')
									bXWin = true;
								else
									bOWin = true;
							}
						}
						else if (TCol == 2)
						{
							if ((chBoard[nRow][0] == chBoard[nRow][1]) && (chBoard[nRow][1] == chBoard[nRow][3]) && (chBoard[nRow][3] != '.'))
							{
								if (chBoard[nRow][0] == 'X')
									bXWin = true;
								else
									bOWin = true;
							}
						}
						else if (TCol == 3)
						{
							if ((chBoard[nRow][0] == chBoard[nRow][1]) && (chBoard[nRow][1] == chBoard[nRow][2]) && (chBoard[nRow][3] != '.'))
							{
								if (chBoard[nRow][0] == 'X')
									bXWin = true;
								else
									bOWin = true;
							}
						}
					}
					else if ((chBoard[nRow][0] == chBoard[nRow][1]) && (chBoard[nRow][2] == chBoard[nRow][3]) && (chBoard[nRow][0] == chBoard[nRow][2]) && (chBoard[nRow][0] != '.'))
					{
						if (chBoard[nRow][0] == 'X')
							bXWin = true;
						else
							bOWin = true;
					}
				}
			}

			InFile.getline(line, 2);
			
			if (!bXWin && !bOWin)
			{
				char chWinner;
				bool bTChecked = false;
				
				for (nCol = 0; nCol < DIM; ++nCol)
				{
					if (!bTChecked && TTotalGame && (TCol == nCol))
					{
						bTChecked = true;
						
						if (checkforwinInCol(nCol, true, TRow, chWinner))
						{
							if (chWinner == 'X') bXWin = true;
							else bOWin = true;
							break;
						}
					}
					else if (checkforwinInCol(nCol, false, 0, chWinner))
					{
						if (chWinner == 'X') bXWin = true;
						else bOWin = true;
						break;
					}
				}

				if (!bXWin && !bOWin)
				{
					char chWinner;
					
					if (TTotalGame && (TRow == TCol))
					{
						TTotalGame = false;
						
						if (checkforWinInFirstDiag(true, TRow, chWinner))
						{
							if (chWinner == 'X') bXWin = true;
							else bOWin = true;	
						}
					}
					else if (checkforWinInFirstDiag(false, 0, chWinner))
					{
						if (chWinner == 'X') bXWin = true;
						else bOWin = true;						
					}
					
					if (!bXWin && !bOWin)
					{
						if (TTotalGame && checkforTInSecDiag(TRow, TCol))
						{
							if (checkforWinInSecDiag(true, TRow, chWinner))
							{
								if (chWinner == 'X') bXWin = true;
								else bOWin = true;						
							}
						}
						else if	(checkforWinInSecDiag(false, 0, chWinner))
						{
							if (chWinner == 'X') bXWin = true;
							else bOWin = true;				
						}
					}
				}
			}

			OutFile << "Case #" << ++nIndex << ": ";
			
			if (bXWin)
			{
				OutFile << "X won" << endl;
			}
			else if (bOWin)
			{
				OutFile << "O won" << endl;
			}
			else if (bBoardEmpty)
			{
				OutFile << "Game has not completed" << endl;
			}
			else
				OutFile << "Draw" << endl;
		}
	}
	
	InFile.close();
	OutFile.close();

	return 0;
}