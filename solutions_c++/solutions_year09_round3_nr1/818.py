#include "stdafx.h"
#include <stdio.h>
#include <vector>
using std::vector;

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <string>
using std::string;

#include <set>
using std::set;

#include <map>
using std::map;

#include <algorithm>
#include <numeric>
#include <fstream>
#include <cmath>
using namespace std;

typedef __int64				Int64;
typedef unsigned __int64	uInt64;




int _tmain(int argc, _TCHAR* argv[])
{
	fstream fIn("d:\\Projects\\code jam\\2009_1C\\A-large.in");
	fstream fOut;
	fOut.open("d:\\Projects\\code jam\\2009_1C\\A-large.res", ios_base::out);

	int testNumber = 0;
	fIn >> testNumber;

	for (int i = 0; i < testNumber; ++i)
	{
		string s;
		fIn >> s;
		std::set<char> st(s.begin(), s.end());
		unsigned int order = st.size();
		if (order == 1)
			order++;

		map<char, unsigned int> mp;
		unsigned int val = 1; 
		unsigned int count = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			if (mp.find(s[i]) == mp.end())
			{
				
				if (count == 1)
				{
					mp[s[i]] = 0;
				}
				else
					mp[s[i]] = val++;

				++count;
			}
		}

		char prev = '!';
		unsigned int n = 0;
		uInt64 res = 0;

			for (size_t j = 0; j < s.size() - 1; ++j)
			{
				unsigned int p = mp[s[j]];
				
				res += p;
				res *= order;
			}

			res += mp[s[s.size() -1]];
		

		//char buff [5];
		//sprintf(buff, "%04d", res);
			fOut << "Case #" << i+1 <<": "<< res << "\n";
	}

	return 0;
}
