#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

int k;
string s;

string apply(string& s, vector<int>& p)
{
	string ret = s;
	for (int l = 0; l < (int)s.size(); l += k)
	{
		forn(i, k)
		{
			ret[l + i] = s[l + p[i]];
		}		
	}
	return ret;
}

int calc(string s)
{
	int ret = 0;
	int l = 0;
	while (l < (int)s.size())
	{
		int r = l;
		while (r < (int)s.size() && s[l] == s[r]) ++r;
		++ret;
		l = r;
	}
	return ret;
}

void solve(int tc)
{
	cin >> k;
	cin >> s;
	vector<int> p;
	p.resize(k);
	forn(i, k) p[i] = i;
	int f = 1;
	for1(i, k) f *= i;
	int bestLen = 100000;
	forn(it, f)
	{
		string t = apply(s, p);
		bestLen = min(bestLen, calc(t));
		next_permutation(all(p));
	}
	printf("Case #%d: %d\n", tc, bestLen);
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	cin >> tc;
	forn(it, tc) solve(it + 1);	
	return 0;
}
         	
