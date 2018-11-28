#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>

using namespace std;

static ifstream fi;
static ofstream fo;

void redirectInput(const std::string& fileName)
{
	fi.open(fileName, std::ios_base::in);
	std::cin.rdbuf(fi.rdbuf());
}

void redirectOutput(const std::string& fileName)
{
	fo.open(fileName, std::ios_base::out);
	std::cout.rdbuf(fo.rdbuf());
}

enum GameState
{
	ePlaying,
	eWinX,
	eWinO,
	eDraw,
};

const char kX = 'X';
const char kO = 'O';
const char kT = 'T';
const char kDot = '.';

GameState checkRows(char b[4][4])
{
	int i,j;
	int xCount;
	int oCount;
	int dotCount = 0;

	GameState gs = ePlaying;

	for (i = 0; i < 4; ++i)
	{
		xCount = 0;
		oCount = 0;

		for (j = 0; j < 4; ++j)
		{
			if (b[i][j] == kX)
				xCount ++;
			else if (b[i][j] == kO)
				oCount ++;
			else if (b[i][j] == kT)
			{
				xCount ++;
				oCount ++;
			}
			else
				dotCount ++;
		}

		if (xCount == 4)
		{
			gs = eWinX;
			break;
		}
		else if (oCount == 4)
		{
			gs = eWinO;
			break;
		}
	}

	if (gs == ePlaying && dotCount == 0)
		gs = eDraw;

	return gs;
}

GameState checkCols(char b[4][4])
{
	int i,j;
	int xCount;
	int oCount;
	int dotCount = 0;

	GameState gs = ePlaying;

	for (i = 0; i < 4; ++i)
	{
		xCount = 0;
		oCount = 0;

		for (j = 0; j < 4; ++j)
		{
			if (b[j][i] == kX)
				xCount ++;
			else if (b[j][i] == kO)
				oCount ++;
			else if (b[j][i] == kT)
			{
				xCount ++;
				oCount ++;
			}
			else
				dotCount ++;
		}

		if (xCount == 4)
		{
			gs = eWinX;
			break;
		}
		else if (oCount == 4)
		{
			gs = eWinO;
			break;
		}
	}

	if (gs == ePlaying && dotCount == 0)
		gs = eDraw;

	return gs;
}

GameState checkDiagonals(char b[4][4])
{
	GameState gs = ePlaying;

	// First
	if ((b[0][0] == kX || b[0][0] == kT) &&
		(b[1][1] == kX || b[1][1] == kT) &&
		(b[2][2] == kX || b[2][2] == kT) &&
		(b[3][3] == kX || b[3][3] == kT))
		gs = eWinX;
	else
	if ((b[0][0] == kO || b[0][0] == kT) &&
		(b[1][1] == kO || b[1][1] == kT) &&
		(b[2][2] == kO || b[2][2] == kT) &&
		(b[3][3] == kO || b[3][3] == kT))
		gs = eWinO;
	else
	if ((b[0][3] == kX || b[0][3] == kT) &&
		(b[1][2] == kX || b[1][2] == kT) &&
		(b[2][1] == kX || b[2][1] == kT) &&
		(b[3][0] == kX || b[3][0] == kT))
		gs = eWinX;
	else
		if ((b[0][3] == kO || b[0][3] == kT) &&
			(b[1][2] == kO || b[1][2] == kT) &&
			(b[2][1] == kO || b[2][1] == kT) &&
			(b[3][0] == kO || b[3][0] == kT))
			gs = eWinO;

	return gs;
}

void main()
{
	redirectInput("in.txt");
	redirectOutput("out.txt");

	int caseCount;
	std::string str;
	int i,j;

	char b[4][4];
	GameState gs;

	cin >> caseCount;
	cin.get();

	if (caseCount < 1 || caseCount > 1000)
		return;

	for (i = 0; i < caseCount; ++i)
	{
		// Board data loading
		for (j = 0; j < 4; ++j)
		{
			getline(cin, str);
			b[j][0] = str[0];
			b[j][1] = str[1];
			b[j][2] = str[2];
			b[j][3] = str[3];
		}
		
		// Reset board status
		gs = ePlaying;
	
		// Diagonals
		gs = checkDiagonals(b);

		// Rows
		if (gs == ePlaying)
			gs = checkRows(b);

		// Cols
		if (gs == ePlaying || gs ==eDraw)
			gs = checkCols(b);

		cout << "Case #" << (i + 1) << ": ";

		switch (gs)
		{
		case ePlaying:
			cout << "Game has not completed" << endl;
			break;
		case eWinX:
			cout << "X won" << endl;
			break;
		case eWinO:
			cout << "O won" << endl;
			break;
		case eDraw:
			cout << "Draw" << endl;
			break;
		}

		// board separator
		cin.get();
	}
}
