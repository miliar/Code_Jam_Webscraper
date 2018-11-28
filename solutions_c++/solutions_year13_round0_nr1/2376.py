#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>


typedef std::vector<std::string> Grid;
typedef std::pair<int, int> Coord;


struct Board
{
	Grid grid;
	Coord tPos;
	bool hasDot;


	Board() : tPos(-1, -1), hasDot(false) {};
};

typedef std::vector<Board> Boards;


const char T = 'T';
const char X = 'X';
const char O = 'O';
const char dot = '.';

std::ofstream out;

Boards readInput(const char* fn)
{
	std::ifstream ifs(fn);

	size_t nGrids = 0;
	ifs >> nGrids;

	Boards boards(nGrids);


	for (size_t n = 0; n < nGrids; ++n)
	{
		
		for (size_t i = 0; i < 4; ++i)
		{
			std::string s;	
			ifs >> s;
			boards[n].grid.push_back(s);
			size_t tPos = s.find(T);
			if (tPos != std::string::npos)
				boards[n].tPos = std::make_pair(i, tPos);
			if (!boards[n].hasDot && s.find(dot) != std::string::npos )
				boards[n].hasDot = true;

		}
	}

	return boards;
}

bool CheckWin(const Board &b, char c)
{
	bool win = false;
	for (int i = 0; i < 4; ++i)
	{
		int row = 0;
		for(int j = 0; j < 4; ++j)
		{
			if (b.grid[i][j] == c)
				++row;
		}
		if (row == 4)
		{
			win = true;
			break;
		}
	}

	if (win)
		return win;

	for (int i = 0; i < 4; ++i)
	{
		int col = 0;
		for(int j = 0; j < 4; ++j)
		{
			if (b.grid[j][i] == c)
				++col;
		}
		if (col == 4)
		{
			win = true;
			break;
		}
	}

	if (win)
		return win;

	int diag = 0;
	for (int i = 0; i < 4; ++i)
		if (b.grid[i][i] == c)
			++diag;

	win = diag == 4;
	if (win)
		return win;

	diag = 0;
	for (int i = 0; i < 4; ++i)
		if (b.grid[i][3-i] == c)
			++diag;

	win = diag == 4;
	return win;
}

void CheckBoard(Board &b)
{
	const Coord &tPos = b.tPos;

	if (tPos.first >= 0 && tPos.second >= 0)
		b.grid[b.tPos.first][b.tPos.second] = X;
	if (CheckWin(b, X))
	{
		out << X << " won" << std::endl;
		return;
	}

	if (tPos.first >= 0 && tPos.second >= 0)
		b.grid[b.tPos.first][b.tPos.second] = O;
	if (CheckWin(b, O))
	{
		out << O << " won" << std::endl;
		return;
	}

	if (b.hasDot)
	{
		out << "Game has not completed" << std::endl;
		return;
	}

	out << "Draw" << std::endl;

}


int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Boards boards = readInput(argv[1]);

	size_t nb = boards.size();

	for (size_t i = 0; i < nb; ++i)
	{
		out << "Case #" << i+1 << ": ";
		CheckBoard(boards[i]);
	}

	return 0;
}