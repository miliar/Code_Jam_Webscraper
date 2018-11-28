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

vector<int> v;
int F[105][1024];
int m, n;

int Go(int last, int d)
{
	int& res = F[last][d];
	if (res != -1) return res;
	if (d == v.size()) return 0;
	res = 1000000;
	if (last == v[d])
	{
		for (int i = 0; i < n; ++i)
		{
			if (i != last)
			{
				res = min(res, Go(i, d+1)+1);
			}
		}
	}
	else 
	{
		res = Go(last, d+1);
	}
	return res;
}

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	int t;
	string s;
	stringstream str;
	getline(ifs, s);
	sscanf(s.c_str(), "%d", &t);
	for (int l = 0; l < t; ++l)
	{
		memset(F, -1, sizeof(F));
		vector<string> names;
		map<string, int> mp;
		getline(ifs, s);
		sscanf(s.c_str(), "%d", &n);
		names.assign(n, "");
		for (int i= 0; i < n; ++i)
		{
			getline(ifs, names[i]);
			mp[names[i]] = i;
		}
		getline(ifs, s);
		sscanf(s.c_str(), "%d", &m);
		v.assign(m, 0);
		for (int i = 0; i < m; ++i)
		{
			getline(ifs, s);
			v[i] = mp[s];
		}
		int res = m;
		for (int i = 0; i < n; ++i)
		{
			res = min(res, Go(i, 0));
		}
		ofs << "Case #" << l+1 << ": " << res << endl;
	}

  	return 0;
}
