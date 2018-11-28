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

int solved(void)
{
    return 0;
}

::std::vector<int> digits;
::std::vector<int> sortedDigits;

bool solve(int fromIndex)
{
    if (fromIndex + 1 < digits.size())
    {
        if (solve(fromIndex + 1))
        {
            return true;
        }
        else
        {
            bool found = false;
            int bestDigit = 0;
            int bestIndex = 0;
            for (int i = fromIndex + 1; i < digits.size(); ++i)
            {
                if (digits[fromIndex] < digits[i])
                {
                    if (!found || bestDigit > digits[i])
                    {
                        found = true;
                        bestDigit = digits[i];
                        bestIndex = i;
                    }
                }
            }

    if (found)
    {
            ::std::swap(digits[fromIndex], digits[bestIndex]);
            ::std::sort(digits.begin() + fromIndex + 1, digits.end());
            return true;
            }

            return false;
        }
    }
    else
    {
        return false;
    }
}

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
    ::std::string number;
    ::std::getline(inputFileStream, number);
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
        ::std::getline(inputFileStream, number);
        digits.clear();
        BOOST_FOREACH(char digit, number)
        {
            digits.push_back(digit - '0');
        }

        sortedDigits = digits;
        ::std::sort(sortedDigits.rbegin(), sortedDigits.rend());
        if (sortedDigits == digits)
        {
            ::std::reverse(sortedDigits.begin(), sortedDigits.end());
            int i = 0;
            for (i = 0; i < sortedDigits.size() && (sortedDigits[i] == 0); ++i);
            std::swap(sortedDigits[i], sortedDigits[0]);
            sortedDigits.insert(sortedDigits.begin() + 1, 0);
            digits = sortedDigits;
        }
        else
        {
            solve(0);        
        }
        
        number.clear();
        BOOST_FOREACH(int digit, digits)
        {
            number.push_back(digit + '0');
        }

        //Print Solution
        outputFileStream << "Case #" << caseIndex << ": " << number << ::std::endl;
    }
    return 0;
}
