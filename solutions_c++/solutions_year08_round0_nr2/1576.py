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

int strtot(const string& s)
{
	int h, m;
	sscanf(s.c_str(), "%d:%d", &h, &m);
	return h*60+m;
}

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	int t;
	ifs >> t;
	for (int l= 0; l < t; ++l)
	{
		int na, nb, t;
		ifs >> t >> na >> nb;
		vector<vector<int> > v;
		for (int i = 0; i < na; ++i)
		{
			vector<int> tmp(3);
			string s, e;
			ifs >> s >> e;
			tmp[0] = strtot(s);
			tmp[1] = strtot(e);
			tmp[2] = 0;
			v.push_back(tmp);
		}

		for (int i = 0; i < nb; ++i)
		{
			vector<int> tmp(3);
			string s, e;
			ifs >> s >> e;
			tmp[0] = strtot(s);
			tmp[1] = strtot(e);
			tmp[2] = 1;
			v.push_back(tmp);
		}
		sort(v.begin(), v.end());
		priority_queue<int, vector<int>, greater<int> > q[2];
		int res[2] = {0};
		for (int i = 0; i < na+nb; ++i)
		{
			int d = v[i][2];
			if (q[d].empty() || q[d].top() > v[i][0])
			{
				res[d]++;
			}
			else 
			{
				q[d].pop();
			}
			q[1-d].push(v[i][1]+t);
		}
		ofs << 	"Case #" << l+1 << ": " << res[0] << ' ' << res[1] << endl;
	}
  	return 0;
}
