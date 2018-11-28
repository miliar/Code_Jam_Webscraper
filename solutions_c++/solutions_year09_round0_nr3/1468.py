#include <string>
#include <fstream>
#include <set>
#include <vector>
#include <iostream>
#include <map>

using std::string;
using std::map;
using std::vector;
using std::pair;
using std::set;

using std::fstream;
using std::istream;
using std::ostream;

using std::cin;
using std::cout;

#define NUMBER 10000

class SubstringFinder
{
	int FindString(const string &targetString, int currentSubstringLenght, int position)
	{
		if (currentSubstringLenght == targetString.size())
			return 1;

		int result = 0;
		for (int newPosition = position; newPosition < innerString.size(); ++newPosition)
		{
			if (innerString[newPosition] == targetString[currentSubstringLenght])
			{
				result += FindString(targetString, currentSubstringLenght + 1, newPosition);
				result %= maxNumber;
			}
		}
		return result;
	}

public:
	string innerString;
	int maxNumber;

	SubstringFinder(int n) : maxNumber(n) {};

	int SubstringNumber(const string &s)
	{
		string pushInnerString = innerString;

		innerString = "";

		set<char> usedSymbols;
		for (int i = 0; i < s.size(); ++i)
			usedSymbols.insert(s[i]);

		for (int i = 0; i < pushInnerString.size(); ++i)
			if (usedSymbols.find(pushInnerString[i]) != usedSymbols.end())
				innerString += pushInnerString[i];

		char ch = 'k';
		return FindString(s, 0, 0);

		innerString = pushInnerString;
	}

	int SubstringNumber2(const string &s)
	{
		vector<map<int, int> > strangeNumbers(innerString.size());

		pair<int, int> p(0, 1);

		for (int i = 0; i < innerString.size(); ++i)
			if (innerString[i] == s[0])
			{
				strangeNumbers[i].insert(p);
			}

		for (int curChar = 1; curChar < s.size(); ++curChar)
		{
			for (int i = 0; i < innerString.size(); ++i)
				if (innerString[i] == s[curChar])
				{
					int tmp = 0;
					for (int j = 0; j < i; ++j)
					{
						if (strangeNumbers[j].find(curChar - 1) != strangeNumbers[j].end())
						{
							tmp += strangeNumbers[j][curChar - 1];
							tmp %= NUMBER;
						}
					}
					pair<int, int> p(curChar, tmp);
					strangeNumbers[i].insert(p);
				}
		}

		int result = 0;
		
		for (int i = 0; i < innerString.size(); ++i)
			if (strangeNumbers[i].find(s.size() - 1) != strangeNumbers[i].end())
			{
				result += strangeNumbers[i][s.size() - 1];
				result %= NUMBER;
			}

		return result % NUMBER;
	}

	friend istream& operator >> (istream &input, SubstringFinder &sFinder)
	{
		char str [1000];
		input.getline(str, 1000);
		sFinder.innerString = str;
		return input;
	}
};

int Digits(int n)
{
	if (n == 0)
		return 1;

	int tmpN = n;
	int result = 0;

	while (tmpN >= 10)
	{
		++result;
		tmpN /= 10;
	}

	if (tmpN != 0)
		++result;

	return result;		
}

int main()
{
	fstream input("input.txt", std::ios::in);
	fstream output("output.txt", std::ios::out);

	int testNumber;

	input >> testNumber;

	char tmp[500];
	input.getline(tmp, 500);

	for (int i = 0; i < testNumber; ++i)
	{
		SubstringFinder sF(NUMBER);
		input >> sF;
		output << "Case #" << (i + 1) << ": ";
		
		int toOutput = sF.SubstringNumber2("welcome to code jam");

		for (int i = 0; i < Digits(NUMBER) - Digits(toOutput) - 1; ++i)
			output << 0;

		output << toOutput << std::endl;
	}

	return 0;
}