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

const int N = 100 + 13;

int n, s, p;
int t[N];
int z[N][N];

const int m = 3;
int v[m];

inline bool correctTriplet (int a, int b, int c)
{	
	v[0] = a;
	v[1] = b;
	v[2] = c;
	
	sort (v, v + m);

	forn (i, m)
		forn (j, i)
			if (v[i] - v[j] > 2)
				return false;

	return true;
}

inline bool isSurprisingTriplet (int a, int b, int c)
{	
	v[0] = a;
	v[1] = b;
	v[2] = c;
	
	sort (v, v + m);

	forn (i, m)
		forn (j, i)
			if (v[i] - v[j] == 2)
				return true;

	return false;
}

inline int max (int a, int b, int c)
{
	return max (a, max (b, c));
}

int lazy (int idx, int cnt)
{
	int &ans = z[idx][cnt];
	if (ans != -1)
		return ans;

	if (idx == n)
	{
		if (cnt != s)
			return -INF;

		return 0;
	}

	ans = 0;

	for (int i = 0; i <= 10; i++)
	{
		for (int j = 0; j <= 10; j++)
		{
			int k = t[idx] - i - j;
		
			if (k < 0)
				continue;

			if (!correctTriplet (i, j, k))
				continue;

			int add = ((max (i, j, k) >= p)? 1: 0);

			if (isSurprisingTriplet (i, j, k))
			{
				if (cnt < s)
					ans = max (ans, add + lazy (idx + 1, cnt + 1));
			}
			else
			{
				ans = max (ans, add + lazy (idx + 1, cnt));
			}				
		}
	}

	return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int tests;
	cin >> tests;

	forn (test, tests)
	{
		cin >> n >> s >> p;

		forn (i, n)
			scanf ("%d", &t[i]);
		
		memset (z, -1, sizeof z);
		
		int res = lazy (0, 0);
		assert (res >= 0 && res <= n);

		printf ("Case #%d: %d\n", test + 1, res);
	}

	return 0;
}