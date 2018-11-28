// 4.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile;
	ofstream outFile;
	inputFile.open("D-large.in");
	outFile.open("D-large.out");
	int caseNumMax;
	outFile.setf(ios::fixed);
	outFile.precision(6);
	inputFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		int count;
		inputFile >> count;
		vector<int> tt;
		double result = 0;
		tt.push_back(0);
		int temp;
		for (int i = 0; i < count; ++i)
		{
			inputFile >> temp;
			tt.push_back(temp);
		}
		int onPos = 0;
		for (int i = 1; i < tt.size(); ++i)
		{
			if (i == tt.at(i))
				++onPos;
		}		
		result = count - onPos;
		outFile << "Case #" << caseNum + 1 << ": " << result << endl;

	}
	inputFile.close();
	outFile.close();
	return 0;
}


