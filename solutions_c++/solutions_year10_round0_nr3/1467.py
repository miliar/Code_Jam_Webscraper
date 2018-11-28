//2010 Google Code Jam - Qualification Round - A.Theme Park
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	//Open files
	//ifstream fin("D:\\GoogleCodeJam\\sampleData.in");
	//ifstream fin("D:\\GoogleCodeJam\\C-small-attempt1.in");
	ifstream fin("D:\\GoogleCodeJam\\C-large.in");
	ofstream fout("D:\\GoogleCodeJam\\output.txt");

	if(!fin)
	{    
		cout << "File loading fails." << endl;   
	}

	int cases; 
	int round, capacity, groups;
	int group[1000];
	int nextGroup[1000];
	int moneyEarned[1000];

	fin >> cases;

	//Handle Input
	for (int caseNumber = 1;caseNumber <= cases;++caseNumber)
	{
		fin >> round >> capacity >> groups;

		for (int i = 0;i < groups;++i)
		{
			fin >> group[i];
		}

		//Calculate next group and money earned		
		for (int gourpIndex = 0;gourpIndex < groups;++gourpIndex)
		{
			int totalPeople = 0;
			int groupTailIndex = gourpIndex;
			int startTailIndex = groupTailIndex;

			while (totalPeople + group[groupTailIndex] <= capacity)
			{
				totalPeople += group[groupTailIndex];
				groupTailIndex = (groupTailIndex + 1 >= groups) ? 0 : groupTailIndex + 1;

				if (startTailIndex == groupTailIndex)
				{
					//Means capacity of the Roller coasters is enough for all groups
					break;
				}
			}

			nextGroup[gourpIndex] = groupTailIndex;
			moneyEarned[gourpIndex] = totalPeople;
		}

		//Ride!!
		int index = 0;
		long long totalEarnedMoney = 0;

		while (round--)
		{
			totalEarnedMoney += moneyEarned[index];
			index = nextGroup[index];
		}

		//Output
		fout << "Case #" << caseNumber << ": " << totalEarnedMoney << endl;
	}
	
	//Close files
	fin.close();   
	fout.close();

	return 0;
}