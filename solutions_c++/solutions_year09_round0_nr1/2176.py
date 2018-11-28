// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream f("D:\\A.in");
	int L, D, N;

	f >> L >> D >>N;
	vector<string> dict(D);
	for (int i = 0; i< D;++i)
	{
		f >> dict[i];
	}
	vector<string> tests(N);

	for (int i = 0; i< N;++i)
	{
		f >> tests[i];
	}
	ofstream fo("D:\\A.out");
	for (int test = 0; test< N;++test)
	{
		vector<vector<bool> > t(L, vector<bool>(26, false));
		int token = 0;
		bool bInToken = false;
		for (int ch =0; ch< tests[test].size(); ++ch)
		{
			char c = tests[test][ch];
			if (c == '(')
			{
				bInToken = true;
				continue;
			}
			if (c == ')')
			{
				bInToken = false;
				token++;
				continue;
			}
			c -= 'a';
			t[token][c] = true;
			if (!bInToken)
				token++;
		}

		int count = 0;
		for (int word = 0; word < D; ++word)
		{
			bool bPresent = true;
			string & w = dict[word];
			for (int token = 0; token < w.size(); ++token)
				if (!t[token][w[token]-'a'])
				{
					bPresent = false;
				}

			if (bPresent)
				count ++;
		}



		fo << "Case #" << test +1 << ": " << count <<endl; 

	}


	return 0;
}

