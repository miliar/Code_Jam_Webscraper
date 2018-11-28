// 1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-large.in");
	outFile.open("A-large.out");
	int caseNumMax;
	inFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		string result;
		int D, G;
		long long N;
		inFile >> N >> D >> G;
		result = "Broken";
		if (!( ((G == 0) || (G == 100)) && (G != D) ))
		{
			if (N >= 100)
				result = "Possible";
			else
			{
				for (int i = 1; i <= N; ++i)
				{
					if ( ((i * D) % 100) == 0 )
					{
						result = "Possible";
						break;
					}
				}
			}
		}
		outFile << "Case #" << caseNum + 1 << ": " << result << endl;

	}
	inFile.close();
	outFile.close();
	return 0;
}