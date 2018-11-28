// 3.cpp: определяет точку входа для консольного приложения.
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
	inputFile.open("C-large.in");
	outFile.open("C-large.out");
	int caseNumMax;
	inputFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		vector<int> nums;
		int count;
		inputFile >> count;
		int curNum;
		long sum = 0;
		int min = 999999; 
		int check = 0;
		for (int i = 0; i < count; ++i)
		{
			inputFile >> curNum;
			if (curNum < min)
				min = curNum;
			sum += curNum;
			check = check ^ curNum;
		}
		outFile << "Case #" << caseNum + 1 << ": ";
		if (check)
			outFile << "NO";
		else
			outFile << sum - min;
		outFile << endl;
	}
	inputFile.close();
	outFile.close();
	return 0;
}

