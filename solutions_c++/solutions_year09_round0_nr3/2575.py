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
#include <boost/lexical_cast.hpp> //WWW.BOOST.ORG LIBRARY USED
//--------------------------------------------------------------------------------------------------


::std::ifstream inputFileStream("input.txt");
::std::ofstream outputFileStream("output.txt");

::std::string line;

::std::vector< ::std::vector<int> > result;

::std::string subline = "welcome to code jam";

void increaseBy(int& aPos, int aValue)
{
	aPos += aValue/* % 10000*/;
	//aPos %= 10000;
}

int count(int lineIndex, int sublineIndex)
{
	int& res = result[lineIndex][sublineIndex];
	if (res == -1)
	{
		res = 0;
		if (lineIndex != 0)
		{
			res += count(lineIndex - 1, sublineIndex);
		}
		if (line[lineIndex] == subline[sublineIndex])
		{
			if (sublineIndex == 0)
			{
				res += 1;
			}
			else if (lineIndex == 0)
			{
			}
			else
			{
				res += count(lineIndex - 1, sublineIndex - 1);
			}
		}
		res %= 1000;
	}
	return res;
}

int solutionFor(::std::string const& )
{
	result.resize(line.size(), ::std::vector<int>(subline.size(), -1));
	return count(line.size() - 1, subline.size() - 1);
}

int solutionFor2(::std::string const& line)
{
	result.resize(line.size(), ::std::vector<int>(subline.size(), 0));
	int total = 0;
	for (size_t lineIndex = 0; lineIndex < line.size(); ++lineIndex)
	{
		if (line[lineIndex] == subline[0])
		{
			++total;
		}
		result[lineIndex][0] = total;
	}

	for (size_t lineIndex = 1; lineIndex < line.size(); ++lineIndex)
	{
		for (size_t sublineIndex = 1; sublineIndex < subline.size(); ++sublineIndex)
		{
			increaseBy(result[lineIndex][sublineIndex], result[lineIndex - 1][sublineIndex]);
			if (subline[sublineIndex] == line[lineIndex])
			{
				increaseBy(result[lineIndex][sublineIndex], result[lineIndex - 1][sublineIndex - 1]);
			}
		}
	}
	return result[line.size() - 1][subline.size() - 1];
}

int main(int /*argc*/, char* /*argv*/[])
{
    unsigned int totalCasesCount;
    inputFileStream >> totalCasesCount;
	::std::getline(inputFileStream, line);
    for (unsigned int caseIndex = 1; caseIndex <= totalCasesCount; ++caseIndex)
    {
		::std::getline(inputFileStream, line);
		result.clear();
		int sol = solutionFor(line);
		::std::string text = ::boost::lexical_cast< ::std::string >(sol);
		while (text.size() < 4)
		{
			text = "0" + text;
		}
		outputFileStream << "Case #" << caseIndex << ": " << text << ::std::endl;
    }
    return 0;
}
