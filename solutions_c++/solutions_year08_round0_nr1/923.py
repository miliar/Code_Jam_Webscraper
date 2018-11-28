
#include <stdio.h>
#include <string.h>

#include <string>
#include <iostream>
#include <fstream>

enum Const
{
	MAX_S_NUM		= 100,
	MAX_Q_NUM		= 1000
};

int main()
{
	std::ifstream inputFile;
	inputFile.open("A-large.in");
	std::ofstream outputFile;
	outputFile.open("A-large.out");

	std::string strTemp;

	std::getline(inputFile, strTemp);
	int iCaseNum = atoi(strTemp.c_str());

	std::string astrSType[MAX_S_NUM];
	unsigned char ucQuerySet[MAX_Q_NUM] = { 0, };
	bool abCheck[MAX_S_NUM];

	for (int i = 0; i < iCaseNum; ++i)
	{
		memset(abCheck, false, MAX_S_NUM);

		std::getline(inputFile, strTemp);
		int iS= atoi(strTemp.c_str());

		for (int j = 0; j < iS; ++j)
		{
			std::getline(inputFile, astrSType[j]);
		}

		std::getline(inputFile, strTemp);
		int iQ = atoi(strTemp.c_str());

		for (int j = 0; j < iQ; ++j)
		{
			std::string strQ;
			std::getline(inputFile, strQ);

			for (int k = 0; k < iS; ++k)
			{
				if (astrSType[k] == strQ)
				{
					ucQuerySet[j] = k;
					break;
				}
			}
		}

		int iSmallestSwitchNum = 0;

		int iCounter = 0;
		for (int j = 0; j < iQ; ++j)
		{
			if (false == abCheck[ucQuerySet[j]])
			{
				abCheck[ucQuerySet[j]] = true;
				++iCounter;

				if (iCounter == iS)
				{
					memset(abCheck, false, MAX_S_NUM);
					abCheck[ucQuerySet[j]] = true;
					iCounter = 1;

					++iSmallestSwitchNum;
				}
			}
		}

		outputFile << "Case #" << i + 1 << ": " << iSmallestSwitchNum << std::endl;
	}

	outputFile.close();
	inputFile.close();
}