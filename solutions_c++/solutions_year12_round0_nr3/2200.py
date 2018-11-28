#pragma comment(linker, "/stack:64000000")
#include <algorithm>
#include <iostream>
#include <cassert>
#include <climits>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <memory.h>
#include <vector>
#include <bitset>
#include <string>
#include <deque>
#include <queue>
#include <ctime>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb push_back
#define pii pair <int, int>
#define vi vector <int>
#define mp make_pair

template <typename X> inline X abs (const X &a) {return a < 0? -a: a;}
template <typename X> inline X sqr (const X &a) {return a * a;}

const int INF = INT_MAX / 2;
const ll INF64 = LLONG_MAX / 2LL;
const ld EPS = 1E-9, PI = 3.1415926535897932384626433832795;

const int N = 2 * 1000 * 1000 + 3;

inline string toString (int x)
{
	string res = "";
	while (x)
	{
		res = char (x % 10 + '0') + res;
		x /= 10;
	}

	return res;
}

inline int toInt (const string &s)
{
	int res = 0;
	
	forn (i, sz (s))
		res = res * 10 + s[i] - '0';

	return res;
}

vector <int> g[N];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	for (int i = 1; i < N; i++)
	{
		string s = toString (i);

		forn (j, sz (s) - 1)
		{
			string t = s.substr (j + 1) + s.substr (0, j + 1);
			
			if (t[0] == '0')
				continue;

			int x = toInt (t);
			if (x <= i)
				continue;

			g[i].pb (x);
		}

		sort (all (g[i]));
		g[i].erase (unique (all (g[i])), g[i].end());

	}

	cerr << clock() << endl;

	int tests;
	cin >> tests;

	forn (test, tests)
	{
		int a, b;
		cin >> a >> b;

		int ans = 0;

		for (int i = a; i <= b; i++)
			ans += int (upper_bound (all (g[i]), b) - g[i].begin());

		printf ("Case #%d: %d\n", test + 1, ans);
	}

	cerr << clock() << endl;

	return 0;
}