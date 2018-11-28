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

struct Trip
{
	int l, r;
};

#define NMAX 105

Trip ab[NMAX], ba[NMAX];
int na, nb, t;

struct Event
{
	int time;
	bool dep;
	bool toA;
};

inline bool operator<(const Event& e1, const Event& e2)
{
	if (e1.time != e2.time) return e1.time < e2.time;
	if (e1.dep != e2.dep) return e1.dep < e2.dep;
	return e1.toA < e2.toA;
}

int toInt(string s)
{
	return (s[0] - '0') * 600 + (s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';
}

bool can(int a, int b)
{
	int cntA = a, cntB = b;
	multiset<Event> e;
	forn(i, na)
	{
		Event e1 = {ab[i].l, true, false};
		Event e2 = {ab[i].r + t, false, false};
		e.insert(e1);
		e.insert(e2);	
	}
	forn(i, nb)
	{
		Event e1 = {ba[i].l, true, true};
		Event e2 = {ba[i].r + t, false, true};
		e.insert(e1);
		e.insert(e2);	
	}
	while (!e.empty())
	{
		Event cur = *(e.begin());
		e.erase(e.begin());
		if (!cur.toA)
		{
			if (cur.dep)
			{
				if (cntA == 0) return false;
				cntA--;
			}
			else
			{
				cntB++;
			}
		}
		else
		{
			if (cur.dep)
			{
				if (cntB == 0) return false;
				cntB--;
			}
			else
			{
				cntA++;
			}
		}
	}
	return true;
}

void solve(int tc)
{
	cin >> t >> na >> nb;
	forn(i, na)
	{
		string s1, s2;
		cin >> s1 >> s2;
		ab[i].l = toInt(s1);
		ab[i].r = toInt(s2);
	}
	forn(i, nb)
	{
		string s1, s2;
		cin >> s1 >> s2;
		ba[i].l = toInt(s1);
		ba[i].r = toInt(s2);
	}
	forn(a, na + 1)
	{
		forn(b, nb + 1)
		{
			if (can(a, b))
			{
				printf("Case #%d: %d %d\n", tc, a, b);
				return;
			}
		}
	}
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	scanf("%d\n", &tc);
	forn(it, tc) solve(it + 1);
	return 0;
}
         	
