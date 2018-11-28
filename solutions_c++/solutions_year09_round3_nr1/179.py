#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <iomanip>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int match[36];
bool set[36];

int GetValue(char ch)
{
	if(ch >= '0' && ch <= '9')
	{
		return ch - '0';
	}
	return ch - 'a' + 10;
}

long long Calc(string num)
{
	memset(set, 0, sizeof(set));
	for(int i = 0; i < 36; ++i)
	{
		match[i] = -1;
	}

	int base = 0;
	for(int i = 0; i < num.length(); ++i)
	{
		if(!set[GetValue(num[i])])
		{
			set[GetValue(num[i])] = true;
			++base;
		}
	}

	if(base == 1)
	{
		++base;
	}

	long long result = 1;
	int curr = 0;
	match[GetValue(num[0])] = 1;

	for(int i = 1; i < num.length(); ++i)
	{
		result *= base;
		if(match[GetValue(num[i])] < 0)
		{
			match[GetValue(num[i])] = curr++;
			if(curr == 1)
			{
				++curr;
			}
		}
		result += match[GetValue(num[i])];
	}

	return result;
}

int main()
{
	int t;
	fin >> t;

	string input;
	for(int i = 0; i < t; ++i)
	{
		fin >>input;

		fout << "Case #" << i + 1 << ": " << Calc(input) << endl;
	}

	return 0;
}