#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

/*
bool isLightOn(int n, int k)
{
	long long lightState = 0;
	int firstOffLight = 0;

	for (int i = 0;i < k;++i)
	{
		long long xorTarget = 1;

		for (long long i = 1;i <= firstOffLight;++i)
		{
			xorTarget |= (1 << i);
		}

		lightState ^= xorTarget;
		firstOffLight = n - 1;

		for (int i = 0;i < n;++i)
		{
			if (((1 << i) & lightState) == 0)
			{
				firstOffLight = i;
				break;
			}
		}
	}

	//Check
	bool isLightOnFlag = true;

	for (int i = 0;i < n;++i)
	{
		if (lightState % 2 == 0)
		{
			isLightOnFlag = false;
			break;
		}

		lightState /= 2;
	}

	return isLightOnFlag;
}
*/

bool isLightOn(int n, int k)
{
	int temp = (int)pow(2.0, (double)n);

	k %= temp;

	return (k == (temp - 1));
}

int main()
{
	//Open files
	//ifstream fin("D:\\GoogleCodeJam\\sampleData.in");
	ifstream fin("D:\\GoogleCodeJam\\A-large.in");
	ofstream fout("D:\\GoogleCodeJam\\output.txt");

	if(!fin)
	{    
		cout << "File loading fails." << endl;   
	}

	int cases; 
	int n, k;

	fin >> cases;

	//Handle Input
	for (int caseNumber = 1;caseNumber <= cases;++caseNumber)
	{
		fin >> n >> k;

		//Output
		fout << "Case #" << caseNumber << ": ";

		if (isLightOn(n, k))
		{
			fout << "ON" << endl;
		}
		else
		{
			fout << "OFF" << endl;
		}
	}
	
	//Close files
	fin.close();   
	fout.close();

	return 0;
}