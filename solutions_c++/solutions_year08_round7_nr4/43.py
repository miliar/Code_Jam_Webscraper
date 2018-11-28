#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
//#include <hash_map>
#include <iterator>
#include <functional>
#include <string>
#include <cassert>

enum Players
{
	firstPlayer,
	secondPlayer
};

struct King
{
	short x;
	short y;
};


using namespace  std;
using namespace  stdext;

typedef vector<bool> BoardRow;
typedef vector<BoardRow> Board;

typedef pair<King, Board> Position;
/*
struct eqstr
{
	bool operator()(Position const& a, Position const& b) const
	{
		return a == b;
	}
};
struct haash
{
	size_t operator()(Position const& a) const
	{
		size_t res = 0;
		for (int i = 0; i < a.second.size(); ++i)
		{
			res ^= (*this)(a.second[i]);
		}
		return res;
	}
	size_t operator()(BoardRow const& a) const
	{
		size_t res = 0;
		for (int i = 0; i < a.size(); ++i)
		{
			res <<= 1;
			res ^= a[i] ? 1 : 0;
		}
		return res;
	}
};
*/


struct comp
{
	size_t operator()(Position const& a, Position const& b) const
	{
		if (a.first.x == b.first.x && a.first.y == b.first.y)
			{
				for (int i = 0; i < a.second.size(); ++i)
				{
					for (int j = 0; j < a.second[0].size(); ++j)
					{
						if (a.second[i][j] != b.second[i][j])
						{
							return a.second[i][j];
						}
					}
				}
			return false;
		}
		else
		{
			if (a.first.x == b.first.x)
			{
				 return a.first.y < b.first.y;
			}
			else
			{
				return a.first.x < b.first.x;
			}
		}
	}
};

typedef map<Position, Players, comp> theemap;
theemap winner;

int rows;
int columns;

int xis[] = { 0, 0, 1, 1, 1, -1, -1, -1};
int yis[] = { 1, -1, 1, -1, 0, 1, -1, 0};

bool canMoveTo(Position const& aPosition, int moveX, int moveY)
{
	return aPosition.first.x + moveX >= 0 &&
		aPosition.first.x + moveX < aPosition.second[0].size() &&
		aPosition.first.y + moveY >= 0 &&
		aPosition.first.y + moveY < aPosition.second.size() &&
		aPosition.second[aPosition.first.y + moveY][aPosition.first.x + moveX];
}

bool canMoveLeft(Position const& aPosition)
{
	return aPosition.first.x > 0 && aPosition.second[aPosition.first.y][aPosition.first.x - 1];
}
bool canMoveRight(Position const& aPosition)
{
	return aPosition.first.x + 1< aPosition.second[0].size()
		&& aPosition.second[aPosition.first.y][aPosition.first.x + 1];
}
bool canMoveTop(Position const& aPosition)
{
	return aPosition.first.y > 0 && aPosition.second[aPosition.first.y - 1][aPosition.first.x];
}
bool canMoveBottom(Position const& aPosition)
{
	return aPosition.first.y  + 1 < aPosition.second.size() && aPosition.second[aPosition.first.y + 1][aPosition.first.x];
}
void burnCurrent(Position& aPosition)
{
	aPosition.second[aPosition.first.y][aPosition.first.x] = false;
}
void unburnCurrent(Position& aPosition)
{
	aPosition.second[aPosition.first.y][aPosition.first.x] = true;
}
void moveTo(Position& aPosition, int moveX, int moveY)
{
	aPosition.first.x += moveX;
	aPosition.first.y += moveY;
	burnCurrent(aPosition);
}
void unmoveTo(Position& aPosition, int moveX, int moveY)
{
	unburnCurrent(aPosition);
	aPosition.first.x -= moveX;
	aPosition.first.y -= moveY;
}

void moveLeft(Position& aPosition)
{
	--aPosition.first.x;
		burnCurrent(aPosition);
}
void  unmoveLeft(Position& aPosition)
{
	unburnCurrent(aPosition);
	++aPosition.first.x;
}
void  moveRight(Position& aPosition)
{
	++aPosition.first.x;
		burnCurrent(aPosition);
}
void  unmoveRight(Position& aPosition)
{
	unburnCurrent(aPosition);
	--aPosition.first.x;
}
void  moveTop(Position& aPosition)
{
	--aPosition.first.y;
		burnCurrent(aPosition);
}
void  unmoveTop(Position& aPosition)
{
	unburnCurrent(aPosition);
	++aPosition.first.y;
}
void  moveBottom(Position& aPosition)
{
	++aPosition.first.y;
		burnCurrent(aPosition);
}
void  unmoveBottom(Position& aPosition)
{
	unburnCurrent(aPosition);
	--aPosition.first.y;
}

void addSolution(Position const& aPosition, Players aPlayer)
{
	winner[aPosition] = aPlayer;
}

Players solve(Position const& aPosition)
{
	theemap :: const_iterator ite = 	winner.find(aPosition);
	if (ite != winner.end())
	{
		return ite->second;
	}
	else
	{
		Position newPos = aPosition;
		for (int m = 0; m < 8; m++)
		{
			if (canMoveTo(newPos, xis[m], yis[m]))
			{
				moveTo(newPos, xis[m], yis[m]);
				if (solve(newPos) == secondPlayer)
				{
					addSolution(aPosition, firstPlayer);
					return firstPlayer;
				}
				unmoveTo(newPos, xis[m], yis[m]);
			}
		}
		return secondPlayer;

		/*
		Position newPos = aPosition;
		if (canMoveLeft(newPos))
		{
			moveLeft(newPos);
			if (solve(newPos) == secondPlayer)
			{
				addSolution(aPosition, firstPlayer);
				return firstPlayer;
			}
			unmoveLeft(newPos);
		}
		if (canMoveRight(newPos))
		{
			moveRight(newPos);
			if (solve(newPos) == secondPlayer)
			{
				addSolution(aPosition, firstPlayer);
				return firstPlayer;
			}
			unmoveRight(newPos);
		}
		if (canMoveTop(newPos))
		{
			moveTop(newPos);
			if (solve(newPos) == secondPlayer)
			{
				addSolution(aPosition, firstPlayer);
				return firstPlayer;
			}
			unmoveTop(newPos);
		}
		if (canMoveBottom(newPos))
		{
			moveBottom(newPos);
			if (solve(newPos) == secondPlayer)
			{
				addSolution(aPosition, firstPlayer);
				return firstPlayer;
			}
			unmoveBottom(newPos);
		}
		*/
		return secondPlayer;
	}
}
int main(int /*argc*/, char* /*argv*/[])
{
	::std::ifstream testCasesStream("input.txt");
	::std::ofstream outputCasesStream("output.txt");
	unsigned int numberOfCases;
	testCasesStream >> numberOfCases;
	for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
	{
		Position initial;
		winner.clear();
		testCasesStream >> rows >> columns;
		testCasesStream .ignore(1);
		for (int r = 0; r < rows; ++r)
		{
			vector<bool> row;
			for (int c = 0; c< columns; ++c)
			{
				switch(testCasesStream.get())
				{
					case 'K':
						{

						initial.first.x = c;
						initial.first.y = r;
						row.push_back(false);
						break;
						}
					case '.':
						row.push_back(true);
						break;
					case '#':
						row.push_back(false);
						break;
					default:
						assert(false);

				}
			}
			initial.second.push_back(row);
			testCasesStream.ignore(1);
		}
		Players solution = solve(initial);
		outputCasesStream << "Case #" << caseIndex << ": " << ((solution == firstPlayer) ? "A" : "B") << "\n";
	}
	return 0;
}