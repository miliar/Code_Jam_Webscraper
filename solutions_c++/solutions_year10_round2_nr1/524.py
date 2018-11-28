#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void OpenSmall(string leter)
{
	string inName = leter + "-small.in";
	string outName = leter + "-small.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

void OpenLarge(string leter)
{
	string inName = leter + "-large.in";
	string outName = leter + "-large.out";
	freopen(inName.c_str(), "r", stdin);
	freopen(outName.c_str(), "w", stdout);
}

int pow2(int n)
{
	int ans = 1;
	for(int i = 0; i < n; ++i)
		ans <<= 1;
	return ans;
}

int main()
{
	OpenLarge("A");
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n, m;
		cin >> n >> m;
		set<string> pathes;
		for(int i = 0; i < n; ++i)
		{
			string path;
			cin >> path;
			for(int j = 1; j <= path.length(); ++j)
			{
				if(j == path.length() || path[j] == '/')
				{
					pathes.insert(path.substr(0, j));
				}
			}
		}
		int cnt = 0;
		for(int i = 0; i < m; ++i)
		{
			string path;
			cin >> path;
			for(int j = 1; j <= path.length(); ++j)
			{
				if(j == path.length() || path[j] == '/')
				{
					if(pathes.find(path.substr(0, j)) == pathes.end())
					{
						++cnt;
						pathes.insert(path.substr(0, j));
					}
				}
			}
		}
		cout<<"Case #"<<Case+1<<": ";
		cout << cnt << endl;
	}

	return 0;
}