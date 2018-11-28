#include "stdafx.h"
#include <fstream>
#include <algorithm>

#define TEST_IN "bigin.txt"
#define TEST_OUT "bigout.txt"

int a[800], b[800], ass[800];


int main()
{
	std::ifstream fin(TEST_IN);
	std::ofstream fout(TEST_OUT);

	int t, i, n, j, k;
	fin>>t;
	for (i = 1; i <= t; ++i)
	{

		fin>>n;
		for (j = 0; j < n; ++j)
			fin>>a[j];
		for (j = 0; j < n; ++j) 
		{
			fin>>b[j];
			ass[j] = j;
		}

		bool changes = true;
		while (changes)
		{
			changes = false;
			for (j = 0; j < n; ++j)
			{
				for (k = j + 1; k < n; ++k)
				{
					long long current = (long long)a[j] * b[ass[j]] + (long long)a[k] * b[ass[k]];
					long long newP = (long long)a[j] * b[ass[k]] + (long long)a[k] * b[ass[j]];
					if (current > newP)
					{
						std::swap(ass[j], ass[k]);
						changes = true;
					}
				}
			}
		}

		long long result = 0;
		for (j = 0; j < n; ++j)
		{
			result += (long long)a[j] * b[ass[j]];
		}
		fout<<"Case #"<<i<<": "<<result<<std::endl;
	}
	fin.close();
	fout.close();
	return 0;
}
			


					
		