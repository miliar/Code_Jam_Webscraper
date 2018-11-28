#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");		
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int n, m;
		ifs >> n >> m;
		vector<string> s(n);
		vector<string> t(m);
		string path;
		for (int i = 0; i < n; ++i)
		{
			ifs >> path;
			s[i] = path;
		}
		for (int i = 0; i < m; ++i)
		{
			ifs >> path;
			t[i] = path;
		}
		sort(t.begin(), t.end());
		int res = 0;
		for (int i = 0; i < m; ++i)
		{
			int best = count(t[i].begin(), t[i].end(), '/');
			int sz = t[i].size();
			for (int j = 0; j < s.size(); ++j)
			{
				if (s[j].substr(0, sz) == t[i])
				{
					if (s[j] == t[i] || s[j].size() > sz && s[j][sz] == '/')
					{
						best = 0;
						break;
					}
				}
				int z = min(s[j].size(), t[i].size());
				int k = 0;
				for (; k < z; ++k)
				{
					if (s[j][k] != t[i][k]) break;
				}
				string st = t[i].substr(k);
				int r = count(st.begin(), st.end(), '/') + 1;
				if (st.size() > 0 && st[0] == '/') --r;
				best = min(best, r);
			}
			res += best;
			s.push_back(t[i]);
		}
		ofs << "Case #" << test+1 << ": " << res << endl;
	}
  	return 0;
}
