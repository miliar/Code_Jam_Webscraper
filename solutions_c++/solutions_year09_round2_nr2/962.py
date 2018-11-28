#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
#include <functional> 

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

string Calc(string num)
{
	string result(num);
	if(num.length() == 1)
	{
		result.push_back('0');
	}
	else
	{
		char digits[10];
		memset(digits, 0, sizeof(digits));
		for(int i = 0; i < num.length(); ++i)
		{
			++digits[num[i] - '0'];
		}

		int nip = -1;
		for(int i = result.length() - 1; i > 0; --i)
		{
			if(result[i] > result[i - 1])
			{
				nip = i - 1;
				break;
			}
		}

		if(nip >= 0)
		{
			result = "";
			for(int i = 0; i < nip; ++i)
			{
				--digits[num[i] - '0'];
				result.push_back(num[i]);
			}

			int sp = nip + 1;
			for(int i = sp + 1; i < num.length(); ++i)
			{
				if(num[i] > num[nip] && num[i] < num[sp])
				{
					sp = i;
				}
			}

			result.push_back(num[sp]);
			--digits[num[sp] - '0'];

			for(int i = 0; i < 10; ++i)
			{
				for(int j = 0; j < digits[i]; ++j)
				{
					result.push_back(i + '0');
				}
			}
		}
		else
		{
			result = "";
			for(int i = 1; i < 10; ++i)
			{
				for(int j = 0; j < digits[i]; ++j)
				{
					result.push_back(i + '0');
				}
			}
			result.insert(1, digits[0] + 1, '0');
		}
	}
	
	return result;
}

int main()
{
	int t;
	fin >> t;

	string num;
	for(int i = 0; i < t; ++i)
	{
		fin >> num;
		fout << "Case #" << i + 1 << ": " << Calc(num) << endl;
	}

	return 0;
}