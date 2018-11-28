#include <iostream>
#include <fstream>

#include <vector>
#include <set>
#include <map>

using namespace std;



void MultipleBigNum(int bigNum[], int maxDigit, int multiplier)
{
	int i;
	int carry, thisDigit;
	carry = 0;
	for (i = 0; i < maxDigit; ++i)
	{
		thisDigit = bigNum[i] * multiplier + carry;
		carry = thisDigit / 10;
		bigNum[i] = thisDigit % 10;
	}
}

// bigNum1 <- bigNum1 + bigNum2
void AddBigNum(int bigNum1[], int bigNum2[], int maxDigit)
{
	int i;
	int carry, thisDigit;
	carry = 0;
	for (i = 0; i < maxDigit; ++i)
	{
		thisDigit = bigNum1[i] + bigNum2[i] + carry;
		carry = thisDigit / 10;
		bigNum1[i] = thisDigit % 10;
	}
}

void CopyBigNum(int bigNumDest[], int bigNumSrc[], int maxDigit)
{
	int i;
	for (i = 0; i < maxDigit; ++i)
		bigNumDest[i] = bigNumSrc[i];
}



int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");

	int T, X;
	char lineBuf[63];
	int lineLen;

	int resultDecTemp[20];
	int resultAdd[20];
	int resultDigit[20];

	int symbolNum;
	set<char> symbolSet;

	map<char, int> numberSymbol;
	map<char, int>::iterator mapFindIt;
	int thisMinMultiplier;

	int base;

	int thisMultiplier;
	int maxDigit;

	int i, j;

	inputFile>>T;
	for (X = 1; X <= T; ++X)
	{
		inputFile>>lineBuf;
		lineLen = strlen(lineBuf);

		symbolSet.clear();
		for (i = 0; i < lineLen; ++i)
			symbolSet.insert(lineBuf[i]);
		symbolNum = symbolSet.size();

		base = symbolNum == 1 ? 2 : symbolNum;
		numberSymbol.clear();
		numberSymbol.insert(pair<char, int>(lineBuf[0], 1));
		thisMinMultiplier = 0;
		for (i = 1; i < lineLen; ++i)
		{
			mapFindIt = numberSymbol.find(lineBuf[i]);
			if (mapFindIt == numberSymbol.end())
			{
				numberSymbol.insert(pair<char, int>(lineBuf[i], thisMinMultiplier));
				thisMinMultiplier = thisMinMultiplier == 0 ? 2 : thisMinMultiplier + 1;
			}
		}

		for (i = 0; i < 20; ++i)
		{
			resultDecTemp[i] = 0;
			resultDigit[i] = 0;
		}

		resultDigit[0] = 1;
		for (i = lineLen - 1; i >= 0; --i)
		{
			mapFindIt = numberSymbol.find(lineBuf[i]);
			thisMultiplier = mapFindIt->second;
			CopyBigNum(resultAdd, resultDigit, 20);
			MultipleBigNum(resultAdd, 20, thisMultiplier);
			AddBigNum(resultDecTemp, resultAdd, 20);
			MultipleBigNum(resultDigit, 20, base);
		}

		outputFile<<"Case #"<<X<<": ";
		
		for (maxDigit = 19; maxDigit >= 0; --maxDigit)
		{
			if (resultDecTemp[maxDigit] != 0)
				break;
		}
		for (i = maxDigit; i >= 0; --i)
			outputFile<<resultDecTemp[i];

		outputFile<<endl;
	}

	inputFile.close();
	outputFile.close();
}
