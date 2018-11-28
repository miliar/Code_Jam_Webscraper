#include <iostream>
#include <set>
#include <string>

#define forn(i, n) for(int i = 0; i < (n); ++i)
using namespace std;

int len, d, n, ans;
set<string> dict[16];
string pattern;

void solve(string cur, int pos)
{
	if(pos >= pattern.size())
	{
		ans += dict[cur.size()].count(cur);
		return;
	}
	if(dict[cur.size()].count(cur) == 0)
		return;
	if(pattern[pos] == '(')
	{
		int cls;
		for(cls = pos + 1; pattern[cls] != ')'; ++cls);
		for(int i = pos + 1; i < cls; ++i)
			solve(cur + pattern[i], cls + 1);
	}
	else
		solve(cur + pattern[pos], pos + 1);
}

void main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d %d %d\n", &len, &d, &n);
	dict[0].insert("");
	forn(i, d)
	{
		string t;
		getline(cin, t);
		for(int j = 1; j <= t.size(); ++j)
			dict[j].insert(t.substr(0, j));
	}

	for(int itm = 1; itm <= n; ++itm)
	{
		ans = 0;
		getline(cin, pattern);
		solve(string(""), 0);
		printf("Case #%d: %d\n", itm, ans);
	}
}