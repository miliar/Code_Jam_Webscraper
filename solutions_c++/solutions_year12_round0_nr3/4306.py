#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>

std::string intToString(int x)
{
	std::stringstream ss;
	ss << x;
	return ss.str();
}

int stringToInt(std::string s)
{
	return atoi(s.c_str());
}

int recycled(int a, int b)
{
	std::string iStr, jStr, backStr, testStr;

	int testIn;
	int count = 0;

	for (int i = a; i <= b; ++i)
	{
		iStr = intToString(i);

		for (int j = i; j <= b; ++j)
		{
			jStr = intToString(j);
			for (int k = 1; k != (jStr.length()); ++k)
			{
				testStr = jStr.substr((jStr.length() - k), (k+1));
				backStr = jStr.substr(0, (jStr.length() - (k)));
				testStr.append(backStr);

				if (testStr == iStr)
				{
					testIn = stringToInt(testStr);

					if ((testIn != j) && (a <= i) && (i <= j) && (testIn <= b))
					{
						++count;
					}

				}
			}
		}
	}
	return count;
}


int main()
{
	int t, aIn, bIn, numPairs;
	int caseNum = 1;
	std::string aStr, bStr, filename;
	std::ofstream outFile("output.txt", std::ios::out);
	
	std::cout << "Input filename:  ";

	std::cin >> filename;

	std::ifstream inputFile (filename, std::ios::in);

	if (!inputFile)
	{
		std::cout << "Bad filename";
	}
	
	inputFile >> t;

	if ((t > 50) || (t < 1))
	{
		outFile << "BAD T, try again";
		std::cout << "BAD T, try again";
		return 1;
	}

	while (inputFile >> aIn >> bIn)
	{

		if ((aIn > bIn) || (aIn < 1) || (bIn > 1000))
		{
			std::cout << "ERROR:  #s are not in format of 1<=A<=B<=1000";
			return 1;
		}

		aStr = intToString(aIn);
		bStr = intToString(bIn);

		if (aStr.length() != bStr.length())
		{
			std::cout << "ERROR:  A & B do not have the same number of digits";
			return 2;
		}

		outFile << "Case #" << caseNum << ": ";

		numPairs = recycled(aIn, bIn);

		outFile << numPairs;

		outFile << "\n";
		++caseNum;
	}

	return 0;
}