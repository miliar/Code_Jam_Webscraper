#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h> 

using namespace std;

int getCount(int L, vector<string> dict, string pat)
{
	replace(pat.begin(), pat.end(), '(', ' ');
	replace(pat.begin(), pat.end(), ')', ' ');
	istringstream istr(pat);
	for (int j = 0; j < L; ++j)
	{
		string c;
		istr >> c;
		vector<string> newdict;
		for (int k = 0; k < (int)dict.size(); ++k)
			if (c.find_first_of(dict[k][j]) != string::npos)
				newdict.push_back(dict[k]);
		dict = newdict;
	}
	return dict.size();
}

int main()
{
	ifstream ifstr("A-large.in");
	int L, D, N;
	ifstr >> L >> D >> N;

	vector<string> dict;
	for (int i = 0; i < D; ++i)
	{
		string temp;
		ifstr >> temp;
		dict.push_back(temp);
	}

	ofstream ofstr("A-large.out");
	for (int i = 0; i < N; ++i)
	{
		string temp;
		ifstr >> temp;
		int j = 0;
		string pat;
		while (j < (int)temp.size())
		{
			if (temp[j] != '(')
			{
				pat += temp[j];
				pat += ' ';
				++j;
			}
			else
				while (j < (int)temp.size() && temp[j] != ')')
				{
					pat += temp[j];
					++j;
				}
		}

		ofstr << "Case #" << i + 1 << ": " << getCount(L, dict, pat) << "\n";
	}

	return 0;
}
