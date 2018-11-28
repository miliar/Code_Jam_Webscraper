// 2.cpp: определяет точку входа для консольного приложения.
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
	inFile.open("B-large.in");
	outFile.open("B-large.out");
	int caseNumMax;
	inFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		vector<string> combine;
		vector<string> opposite;
		int T;
		inFile >> T;
		char c;
		for (int i = 0; i < T; ++i)
		{
			string temp;
			inFile >> temp;
			combine.push_back(temp);
		}
		inFile >> T;
		for (int i = 0; i < T; ++i)
		{
			string temp;
			inFile >> temp;
			opposite.push_back(temp);
		}
		inFile >> T;
		string result;
		char prev;
		for (int i = 0; i < T; ++i)
		{
			bool flag = false;
			inFile >> c;
			if (result.empty())
			{
				result += c;
				continue;
			}
			prev = result.at(result.size()-1);
			for (vector<string>::iterator it = combine.begin(); it < combine.end(); ++it)
			{
				if ( ((c == (*it).at(0)) && (prev == (*it).at(1))) || ((c == (*it).at(1)) && (prev == (*it).at(0))) )
				{
					result.pop_back();
					result += (*it).at(2);
					flag = true;
					break;
				}
			}
			if (flag)
				continue;
			for (vector<string>::iterator it = opposite.begin(); it < opposite.end(); ++it)
			{
				if (c == (*it).at(0))
				{
					for (int pos = 0; pos < result.size(); ++pos)
					{
						if ( result.at(pos) == (*it).at(1) )
						{
							result.clear();
							flag = true;
							break;
						}
					}
				}
				else if (c == (*it).at(1))
				{
					for (int pos = 0; pos < result.size(); ++pos)
					{
						if ( result.at(pos) == (*it).at(0) )
						{
							result.clear();
							flag = true;
							break;
						}
					}
				}
				if (flag)
					break;
			}
			if (flag) 
				continue;
			result += c;
		}
		outFile << "Case #" << caseNum + 1 << ": [";
		if (!result.empty())
		{
			outFile << result.at(0);
		}
		for (int i = 1; i < result.size(); ++i)
		{
			outFile << ", " << result.at(i);
		}
		outFile << "]" << endl;


	}
	inFile.close();
	outFile.close();
	return 0;
}