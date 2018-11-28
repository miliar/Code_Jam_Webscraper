// 1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile;
	ofstream outFile;
	inputFile.open("A-large.in");
	outFile.open("A-large.out");
	int caseNumMax;
	inputFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		int buttons;
		inputFile >> buttons;
		int oPos = 1;
		int bPos = 1;
		int oDelta = 0;
		int bDelta = 0;
		char curRobot;
		int curPos;
		int result = 0;
		int diff;
		for (int button = 0; button < buttons; ++button)
		{
			inputFile >> curRobot >> curPos;
			if (curRobot == 'O')
			{
				diff = abs(curPos - oPos);
				oDelta += diff;
				oPos = curPos;
				if (oDelta <= bDelta)
				{
					oDelta = 1;
					result += bDelta;
					bDelta = 0;
				}
				else
				{
					oDelta = oDelta - bDelta + 1;
					result += bDelta;
					bDelta = 0;
				}
			}
			else if (curRobot == 'B')
			{
				diff = abs(curPos - bPos);
				bDelta += diff;
				bPos = curPos;
				if (bDelta <= oDelta)
				{
					bDelta = 1;
					result += oDelta;
					oDelta = 0;
				}
				else
				{
					bDelta = bDelta - oDelta + 1;
					result += oDelta;
					oDelta = 0;
				}
			}
		}
		result += oDelta + bDelta;
		outFile << "Case #" << caseNum + 1 << ": " << result << endl;
	}
	inputFile.close();
	outFile.close();
	return 0;
}

