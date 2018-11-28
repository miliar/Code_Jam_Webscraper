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

#define NMAX 302

struct Segm
{
	int l, r;
	Segm() {};
	Segm(int _l, int _r)
	{
		l = _l;
		r = _r;
	}
};

inline bool operator<(const Segm& s1, const Segm& s2)
{
	if (s1.l != s2.l) return s1.l < s2.l;
	return s1.r > s2.r;
}

string col[NMAX];
int a[NMAX], b[NMAX], c[NMAX];
map<string, int> num;
vector<int> id[NMAX];
Segm s[NMAX];

int getNum(string s)
{
	if (num.count(s) == 0)
	{
		num.insert(mp(s, (int)num.size()));
	}
	return num[s];
}

int calc(int c1, int c2, int c3)
{
	int cs = 0;
	forv(i, id[c1])
	{
		s[cs].l = a[id[c1][i]];
		s[cs].r = b[id[c1][i]];
		++cs;
	}
	if (c2 != c1)
	{
		forv(i, id[c2])
		{
			s[cs].l = a[id[c2][i]];
			s[cs].r = b[id[c2][i]];
			++cs;
		}
	}
	if (c3 != c2)
	{
		forv(i, id[c3])
		{
			s[cs].l = a[id[c3][i]];
			s[cs].r = b[id[c3][i]];
			++cs;
		}
	}
	sort(s, s + cs);
	if (s[0].l != 1) return 500;
	int ptr = 1;
	int cr = s[0].r;
	int ans = 1;
	while (true)
	{
		if (cr == 10000) return ans;
		int mx = cr;
		while (ptr < cs && s[ptr].l <= cr + 1)
		{
			mx = max(mx, s[ptr].r);
			++ptr;
		}
		if (mx == cr) return 500;
		++ans;
		cr = mx;
	}
	return 500;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    int n;
    cin >> n;
	num.clear();
	forn(i, n) id[i].clear();
    forn(i, n)
    {
        cin >> col[i] >> a[i] >> b[i];
		c[i] = getNum(col[i]);
		id[c[i]].pb(i);
    }
	int m = num.size();
    int mn = 500;
    forn(c1, m)
	{
		forn(c2, c1 + 1)
		{
			forn(c3, c2 + 1)
			{
				mn = min(mn, calc(c1, c2, c3));
			}
		}
	}
	if (mn == 500) printf("IMPOSSIBLE\n"); else printf("%d\n", mn);
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
            
