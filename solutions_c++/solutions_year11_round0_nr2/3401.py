#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

#define ELEMENTS_SIZE 8

static string baseElements = "QWERASDF";
static char combineTable[ELEMENTS_SIZE][ELEMENTS_SIZE];
static int opposeTable[ELEMENTS_SIZE][ELEMENTS_SIZE];
vector<char> elementsList;

size_t getElementIndex(char c) { return baseElements.find_first_of(c); }

void updateCombineTable(string &s)
{
	combineTable[getElementIndex(s[0])][getElementIndex(s[1])] = s[2];
	combineTable[getElementIndex(s[1])][getElementIndex(s[0])] = s[2];
}

void updateOpposeTable(string &s)
{
	opposeTable[getElementIndex(s[0])][getElementIndex(s[1])] = 1;
	opposeTable[getElementIndex(s[1])][getElementIndex(s[0])] = 1;
}

char combine(char c1, char c2)
{
	size_t i1 = getElementIndex(c1);
	size_t i2 = getElementIndex(c2);

	if (i1 == string::npos || i2 == string::npos)
		return '.';

	if (combineTable[i1][i2] != '.')
		return combineTable[i1][i2];

	return combineTable[i2][i1];
}

bool oppose(char c)
{
	size_t i1,i2;
	i1 = getElementIndex(c);
	if (i1 == string::npos)
		return false;

	for (int i=0;i<elementsList.size();i++)
	{
		i2 = getElementIndex(elementsList[i]);

		if (i2 == string::npos)
			continue;

		if (opposeTable[i1][i2] == 1 || opposeTable[i2][i1] == 1)
			return true;
	}

	return false;
}

void addToElementsList(char c)
{
	if (elementsList.size() > 0)
	{
		char c2 = elementsList[elementsList.size()-1];
		char retVal = combine(c,c2);
		if (retVal != '.' )
		{
			int i = elementsList.size()-1;
			elementsList[i] = retVal;
			return;
		}
	}

	if (oppose(c))
	{
		elementsList.clear();
		return;
	}

	elementsList.push_back(c);
}

void init()
{
	elementsList.clear();

	for (int i=0;i<ELEMENTS_SIZE;i++)
		for (int j=0;j<ELEMENTS_SIZE;j++)
		{
			combineTable[i][j] = '.';
			opposeTable[i][j] = 0;
		}
}

int main()
{
	ifstream inputFile;
	inputFile.open("B-small.in");
	ofstream outputFile;
	outputFile.open("B.out");
	int T;
	vector<string> output;

	inputFile >> T;

	for (int t=1;t<=T;t++)
	{
		init();
		int C,D,N;

		inputFile >> C;
		for (int c=0;c<C;c++)
		{
			string s;
			inputFile >> s;
			//cout << s << endl;
			updateCombineTable(s);
		}

		inputFile >> D;
		for (int d=0;d<D;d++)
		{
			string s;
			inputFile >> s;
			//cout << s << endl;
			updateOpposeTable(s);
		}

		inputFile >> N;
		for (int n=0;n<N;n++)
		{
			char c;
			inputFile >> c;
			addToElementsList(c);
		}

		ostringstream outStr;
		outStr << "Case #" << t << ": [";
		for (int i=0;i<elementsList.size();)
		{
			outStr << elementsList[i];
			if (++i < elementsList.size())
				outStr << ", ";
		}
		outStr << "]";
		outputFile << outStr.str() << endl;
	}

	inputFile.close();
	outputFile.close();
}
