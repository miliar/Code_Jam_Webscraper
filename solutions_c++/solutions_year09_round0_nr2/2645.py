//--------------------------------------------------------------------------------------------------
// Includes
//--------------------------------------------------------------------------------------------------
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cassert>
#include <set>
#include <map>
#include <boost/foreach.hpp> //WWW.BOOST.ORG LIBRARY USED
//--------------------------------------------------------------------------------------------------


::std::ifstream inputFileStream("input.txt");
::std::ofstream outputFileStream("output.txt");
unsigned int rowsCount, columnsCount;

typedef ::std::pair<int, int> coords;
coords NullCoord = coords(-1, -1);
::std::vector< ::std::vector< int > > heightsMap;

::std::vector< ::std::vector< coords > > cellsToSinkMap;

::std::map< coords, ::std::vector< coords > > sinkToCellsMap;

::std::vector< ::std::vector< char > > lettersMap;

int arrayX [] = {0, -1, 1, 0};
int arrayY [] = {-1, 0, 0, 1};
void calculateSinkOf(int currentX, int currentY)
{
	if (cellsToSinkMap[currentY][currentX] == NullCoord)
	{
		coords current = coords(currentX, currentY);
		coords sinkCoords = current;
		int bestHeight = heightsMap[currentY][currentX];
		for (int i = 0; i < 4; ++i)
		{
			int x = currentX + arrayX[i];
			int y = currentY + arrayY[i];
				if (x < 0) continue;
				if (y < 0) continue;
				if (x >= columnsCount) continue;
				if (y >= rowsCount) continue;
				if (bestHeight > heightsMap[y][x])
				{
					calculateSinkOf(x, y);
					bestHeight = heightsMap[y][x];
					sinkCoords = cellsToSinkMap[y][x];
				}
		}
		cellsToSinkMap[currentY][currentX] = sinkCoords;
		sinkToCellsMap[sinkCoords].push_back(current);
	}
}

void paintLetter(coords const& sink, char letter)
{
	BOOST_FOREACH(coords where, sinkToCellsMap[sink])
	{
		lettersMap[where.second][where.first] = letter;
	}
}

void solve()
{
	for (int currentY = 0; currentY < rowsCount; ++currentY)
	{
		for (int currentX = 0; currentX < columnsCount; ++currentX)
		{
			calculateSinkOf(currentX, currentY);
		}
	}

	char letter = 'a';
	for (int currentY = 0; currentY < rowsCount; ++currentY)
	{
		for (int currentX = 0; currentX < columnsCount; ++currentX)
		{
			if (lettersMap[currentY][currentX] == ' ')
			{
				paintLetter(cellsToSinkMap[currentY][currentX], letter++);
			}
		}
	}
}

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        //Read Instance Data
        inputFileStream >> rowsCount >> columnsCount;
        heightsMap.clear();
        heightsMap.reserve(rowsCount);
		cellsToSinkMap.clear();
		cellsToSinkMap.resize(rowsCount, ::std::vector< coords >(columnsCount, NullCoord));
		sinkToCellsMap.clear();
		lettersMap.clear();
		lettersMap.resize(rowsCount, ::std::vector< char >(columnsCount, ' '));
		
		::std::vector< int > heightsLine;
        for (int currentY = 0; currentY < rowsCount; ++currentY)
        {
			heightsLine.clear();
            for (int currentX = 0; currentX < columnsCount; ++currentX)
            {
				int height;
				inputFileStream >> height;
				heightsLine.push_back(height);
            }
			heightsMap.push_back(heightsLine);
        }

		solve();

		outputFileStream << "Case #" << caseIndex << ":" << ::std::endl;
		for (int currentY = 0; currentY < rowsCount; ++currentY)
		{
			for (int currentX = 0; currentX < columnsCount; ++currentX)
			{
				if (currentX != 0) outputFileStream << " ";
				outputFileStream << lettersMap[currentY][currentX];
			}
			outputFileStream << ::std::endl;
		}
    }
    return 0;
}
