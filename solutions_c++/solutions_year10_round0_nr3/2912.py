//============================================================================
// Name        : Theme.cpp
// Author      : Jaqoup
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;
int arr[10000];

int main() {
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	int loop;
	fin>>loop;
	for (int caseNo=0;caseNo<loop;caseNo++)
	{
		int startPos = 0, curPos = 0, curCounter = 0,Output = 0;
		int R, k, N;
		fin>>R>>k>>N;
		for (int i=0; i < N;i++)
		{
			fin>>arr[i];
		}
		for (int it = 0; it < R; it++)
		{
			while (curCounter + arr[curPos] <= k)
			{
				curCounter += arr[curPos];
				curPos++;
				curPos%=N;
				if(curPos == startPos)
					break;
			}
			Output += curCounter;
			curCounter = 0;
			startPos = curPos;
		}
		fout<<"Case #"<<caseNo+1<<": "<<Output<<endl;
	}
	return 0;
}
