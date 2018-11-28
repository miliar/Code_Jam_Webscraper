#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <stack>
#include <queue>
#include <string>
#include <memory.h>
#include <iostream>
#include <sstream>

using namespace std;

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef long long LL;
//typedef double D;

int c, d, n, t;
vint V;
vvint G, C;
string s;

bool change(string & s)
{
	if (s.size() > 1)
	{
		if (G[s[s.size() - 1] - 'A'][s[s.size() - 2] - 'A'] > 0)
		{
			string st = s.substr(0, s.size() - 2) + 
			(char)(G[s[s.size() - 1] - 'A'][s[s.size() - 2] - 'A']);
			s = st;
			return 1;
		}
	}
	return 0;
}

bool opposed(const string & s)
{
	for(int i = 0; i < s.size(); ++i)
		for(int j = i + 1; j < s.size(); ++j)
			if (C[s[i] - 'A'][s[j] - 'A'] < 0)
				return 1;
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		cin >> c;
		G.assign(26, vint(26, 0));
		C.assign(26, vint(26, 0));
		for(int j = 0; j < c; ++j)
		{
			cin >> s;
			G[s[0] - 'A'][s[1] - 'A'] = s[2];
			G[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		cin >> d;
		for(int j = 0; j < d; ++j)
		{
			cin >> s;
			C[s[0] - 'A'][s[1] - 'A'] = -1;
			C[s[1] - 'A'][s[0] - 'A'] = -1;
		}
		cin >> n;
		cin >> s;
		string t;
		for(int j = 0; j < n; ++j)
		{
			t += s[j];
			while (change(t));
			if (opposed(t))
				t.clear();
		}
		cout << "Case #" << i + 1 << ": [";
		for(int j = 0; j < t.size(); ++j)
		{
			cout << t[j];
			if (j + 1 < t.size())
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}