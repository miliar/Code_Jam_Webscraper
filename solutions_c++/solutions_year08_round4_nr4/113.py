#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs("d.in");
	ofstream ofs("d.out");
	
	int t;
	ifs >> t;
	for (int l= 0; l < t; ++l)
	{
		ofs << "Case #" << l+1 << ": ";
		int n;
		int best = 1000000;
		ifs >> n;
		string text;
		ifs >> text;
		vector<int> v(n);
		for (int i = 0; i < n; ++i)
		{
			v[i] = i;
		}
		do {
			string s = text;
			for (int i = 0; i < s.size(); i += n)
			{
				for (int j = 0; j < n; ++j)
				{
					s[i+j] = text[i+v[j]];
				}
			}
			s += ' ';
			int o = 0;
			for (int i = 1; i < s.size(); ++i)
				if (s[i] != s[i-1]) ++o;
			best = min(best, o);

		} while (next_permutation(v.begin(), v.end()));
		ofs << best << endl;
	}
  	return 0;
}

