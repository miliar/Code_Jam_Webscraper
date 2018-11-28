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

::std::string originalString;
unsigned int K;

::std::vector<bool> isNumberUsed;
::std::vector<int>  permutation;
int best = -1;

::std::set< ::std::vector<int> >  allpermutation;
unsigned int createSinglePermutation()
{
    unsigned int differentLetters = 1;
    char lastLetter = originalString[permutation[0]];
    unsigned int nextPerm = 1;
    for (unsigned int i = 1; i < originalString.size(); ++i, ++nextPerm)
    {
        if (nextPerm >= K)
        {
            nextPerm = 0;
        }
        char newLetter = originalString[(i - nextPerm) + permutation[nextPerm]];
        if (lastLetter != newLetter)
        {
            ++differentLetters;
        }
        else
        {
            differentLetters = differentLetters;
        }
        lastLetter = newLetter;
    }
    return differentLetters;
};

void calculate()
{
    unsigned int len = createSinglePermutation();
    if (best == -1)
    {
        best = len;
    }
    else if (len < best)
    {
        best = len;
    }
}

void createPermutation()
{
    if (K == permutation.size())
    {
        calculate();
    }
    else
    {
        for (unsigned int i = 0; i < isNumberUsed.size(); ++i)
        {
            if (isNumberUsed[i] == false)
            {
                isNumberUsed[i] = true;
                permutation.push_back(i);
                createPermutation();
                permutation.pop_back();
                isNumberUsed[i] = false;
            }
        }
    }
}


typedef int Number;
int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int numberOfCases;
    inputFileStream >> numberOfCases;
    for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
    {
        best = -1;
        inputFileStream >> K;
        ::std::getline(inputFileStream, originalString);
        ::std::getline(inputFileStream, originalString);
        isNumberUsed.resize(K, false);
        permutation.clear();
        createPermutation();
        outputFileStream << "Case #" << caseIndex << ": " << best << ::std::endl;
    }
    return 0;
}
