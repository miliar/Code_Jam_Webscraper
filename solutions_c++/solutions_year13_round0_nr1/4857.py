#include <iostream>
#include <string>

char board[4][4];
std::string status;
int allX = 'X' + 'X' + 'X' + 'X';
int allO = 'O' + 'O' + 'O' + 'O';
int XT = 'X' + 'X' + 'X' + 'T';
int OT = 'O' + 'O' + 'O' + 'T';

void fillBoard()
{
	status = "Draw";
	char temp[5];
	for(int i = 0; i < 4; i++)
	{
		std::cin.getline(temp, 5);
		for(int j = 0; j < 4; j++)
		{
			board[i][j] = temp[j];

			if(board[i][j] == '.')
				status = "Game has not completed";
		}
	}
	std::cin.get();
}

void findStatus()
{
	int topRow = 0, bottomRow = 0, leftColumn = 0, rightColumn = 0, rightDiag = 0, leftDiag = 0;
	int row2 = 0, row3 = 0, column2 = 0, column3 = 0;

	for(int i = 0; i < 4; i++)
	{
		topRow += board[0][i];
		leftColumn += board[i][0];
		rightDiag += board[i][i];
		bottomRow += board[3][i];
		rightColumn += board[i][3];
		leftDiag += board[i][3 -i];
		row2 += board[1][i];
		row3 += board[2][i];
		column2 += board[i][1];
		column3 += board[i][2];
	}

	if(topRow == allX || topRow == XT ||
		leftColumn == allX || leftColumn == XT ||
		rightDiag == allX || rightDiag == XT ||
		bottomRow == allX || bottomRow == XT ||
		rightColumn == allX || rightColumn == XT ||
		leftDiag == allX || leftDiag == XT ||
		row2 == allX || row2 == XT ||
		row3 == allX || row3 == XT ||
		column2 == allX || column2 == XT ||
		column3 == allX || column3 == XT)
	{
		status = "X won";
	}

	else if(topRow == allO || topRow == OT ||
		leftColumn == allO || leftColumn == OT ||
		rightDiag == allO || rightDiag == OT ||
		bottomRow == allO || bottomRow == OT ||
		rightColumn == allO || rightColumn == OT ||
		leftDiag == allO || leftDiag == OT ||
		row2 == allO || row2 == OT ||
		row3 == allO || row3 == OT ||
		column2 == allO || column2 == OT ||
		column3 == allO || column3 == OT)
	{
		status = "O won";
	}
}

int main()
{
	int numCases = 0;
	std::cin >> numCases;
	std::cin.get();
	
	for(int i = 0; i < numCases; i++)
	{
		fillBoard();
		findStatus();
		
		std::cout << "Case #" << (i + 1) << ": " << status << std::endl;
	}

	std::cin.get();
	return 0;
}