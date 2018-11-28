#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define ft first
#define sc second

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long double ld;
typedef pair<ld, ld> ptd;
typedef pair <int, int> pt;
typedef long long li;
typedef unsigned char byte;

const ld PI = 3.1415926535897932384626433832795;
const int INF = 1000 * 1000 * 1000;

const int N = 200 + 13;
const ld EPS = 1e-9;

int n, d;
int x[N], cnt[N];
pt xs[N];

bool can (ld mid)
{
	ld rg = -1e18;
	
	forn(i, n)
	{
		ld len = (xs[i].sc - 1) * 1.0 * d;
		
		ld lf = max(rg, xs[i].ft - mid);
		ld nrg = lf + len;

		if (abs(xs[i].ft - lf) > mid + EPS)
			return false;
		
		if (abs(xs[i].ft - nrg) > mid + EPS)
			return false;
		
		rg = nrg + d;
	}
	
	return true;
}

ld solve ()
{
	ld lf = 0.0, rg = 1e18;
	
	forn(i, 300)
	{
		ld mid = (lf + rg) / 2.0;
		
		if (can(mid))
			rg = mid;
		else
			lf = mid;
	}
	
	return lf;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		scanf("%d%d", &n, &d);
		
		forn(i, n)
		{
			scanf("%d%d", &x[i], &cnt[i]);
			xs[i] = mp(x[i], cnt[i]);
		}
		
		sort(xs, xs + n);
			
		printf("Case #%d: %.8lf\n", test + 1, double(solve()));
	}

	return 0;
}
























































