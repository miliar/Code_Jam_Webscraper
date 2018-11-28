
#include "stdafx.h"
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
#using <mscorlib.dll>

using namespace std;

ifstream in("D-small-attempt0.in.txt");
ofstream out("D-small-attempt0.out.txt");

int _tmain()
{
	int n;
	in >> n;
	for (int i = 1; i <= n; ++i)
	{
		int k;
		string s;
		in >> k >> s;
		vector<int> per;
		for (int j = 0; j < k; ++j)
		{
			per.push_back(j);
		}
		int best = 999999;
		do
		{
			string after;
			for (int j = 0; j * k < s.size(); ++j)
			{
                for (int jj = 0; jj < k; ++jj)
				{
					after += s[j * k + per[jj]];
				}
			}
			int temp = 1;
			for (int j = 1; j < after.size(); ++j)
			{
				if (after[j] != after[j - 1])
				{
					++temp;
				}
			}
			best = min(temp, best);
		}while(next_permutation(per.begin(), per.end()));
		out << "Case #" << i << ": " << best << endl;
	}
	return 0;
}