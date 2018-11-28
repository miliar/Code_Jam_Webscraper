#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <cassert>
#include <cmath>
#include <deque>
#include <sstream>
using namespace std;
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define only(v) v.erase(unique(all(v)), v.end())
typedef  vector<int> VI;
typedef  pair<int, int> pii;
typedef vector<string> VS;
#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
vector<vector<pair<string, int> > > g;
int cnt;

vector<string> parse(string s) 
{
	vector<string> t;
	string tmp;
	forv(i, s)
	{
		if (s[i] == '/')
		{
			if (tmp.size())
				t.pb(tmp);
			tmp = "";
		}
		else
		{
			tmp += s[i];
		}
	}
	t.pb(tmp);
	return t;
}

int add(vector<string> v) 
{
	int ret = 0;
	int cur = 0;
	forv(i, v)
	{
		int next = -1;
		forv(j, g[cur])
		{
			if (g[cur][j].first == v[i])
			{
				next = g[cur][j].second;
				break;
			}
		}										
		if (next == -1)
		{
			ret++;
			next = cnt++;
			g[cur].pb(mp(v[i], next));	
			g.pb(vector<pair<string, int> >());
		}
		cur = next;
	}
	return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
#endif
	int tc; cin >> tc;
	forn(it, tc) 
	{
		cnt = 1;
		g.clear();
		g.pb(vector<pair<string, int> >());
		int n, m; cin >> n >> m;
		forn(i, n)
		{
			string s; cin >> s;
			vector<string> v = parse(s);
			add(v);
		}
		int ans = 0;
		forn(i, m)
		{
			string s; cin >> s;
			vector<string> v = parse(s);
			ans += add(v);
		}
		printf("Case #%d: %d\n", it+1, ans);
	}

	return 0;
}
