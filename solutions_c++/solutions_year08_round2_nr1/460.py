//--------------------------------------------------------------------------------------------------
// Includes
//--------------------------------------------------------------------------------------------------
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cassert>
//--------------------------------------------------------------------------------------------------

::std::ifstream inputFileStream("input.txt");
::std::ofstream outputFileStream("output.txt");
long long n, A, B, C, D, x0, y0, M;

struct Coordinates
{
    long long x, y;
    Coordinates(long long anX, long long anY)
        : x(anX), y(anY)
    {

    }
};

long long solve(void)
{
    ::std::vector<Coordinates> coords;
    long long X = x0, Y = y0;
    unsigned int total = 0;
    coords.push_back(Coordinates(X, Y));
    for (unsigned int i = 1; i <= n - 1; ++i)
    {
        X = (A * X + B) % M;
        Y = (C * Y + D) % M;
        coords.push_back(Coordinates(X, Y));
    }
    for (unsigned int i = 0; i < coords.size(); ++i)
    {
        for (unsigned int j = i + 1; j < coords.size(); ++j)
        {
            for (unsigned int k = j + 1; k < coords.size(); ++k)
            {
                long long totalX = (coords[i].x + coords[j].x + coords[k].x);
                if ((coords[i].x + coords[j].x + coords[k].x) % 3 == 0)
                {
                    long long totalY = (coords[i].y + coords[j].y + coords[k].y);
                    if ((coords[i].y + coords[j].y + coords[k].y) % 3 == 0)
                    {
                        ++total;
                    }
                }
            }
        }
    }
    return total;
}
void solveAndWrite(unsigned int aCaseIndex)
{
    long long solution = solve();
    outputFileStream << "Case #" << aCaseIndex << ": " << solution << ::std::endl;
}
void parseAndSolveCase(unsigned int aCaseIndex)
{
    inputFileStream >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    solveAndWrite(aCaseIndex);
}
void parseAndSolveFile(void)
{
    unsigned int numberOfCases;
    inputFileStream >> numberOfCases;
    for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
    {
        parseAndSolveCase(caseIndex);
    }
}
int main(int /*argc*/, char* /*argv*/[])
{
    parseAndSolveFile();
    return 0;
}
