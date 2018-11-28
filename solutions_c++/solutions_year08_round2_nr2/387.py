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
long long intervalStart, intervalEnd, minimum, totalNumbers;

typedef std::vector< long long> llv;
::std::vector< llv > primeFactors;
llv primeNumbers;
void addPrimesOfTo(unsigned int number, std::vector< long long>& factors)
{
    for (unsigned int i = 0; i < primeNumbers.size(); ++i)
    {
        if (number % primeNumbers[i] == 0)
        {
            factors.push_back(primeNumbers[i]);
        }
    }
    if (factors.empty())
    {
        primeNumbers.push_back(number);
        factors.push_back(number);
    }
}

void initialize(void)
{
    primeFactors.resize(1001);
    for (unsigned int i = 2; i <= 1000; ++i)
    {
        addPrimesOfTo(i, primeFactors[i]);
        ::std::sort(primeFactors[i].rbegin(), primeFactors[i].rend());
    }
}


bool testForUnite(long long i, long long j)
{
    BOOST_FOREACH(long long prime, primeFactors[i])
    {
        if (prime < minimum) return false;
        for (unsigned int k = 0; (k < primeFactors[j].size()); ++k)
        {
            if (prime == primeFactors[j][k]) 
            {
                return true;
            }
            if (prime > primeFactors[j][k]) break;
        }
    }
    return false;
}
long long solve(void)
{
    ::std::vector< std::vector< bool  > > graph(totalNumbers, std::vector< bool  >(totalNumbers, false));
    for (unsigned int i = 0; i < totalNumbers; ++i)
    {
        for (unsigned int j = i + 1; j < totalNumbers; ++j)
        {
            if (testForUnite(i + intervalStart, j + intervalStart))
            {
                graph[i][j] = true;
                graph[j][i] = true;
            }
        }
    }

    bool change = true;
    while (change)
    {
        change = false;

        for (unsigned int i = 0; i < totalNumbers; ++i)
        {
            for (unsigned int j = i + 1; j < totalNumbers; ++j)
            {
                if (graph[i][j]) continue;
                for (unsigned int k = minimum; k < totalNumbers; ++k)
                {
                    if (graph[i][k] && graph[k][j])
                    {
                        graph[i][j] = graph[j][i] = true;
                        change = true;
                    }
                }
            }
        }
    }

    ::std::set<long long> numbers;
    for (long long i = 0; i < totalNumbers; ++i)
    {
        for (long long j = 0; j < i; ++j)
        {
            if (graph[i][j])
            {
                goto contiii;
            }
        }
        numbers.insert(i);
        contiii:
        ;
    }
    return numbers.size();
}
void solveAndWrite(unsigned int aCaseIndex)
{
    long long solution = solve();
    outputFileStream << "Case #" << aCaseIndex << ": " << solution << ::std::endl;
}
void parseAndSolveCase(unsigned int aCaseIndex)
{
    inputFileStream >> intervalStart >> intervalEnd >> minimum;
    totalNumbers = intervalEnd - intervalStart + 1;
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
    initialize();
    parseAndSolveFile();
    return 0;
}
