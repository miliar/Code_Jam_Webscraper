#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const string welcome("welcome to code jam");
int dp[20];

string GetFormatedNumber(int num)
{
	string result("0000");
	int p = 3;
	while(num > 0)
	{
		result[p--] = (char)(num % 10 + '0');
		num /= 10;
	}
	return result;
}

int main()
{
	int n;
	fin >> n;

	string str;
	getline(fin, str);
	for(int i = 0; i < n; ++i)
	{
		getline(fin, str);
		memset(dp, 0, sizeof(dp));
		for(int j = 0; j < str.size(); ++j)
		{
			for(int k = 0; k < welcome.size(); ++k)
			{
				if(welcome[k] == str[j])
				{
					if(k == 0)
					{
						++dp[k];
					}
					else
					{
						dp[k] += dp[k - 1];
					}

					if(dp[k] >= 10000)
					{
						dp[k] -= 10000;
					}
				}
			}
		}

		fout << "Case #" << i + 1 << ": " << GetFormatedNumber(dp[welcome.size() - 1]) << endl;
	}

	return 0;
}