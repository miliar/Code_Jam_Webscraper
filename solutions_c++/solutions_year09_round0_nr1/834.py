#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int L, D, N;
vector<string> dict;
string pattern;

char check[5001][20];

int solve(void)
{
	int pos = 0;

	for (int i = 0 ; i < D ; ++i)
	{
		for (int j = 0 ; j < L ; ++j)
		{
			check[i][j] = 0;
		}
	}

	bool range = false;
	for (int i = 0 ; i < pattern.length() ; ++i)
	{
		if (pattern[i] == '(')
		{
			range = true;
			continue;
		}
		if (pattern[i] == ')')
		{
			range = false;
			++pos;
			continue;
		}

		for (int j = 0 ; j < D ; ++j)
		{
			if ((pos == 0 || check[j][pos - 1]) && pattern[i] == dict[j][pos])
			{
				check[j][pos] = 1;
			}
		}

		if (!range) ++pos;
	}

	int result = 0;

	for (int i = 0 ; i < D ; ++i)
	{
		if (check[i][L - 1]) ++result;
	}

	return result;
}

int main(void)
{
	cin >> L >> D >> N;

	for (int i = 0 ; i < D ; ++i)
	{
		string word;

		cin >> word;
		dict.push_back(word);
	}

	for (int t = 1 ; t <= N ; ++t)
	{
		cin >> pattern;

		cout << "Case #" << t << ": " << solve() << endl;
	}
}
