#include <iostream>
#include <string>

using namespace std;

class Game
{
private:
	char board[4][4];
	bool hasDot;
	char checkRow();
	char checkCol();
	char checkDiaglr();
	char checkDiagrl();

public:
	Game();
	void readBoard();
	char checkWinner();

};

Game::Game()
{
	hasDot = false;
}
void Game::readBoard()
{
	for (int i = 0; i < 4; i++)
		for (int k = 0; k < 4; k++)
			cin >> board[i][k];
}

char Game::checkWinner()
{
	char win = checkRow();
	if (win == 'X' || win == 'O')
		return win;
	win = checkCol();
	if (win == 'X' || win == 'O')
		return win;
	win = checkDiaglr();
	if (win == 'X' || win == 'O')
		return win;
	win = checkDiagrl();
	if (win == 'X' || win == 'O')
		return win;
	else if (hasDot)
		return '.';
	else 
		return '1';
}

char Game::checkRow()
{
	char test = '1';
	bool isPos = false;
	for (int i = 0; i < 4; i++)
	{
		if (isPos)
			return test;
		else
			isPos = true;
		while (i < 4 && board[i][0] == '.' )
		{
			i++;
			hasDot = true;
		}
		if (board[i][0] == 'T')
			test = board[i][1];
		else
			test = board[i][0];
		for (int k = 0; k < 4; k++)
		{
			if (test != board[i][k] && board[i][k] != 'T')
				isPos = false;
			if (board[i][k] == '.')
				hasDot = true;
		}
	}
	if (isPos)
		return test;
	else
		return '1';
}


char Game::checkCol()
{
	char test = '1';
	bool isPos = false;
	for (int i = 0; i < 4; i++)
	{
		if (isPos)
			return test;
		else
			isPos = true;
		while (board[0][i] == '.' && i < 4)
		{
			i++;
			hasDot = true;
		}
		if (board[0][i] == 'T')
			test = board[1][i];
		else
			test = board[0][i];
		for (int k = 0; k < 4; k++)
		{
			if (test != board[k][i] && board[k][i] != 'T')
				isPos = false;
			if (board[k][i] == '.')
				hasDot = true;
		}
	}
	if (isPos)
		return test;
	else
		return '1';
}


char Game::checkDiaglr()
{
	char test = '1';
	bool isPos = true;
	int i = 0;
	if (board[i][i] == '.')
	{
		hasDot = true;
		return '1';
	}
	else if (board[i][i] == 'T')
		i++;
	if (board[i][i] == '.')
	{
		hasDot = true;
		return '1';
	}
	test = board[i][i];
	for (i++; i < 4; i++)
	{
		if (board[i][i] == '.' )
		{

			hasDot = true;
			return '1';
		}
		if (test != board[i][i] && board[i][i] != 'T')
				isPos = false;
		if (board[i][i] == '.')
				hasDot = true;
		
	}
	if (isPos)
		return test;
	else
		return '1';
}

char Game::checkDiagrl()
{
	char test = '1';
	bool isPos = true;
	int i = 3;
	int k = 0;
	if (board[k][i] == '.')
	{
		hasDot = true;
		return '1';
	}
	else if (board[k][i] == 'T')
	{
		i--;
		k++;
	}
	if (board[k][i] == '.')
	{
		hasDot = true;
		return '1';
	}
	test = board[k][i];
	for (i--, k++; i >=0; i-- , k++)
	{
		if (board[k][i] == '.' )
		{
			hasDot = true;
			return '1';
		}
		if (test != board[k][i] && board[k][i] != 'T')
				isPos = false;
		if (board[k][i] == '.')
				hasDot = true;
		
	}
	if (isPos)
		return test;
	else
		return '1';
}

void processString(string sentence[], string entireLine);

int main()
{
	int numOfCases;
	Game* cases;

	cin >> numOfCases;
	cases = new Game[numOfCases];

	for (int i = 0; i < numOfCases; i++)
	{
		cases[i].readBoard();
	}

	for (int i = 0; i < numOfCases; i++)
	{
		cout << "Case #" << i+1 << ": ";
		if ( cases[i].checkWinner() == 'X')
			cout << "X won";
		else if (cases[i].checkWinner() == 'O')
			cout << "O won";
		else if (cases[i].checkWinner() == '.')
			cout << "Game has not completed";
		else 
			cout << "Draw";
		cout << endl;
	}
}


