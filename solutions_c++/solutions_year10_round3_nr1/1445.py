//2010 Google Code Jam - Round 1B - B. Picking Up Chicks
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class Rope
{
public :
		int rightHeight;
		int leftHeight;

		Rope(int rightHeight, int leftHeight)
		{
			this->leftHeight = leftHeight;
			this->rightHeight = rightHeight;
		}
};

int main()
{
	//Open files
	//ifstream fin("I:\\GoogleCodeJam\\sampleData.in");
	//ifstream fin("I:\\GoogleCodeJam\\B-small-practice.in");
	ifstream fin("I:\\GoogleCodeJam\\A-small-attempt0.in");
	//ifstream fin("I:\\GoogleCodeJam\\A-large.in");
	ofstream fout("I:\\GoogleCodeJam\\output.txt");

	if(!fin)
	{    
		cout << "File loading fails." << endl;   
	}

	int cases; 

	fin >> cases;

	//Handle Input
	for (int caseNumber = 1;caseNumber <= cases;++caseNumber)
	{
		int ropeCount, rightHeight, leftHeight;

		fin >> ropeCount;

		vector<Rope> ropes;

		for (int i = 0;i < ropeCount;i++)
		{
			fin >> rightHeight >> leftHeight;

			Rope temp(rightHeight, leftHeight);

			ropes.push_back(temp);
		}

		//Sort
		for (int i = 0;i < ropeCount - 1;i++)
		{
			for (int j = i;j < ropeCount - 1;j++)
			{
				if (ropes[j].leftHeight > ropes[j + 1].leftHeight)
				{
					Rope temp = ropes[j];
					ropes[j] = ropes[j + 1];
					ropes[j + 1] = temp;
				}
			}
		}

		int intersection = 0;

		//Compare
		for (int i = 0;i < ropeCount;i++)
		{
			for (int j = i + 1;j < ropeCount;j++)
			{
				if (ropes[i].rightHeight > ropes[j].rightHeight)
				{
					intersection++;
				}
			}
		}

		//Output
		fout << "Case #" << caseNumber << ": " << intersection << endl;	
	}
	
	//Close files
	fin.close();   
	fout.close();

	return 0;
}