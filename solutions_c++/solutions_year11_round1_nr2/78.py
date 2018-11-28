#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
//#include <complex>

using namespace std;

void ASS(bool b)
{
	if (!b)
	{
		++*(int*)0;
	}
}

#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))

#pragma comment(linker, "/STACK:106777216")

typedef vector<int> vi;
typedef long long LL;

vector<string> w;
string s;

bool Less(pair<int, int> res, pair<int, int> t)
{
	return res.first < t.first || res.first == t.first && res.second > t.second;
}

pair<int, int> S(const vi& v, int p)
{
	if (v.size() == 1)
		return make_pair(0, v[0]);
	
	ASS(p < 26);

	map<int, vi> mp;
	FOR(i, v.size())
	{
		const string& ss = w[v[i]];
		int M = 0;
		FOR(j, ss.size())
			if (ss[j] == s[p])
				M |= (1 << j);
		mp[M].push_back(v[i]);
	}

	pair<int, int> res(-1, 0);
	for (map<int, vi>::iterator it = mp.begin(); it != mp.end(); it++)
	{
		pair<int, int> t = S(it->second, p + 1);
		if (t.second == 0)
		{
			p = p;
		}
		if (it->first == 0 && mp.size() > 1)
			t.first++;
		char C = s[p];
		if (Less(res, t))
			res = t;
	}
	return res;
}

int Solve0()
{
	cin >> s;
	pair<int, int> res(0, 0);
	for (int d = 1; d <= 10; d++)
	{
		vi v;
		FOR(i, w.size())
			if (w[i].size() == d)
				v.push_back(i);
		if (v.size() == 0)
			continue;
		pair<int, int> t = S(v, 0);
		if (Less(res, t))
			res = t;
	}
//	printf("ERR %d\n", res.first);
	return res.second;
}

void Solve()
{
	int n, m;
	cin >> n >> m;
	w.resize(n);
	FOR(i, n)
	{
		string s;
		cin >> w[i];
	}
	FOR(i, m)
	{
		if (i ) printf(" ");
		int res = Solve0();
		printf("%s", w[res].c_str());
	}
	printf("\n");
}

int main()
{
//#ifndef _DEBUG
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
//#endif
	int n;
	cin >> n;
	FOR(i, n)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}