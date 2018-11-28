// C++ source code file for Problem A. Bot Trust
// ANIL SOOD
// anilsood.ucla@gmail.com

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

const char orange = 'O';
const char blue = 'B';

int curPos, OcurStrPos, OcurButtonPos, BcurStrPos, BcurButtonPos;

void refresh()
{
	OcurStrPos = 0;
	OcurButtonPos = 1;
	BcurStrPos = 0;
	BcurButtonPos = 1;

	curPos = 0;
}

int OseekNextTaskTime(const string &str, int& length)
{
	int timer = 0;
	int temp = 0;
	char ch;

	if(OcurStrPos >= length)
		return timer;

	while(str[OcurStrPos] != orange)
	{
		OcurStrPos++;
		if(OcurStrPos == length)
			return timer;
	}

	OcurStrPos++;		
	ch = str[OcurStrPos];
	while(isdigit(ch)) 
	{
		temp = (temp * 10) + ch - 48;

		OcurStrPos++;
		if(OcurStrPos == length)
			break;

		ch = str[OcurStrPos];
	}

	if(temp == OcurButtonPos)
	{
		timer = 1;
	}
	else
	{
		timer = 1 + abs(OcurButtonPos - temp);
		OcurButtonPos = temp;
	}

	return timer;
}

int BseekNextTaskTime(const string &str, int& length)
{
	int timer = 0;
	int temp = 0;
	char ch;

	if(BcurStrPos >= length)
		return timer;

	while(str[BcurStrPos] != blue)
	{
		BcurStrPos++;
		if(BcurStrPos == length)
			return timer;
	}

	BcurStrPos++;		
	ch = str[BcurStrPos];
	while(isdigit(ch)) 
	{
		temp = (temp * 10) + ch - 48;

		BcurStrPos++;
		if(BcurStrPos == length)
			break;

		ch = str[BcurStrPos];
	}

	if(temp == BcurButtonPos)
	{
		timer = 1;
	}
	else
	{
		timer = 1 + abs(BcurButtonPos - temp);
		BcurButtonPos = temp;
	}

	return timer;
}

char GetNextTask(const string &str, int& length)
{
	char next;

	if(curPos == length)
		return NULL;
	else
		next = str[curPos];

	curPos++;
	while(str[curPos] != orange && str[curPos] != blue)
	{
		curPos++;
		if(curPos == length)
			break;
	}

	return next;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int count = 0;
	int length = 0;
	int answer = 0;
	string inputFile = "C:\\Users\\Anil\\Desktop\\input.in";
	string outputFile = "C:\\Users\\Anil\\Desktop\\output.out";
	string line;
	string filteredLine;
	ifstream myfile (inputFile);
	ofstream myoutfile (outputFile);

	if (myfile.is_open() && myoutfile.is_open())
	{
		int caseIndex = 0;

		// Skip the count
		if(myfile.good())
			getline (myfile,line);

		while ( myfile.good() )
		{
			answer = 0;
			caseIndex++;			
			getline (myfile,line);
			refresh();

			int BcurTask = 0;
			int OcurTask = 0;

			if(line.length() == 0)
				return -1;

			// Filter the string
			int i = 0;
			char ch = line[0];
			while (isdigit(ch))
			{
				i++;
				ch = line[i];
			}
			filteredLine = line.substr(i + 1);
			filteredLine.erase(remove_if(filteredLine.begin(), filteredLine.end(), isspace), filteredLine.end());

			length = filteredLine.length();
			int BcurTaskTime = BseekNextTaskTime(filteredLine, length);
			int OcurTaskTime = OseekNextTaskTime(filteredLine, length);

			while(true)
			{
				char ch = GetNextTask(filteredLine, length);
				if(ch == orange)
				{
					answer += OcurTaskTime;
					BcurTaskTime = max(1, BcurTaskTime - OcurTaskTime);
					OcurTaskTime = OseekNextTaskTime(filteredLine, length);
				}
				else if(ch == blue)
				{
					answer += BcurTaskTime;
					OcurTaskTime = max(1, OcurTaskTime - BcurTaskTime);
					BcurTaskTime = BseekNextTaskTime(filteredLine, length);
				}
				else
				{
					break;
				}
			}

			myoutfile << "Case #" << caseIndex << ": " << answer << "\n";
		}

		myfile.close();
		myoutfile.close();
	}		 		
}