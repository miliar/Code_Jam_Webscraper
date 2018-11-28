#include <vector>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
#include <math.h>
using namespace std;

#define SIZE 10000
#define MEMSET(X) memset(X, 0, SIZE)
#define GETLINE(X) \
	MEMSET(buffer); \
	X.getline(buffer, SIZE, '\n');

typedef __int64 I64;

int main (int argc, char **argv)
{
	ifstream ifstr("Input.txt");
	ofstream ofstr("Output.txt");
	char buffer[SIZE];
	MEMSET(buffer);
	ifstr.getline(buffer, SIZE, '\n');
	int numOfCases = atoi(buffer);

	char buffer1[200];
	memset(buffer1, 0, 200);
	for (int i = 0; i < numOfCases; i++)
	{
		map <char, int> iMap;
		vector<int> iVec;
		GETLINE(ifstr);
		string temp(buffer);
		int count = 0;
		for (int i =0; i < temp.length(); i++)
		{
			char c = temp[i];
			if (i == 0)
			{
				iMap[c] = 1;
				iVec.push_back(1);
				continue;
			}
			if (iMap.find(c) != iMap.end())
			{
				continue;
			}
			else
			{
				iMap[c] = count;
				iVec.push_back(count);
				count++;
				if (count == 1)
				{
					count++;
				}
			}
		}
		sort(iVec.begin(), iVec.end());
		double base = iVec[iVec.size()-1];
		base++;
		char buf1[200];
		memset(buf1, 0, 200);

		double count1 = 0;
		map <int, char> cMap;
		cMap[0] = '0';
		cMap[1] = '1';
		cMap[2] = '2';
		cMap[3] = '3';
		cMap[4] = '4';
		cMap[5] = '5';
		cMap[6] = '6';
		cMap[7] = '7';
		cMap[8] = '8';
		cMap[9] = '9';
		//string res;
		__int64 res = 0;
		int base1 = base;
		int q = 0;
		for (int j = temp.size()-1; j >= 0; j--)
		{
			int rem;
			char c = temp[j];
			I64 t = pow(base, count1);
			I64 num = iMap[c] * t;
			//rem = num%base1;
			//rem += q;
			res += num;
			//res.push_back(cMap[rem]);
			count1++;
		}
		ofstr << "Case #" << i+1 << ": " << res << endl;
		cout << res << endl;
	}
	return 0;
}





