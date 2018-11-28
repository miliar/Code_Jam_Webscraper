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

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        //Read Instance Data
        unsigned int height, width, rocksCount;
        ::std::vector< ::std::vector< int > > places;

        inputFileStream >> height >> width >> rocksCount;
        places.resize(width, ::std::vector< int >(height, 0));
        for (int i = 0; i < rocksCount; ++i)
        {
            int x, y;
            inputFileStream >> y >> x;
            places[x - 1][y - 1] = -1;
        }
        places[width - 1][height - 1] = 1;
        //Solve Instance Data
        for (int x = width - 1; x >= 0; --x)
        {
            for (int y = height - 1; y >= 0; --y)
            {
                if (x == width - 1 && y == height -1) continue;
                if (places[x][y] == -1) continue;
                int res = 0;
                if ((x + 2 < width) && (y + 1 < height))
                {
                    if (places[x + 2][y + 1] != - 1)
                        res += places[x + 2][y + 1];
                }
                if ((x + 1 < width) && (y + 2 < height))
                {
                    if (places[x + 1][y + 2] != - 1)
                        res += places[x + 1][y + 2];
                }
                places[x][y] = res % 10007;
            }
        }

        //Print Solution
        outputFileStream << "Case #" << caseIndex << ": " << places[0][0] << ::std::endl;
    }
    return 0;
}
