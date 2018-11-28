
#include "stdafx.h"
#using <mscorlib.dll>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <conio.h>
#include <iomanip>

using namespace std;

ifstream in("A-large.in.txt");
ofstream out("A-large.out.txt");

bool exist[16][32];

int _tmain()
{
	int L, D, N;
	in >> L >> D >> N;
	vector<string> words;
	for (int i = 0; i < D; ++i)
	{
		string word;
		in >> word;
		words.push_back(word);
	}
    for (int i = 0; i < N; ++i)
	{
		memset(exist, 0, sizeof(exist));
		string pattern;
		in >> pattern;
		int index = 0;
		int pos = 0;
		bool inkuo = false;
		while(index != L)
		{
			char ch = pattern[pos];
			if (ch == '(')
			{
				inkuo = true;
			}
			if (ch == ')')
			{
				inkuo = false;
				++index;
			}
			if (ch >= 'a' && ch <= 'z')
			{
				exist[index][ch - 'a'] = true;
				if (!inkuo)
				{
					++index;
				}
			}
			++pos;
		}
		int res = 0;
		for (int j = 0; j < (int) words.size(); ++j)
		{
			bool ok = true;
			for (int k = 0; k < L; ++k)
			{
				if (!exist[k][words[j][k] - 'a'])
				{
					ok = false;
					break;
				}
			}
			if (ok)
			{
				++res;
			}
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
    return 0;
}