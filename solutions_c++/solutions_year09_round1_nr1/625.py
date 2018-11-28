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

::std::ifstream inputFileStream("input.in");
::std::ofstream outputFileStream("output.txt");

::std::vector<int> bases;

enum IsHappy
{
    Happy,
    NotHappy,
    Unknown
};

#define BASES_COUNT = 11
typedef ::std::vector<IsHappy>  Number_IsHappy;
::std::vector< Number_IsHappy > number_is_happy;

Number_IsHappy defaultNumber_IsHappy;

int squares[11][11];

void init_square()
{
    for (int i = 2; i <= 10; ++i)
    {
        for (int j = 0; j <= i; ++j)
        {
            squares[i][j] = j * j;
        }
    }
}
::std::vector<int> changeBase(int number, int base)
{
    ::std::vector<int> res;
    while (number != 0)
    {
        int resto = number % base;
        res.push_back(resto);
        number /= base;
    }
    ::std::reverse(res.begin(), res.end());
    return res;
}

int resultOfCalc(int number, int base)
{
    ::std::vector<int> res = changeBase(number, base);
    int resslult = 0;
    BOOST_FOREACH(int d, res)
    {
        resslult += squares[base][d];
    }
    return resslult;
}

void resolveHappyForBase(int number, int base)
{
    if (number_is_happy.size() < number + 1)
    {
        number_is_happy.resize(number + 1, defaultNumber_IsHappy);
    }
    if (number_is_happy[number][base] == Unknown)
    {
        int res = resultOfCalc(number, base);
        number_is_happy[number][base] = NotHappy;
        resolveHappyForBase(res, base);
        number_is_happy[number][base] = number_is_happy[res][base];
    }
}
void resolveHappyFor(int number)
{
    if (number_is_happy.size() < number + 1)
    {
        number_is_happy.resize(number + 1, defaultNumber_IsHappy);
    }
    Number_IsHappy& happ = number_is_happy[number];
    BOOST_FOREACH(int base, bases)
    {
        resolveHappyForBase(number, base);
    }
}
bool isHappyInAllBases(int number)
{
    Number_IsHappy const& happ = number_is_happy[number];
    BOOST_FOREACH(int base, bases)
    {
        if (happ[base] != Happy )
        {
            return false;
        }
    }
    return true;
}
int solved(void)
{
    for (int i = 2;; ++i)
    {
        resolveHappyFor(i);
        if (isHappyInAllBases(i))
        {
            return i;
        }
    }
    return 0;
}
int main(int /*argc*/, char* /*argv*/[])
{
    init_square();
    defaultNumber_IsHappy.resize(11);
    number_is_happy.resize(2, defaultNumber_IsHappy);
    for (int i = 0; i <= 10; ++i)
    {
        defaultNumber_IsHappy[i] = Unknown;
        number_is_happy[0][i] = NotHappy;
        number_is_happy[1][i] = Happy;
    }
    
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
        ::std::string basesline;
        ::std::getline(inputFileStream, basesline);
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        bases.clear();
        ::std::getline(inputFileStream, basesline);
        ::std::istringstream stream(basesline);
        stream.peek();
        while (!stream.eof())
        {
            int base;
            stream >> base;
            bases.push_back(base);
            stream.peek();
        }
        //Print Solution
        outputFileStream << "Case #" << caseIndex << ": " << solved() << ::std::endl;
    }
    return 0;
}
