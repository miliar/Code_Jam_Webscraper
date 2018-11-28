#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>
#include <map>
#include <string>

using namespace std;

int Cycle(int old, int base)
{
	int remain = old%10;
	int res = old/10;
	return remain*base+res;
}

int MinCyc(int old, int base)
{
	int min = old, tmp = old;
	int count = 0;
	for (int b=1; b<=base; b*=10)
	{
		count++;
	}
	for (int i=0; i<count; i++)
	{
		tmp = Cycle(tmp, base);
		min > tmp ? min = tmp : NULL;
	}
	return min;
}

int stepMilti(int size)
{
	int res=1;
	for (int i=1; i<=size; i++)
	{
		res *= i;
	}
	return res;
}

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("C-Small.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("C-Small.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	string strA, strB;
	int minA, maxB;

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//输入
		inFile >> strA /*input data receiver*/;
		minA = atoi(strA.c_str());
		inFile >> strB /*input data receiver*/;
		maxB = atoi(strB.c_str());
		int base = 1;
		for (int j=0; j<strA.length()-1; j++)
		{
			base *= 10;
		}
		//操作区
		int pairCount = 0;
		map<int, int> pairSet;
		map<int, int>::iterator pairIter;
		if (maxB > 10)
		{
			for (int j=minA; j<=maxB; j++)
			{
				int min = MinCyc(j, base);
				if (pairSet.count(min))
				{
					pairSet[min]++;
				}
				else
				{
					pairSet[min] = 1;
				}
			}
			for (pairIter=pairSet.begin(); pairIter!=pairSet.end(); pairIter++)
			{
				int t = (*pairIter).second;
				if (t>1)
				{
					pairCount += stepMilti(t)/2;
				}
			}
		}

		//输出
		outFile << "Case #" << i+1 << ": " << pairCount << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}