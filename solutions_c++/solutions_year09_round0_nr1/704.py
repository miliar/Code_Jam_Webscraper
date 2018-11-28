#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()

typedef long double ld;
typedef long long int64;
typedef pair<ld, ld> pt;

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define y1 PALEVO

char buff[3000];

string dd[5000];

bool ok[15][26];

int l, d, n;

inline void set_pattern(const string& s)
{
	bool in = false;
	int idx = 0;
	for (int i = 0; i < (int)s.size(); i++)
	{
		if (s[i] == '(')
		{
			in = true;
			continue;
		}
		if (s[i] == ')')
		{
			in = false;
			++idx;
			continue;
		}
		ok[idx][s[i] - 'a'] = true;
		if (!in)
			++idx;
	}
}

inline bool check(const string& s)
{
	for (int i = 0; i < (int)s.length(); i++)
	{
		if (!ok[i][s[i] - 'a'])
			return false;
	}
	return true;
}

int main()
{
	
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cin >> l >> d >> n;
	for (int i = 0; i < d; i++)
	{
		scanf("%s", buff);
		dd[i] = buff;
	}
	for (int i = 0; i < n; i++)
	{
		scanf("%s", buff);
		memset(ok, 0, sizeof ok);
		set_pattern(buff);
		int ans = 0;
		for (int j = 0; j < d; j++)
		{
			if (check(dd[j]))
				++ans;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}

