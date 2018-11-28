// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main(int argc, char* argv[])
{
	std::fstream inputFileStream("B-small.in",ios::in);
	string outFileName("B-small");
	outFileName += ".out";
	std::fstream outputFileStream(outFileName.c_str(), ios::out);
	int caseCount;
	cout.precision(6);
	cout.setf(std::ios_base::fixed);
	inputFileStream >> caseCount;
	cout << caseCount << endl;
	for(int caseNo =1; caseNo <= caseCount; caseNo++)
	{
		int P, K, L;
		inputFileStream >> P >> K >> L;
		cout << P << " " << K  << " " << L << endl;
		vector<int> let;
		for(int i=0; i < L; i++)
		{
			int no;
			inputFileStream >> no;
			let.push_back(no);
			cout << no <<" ";
		}
		sort(let.begin(), let.end());
		//for(int i = let.size(); i >0; i--)
		//{
		//	int pre = 1;
		int letCount = let.size()-1;
		int pressCount = 0;
		for(int i = 1; i <= P; i++)
		{
			for(int j = 1; j <= K; j++)
			{
				if(letCount >= 0)
				{
					pressCount += let[letCount--]*i;
				}
			}
		}

	outputFileStream << "Case #" << caseNo << ": " << pressCount << endl;
		

			
		cout << endl;

	}
	cout << "GCJ-2" << endl;
}