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
#include <boost/foreach.hpp> //WWW.BOOST.ORG LIBRARY USED
//--------------------------------------------------------------------------------------------------


::std::ifstream inputFileStream("input.txt");
::std::ofstream outputFileStream("output.txt");

const int Infinite = 100000;

typedef ::std::pair<int, int> coords;
::std::vector< ::std::vector< int > > map;
::std::vector< coords > positionsToTryFrom;
        int originX, originY;
        int targetX, targetY;

bool isWall(coords aCoord)
{
    return map[aCoord.first][aCoord.second] == -1;
}
bool isTarget(coords aCoord)
{
    return aCoord.first == targetX && aCoord.second == targetY;
}

void writeNewCost(coords aCoord, int aNewCost)
{
    int coost = map[aCoord.first][aCoord.second];
    if (aNewCost < coost)
    {
        map[aCoord.first][aCoord.second] = aNewCost;
        positionsToTryFrom.push_back(aCoord);
    }
}
coords wallToUp(coords aCoord)
{
    coords newCoord = aCoord;
    while (!isWall(newCoord))
    {
        if (newCoord.second == 0)
        {
            return newCoord;
        }
        --newCoord.second;
    }
    ++newCoord.second;
    return newCoord;
}
coords wallToDown(coords aCoord)
{
    coords newCoord = aCoord;
    while (!isWall(newCoord))
    {
        ++newCoord.second;
        if (newCoord.second == map[0].size())
        {
            --newCoord.second;
            return newCoord;
        }
    }
    --newCoord.second;
    return newCoord;
}
coords wallToLeft(coords aCoord)
{
    coords newCoord = aCoord;
    while (!isWall(newCoord))
    {
        if (newCoord.first == 0)
        {
            return newCoord;
        }
        --newCoord.first;
    }
    ++newCoord.first;
    return newCoord;
}
coords wallToRight(coords aCoord)
{
    coords newCoord = aCoord;
    while (!isWall(newCoord))
    {
        ++newCoord.first;
        if (newCoord.first == map.size())
        {
            --newCoord.first;
            return newCoord;
        }
    }
    --newCoord.first;
    return newCoord;
}
bool isValid(coords aCoord)
{
    return aCoord.first >= 0 && aCoord.first < map.size() &&
        aCoord.second >= 0 && aCoord.second  < map[0].size();
}
void tryFrom(coords aCoord)
{
    int coost = map[aCoord.first][aCoord.second];
    coords newCoord(aCoord);
    ++newCoord.first;
    bool hasWall = false;
    if (isValid(newCoord))
    {
    if (!isWall(newCoord))
    {
        writeNewCost(newCoord, coost + 1);
    }
    else
    {
        hasWall = true;
    }
    }
    else
    {
        hasWall = true;
    }
    --newCoord.first;

    --newCoord.first;
    if (isValid(newCoord))
    {
    if (!isWall(newCoord))
    {
        writeNewCost(newCoord, coost + 1);
    }
    else
    {
        hasWall = true;
    }
    }
    else
    {
        hasWall = true;
    }
    ++newCoord.first;

    --newCoord.second;
    if (isValid(newCoord))
    {
    if (!isWall(newCoord))
    {
        writeNewCost(newCoord, coost + 1);
    }
    else
    {
        hasWall = true;
    }
    }
    else
    {
        hasWall = true;
    }
    ++newCoord.second;

    ++newCoord.second;
    if (isValid(newCoord))
    {
    if (!isWall(newCoord))
    {
        writeNewCost(newCoord, coost + 1);
    }
    else
    {
        hasWall = true;
    }
    }
    else
    {
        hasWall = true;
    }
    --newCoord.second;

    if (hasWall)
    {
        writeNewCost(wallToUp(newCoord), coost + 1);
        writeNewCost(wallToDown(newCoord), coost + 1);
        writeNewCost(wallToLeft(newCoord), coost + 1);
        writeNewCost(wallToRight(newCoord), coost + 1);
    }
}

::std::vector< ::std::string > drawnMap;
int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        //Read Instance Data
        unsigned int rowsCount, columnsCount;
        inputFileStream >> rowsCount >> columnsCount;
        map.clear();
        positionsToTryFrom.clear();
        map.resize(columnsCount, ::std::vector< int >(rowsCount, Infinite));
        //drawnMap.resize(columnsCount, ::std::string(rowsCount, '.'));
        ::std::string line;
        for (int currentY = 0; currentY < rowsCount; ++currentY)
        {
            line.clear();
            while (line.empty())
            ::std::getline(inputFileStream, line);
            for (int currentX = 0; currentX < line.size(); ++currentX)
            {
                switch (line[currentX])
                {
                    case 'O':
                        originX = currentX;
                        originY = currentY;
                        map[currentX][currentY] = 0;
                        //drawnMap[currentX][currentY] = 'O';
                        break;
                    case '.':
                        break;
                    case 'X':
                        targetX = currentX;
                        targetY = currentY;
                        //drawnMap[currentX][currentY] = 'X';
                        break;
                    case '#':
                        map[currentX][currentY] = -1;
                        //drawnMap[currentX][currentY] = '#';
                        break;
                }
            }
        }
        //Solve Instance Data
        positionsToTryFrom.push_back(coords(originX, originY));
        while (positionsToTryFrom.size() > 0)
        {
            coords nextToTry = positionsToTryFrom[positionsToTryFrom.size() - 1];
            positionsToTryFrom.pop_back();
            tryFrom(nextToTry);
        }

        //Print Solution
        if (map[targetX][targetY] == Infinite)
        {
        outputFileStream << "Case #" << caseIndex << ": " << "THE CAKE IS A LIE" << ::std::endl;
        }
        else
        {
            outputFileStream << "Case #" << caseIndex << ": " << map[targetX][targetY] << ::std::endl;
        }
    }
    return 0;
}
