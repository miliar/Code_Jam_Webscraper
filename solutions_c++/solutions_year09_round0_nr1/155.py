#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

int L, d, n;
string s[5000];

vector<string> produce(string p)
{
	int i, n = (int)p.size();
	vector<string> vs;
	for(i = 0; i < n; ++i)
	{
		string t;
		if (p[i] == '(')
		{
			++i;
			while(p[i] != ')')
			{
				t += p[i];
				++i;
			}
		}
		else
		{
			t = p[i];
		}
		vs.push_back(t);
	}
	return vs;
}

vector<string> g;

bool compare(int ind)
{
	int i;
	for(i = 0; i < L; ++i)
	{
		if (find(g[i].begin(), g[i].end(), s[ind][i]) == g[i].end())
		{
			return false;
		}
	}
	return true;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> L >> d >> n;
	string t;
	int i;
	for(i = 0; i < d; ++i)
	{
		cin >> s[i];
	}
	int j;
	for(i = 0; i < n; ++i)
	{
		cin >> t;
		int ans = 0;
		g = produce(t);
		for(j = 0; j < d; ++j)
		{
			if (compare(j))
			{
				++ans;
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << '\n';
	}
	return 0;
}