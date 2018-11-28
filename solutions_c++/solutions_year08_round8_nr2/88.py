#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <numeric>
#include <cmath>
#include <utility>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int ones(int i) {int j =0; while (i) {i &= i-1; ++j;} return j;}


int count(const vector<pair<int,int> >& v)
{
	int r = -1;
	int n = v.size();
	int res = 1000;
	vector<int> f(n+1, 1000);
	for (int j = 0; j < n; ++j)
	{
		if (v[j].first <= 0) f[j] = 1;
		else
			for (int k = 0; k < j; ++k)
				if (v[k].second+1 >= v[j].first)
				{
					f[j] = min(f[j], f[k]+1);
				}
		if (v[j].second >= 9999) 
			res = min(res, f[j]);
	}
	return res;
}

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	int t;
	ifs >> t;
	for (int l =0; l < t; ++l)
	{
		vector<vector<int> > left, right;
		map<string, int> m;
		vector<vector<int> > v;
		int n;
		ifs >> n;
		string s;
		int lef, r;
		int cnt = 0;
		for (int i = 0; i < n; ++i)
		{
			ifs >> s >> lef >> r;
			--lef; --r;
			if (m.count(s) == 0)
			{
				m[s] = cnt;
				left.push_back(vector<int>());
				right.push_back(vector<int>());
				left[cnt].push_back(lef);
				right[cnt].push_back(r);
				++cnt;
			}
			else 
			{
				int c = m[s];
				left[c].push_back(lef);
				right[c].push_back(r);
			}
		}
		ofs << "Case #" << l+1 << ": ";
		int minn = n+1;
		for (int i = 0; i < cnt; ++i)
		{
			vector<pair<int,int> > tmp;
			for (int z = 0; z < left[i].size(); ++z)
			{
				tmp.push_back(make_pair(left[i][z], right[i][z]));
			}
			sort(tmp.begin(), tmp.end());
			int res = count(tmp);
			minn = min(minn, res);
		}
		for (int i = 0; i < cnt; ++i)
			for (int j = i+1; j < cnt; ++j)
			{
				vector<pair<int,int> > tmp;
				for (int z = 0; z < left[i].size(); ++z)
				{
					tmp.push_back(make_pair(left[i][z], right[i][z]));
				}
				for (int z = 0; z < left[j].size(); ++z)
				{
					tmp.push_back(make_pair(left[j][z], right[j][z]));
				}
				sort(tmp.begin(), tmp.end());
				int res = count(tmp);
				minn = min(minn, res);
			}
		for (int i = 0; i < cnt; ++i)
			for (int j = i+1; j < cnt; ++j)
				for (int k = j+1; k < cnt; ++k)
				{
					vector<pair<int,int> > tmp;
					for (int z = 0; z < left[i].size(); ++z)
					{
						tmp.push_back(make_pair(left[i][z], right[i][z]));
					}
					for (int z = 0; z < left[j].size(); ++z)
					{
						tmp.push_back(make_pair(left[j][z], right[j][z]));
					}
					for (int z = 0; z < left[k].size(); ++z)
					{
						tmp.push_back(make_pair(left[k][z], right[k][z]));
					}
					sort(tmp.begin(), tmp.end());
					int res = count(tmp);
					minn = min(minn, res);
				}
		if (minn > n)
			ofs << "IMPOSSIBLE\n";
		else
			ofs << minn <<  endl;
	}
	return 0;
}