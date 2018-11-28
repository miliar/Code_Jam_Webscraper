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
#include <bitset>
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
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
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
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int N = 1000 + 13;

int n, w, h;
pt r[N];

inline ld dist (const pt& a, const pt& b)
{
	return sqrt(sqr(ld(a.ft - b.ft)) + sqr(ld(a.sc - b.sc)));
}

inline bool cmp (const pair <pt, int>& a, const pair <pt, int>& b)
{
	return a.sc < b.sc;
}

void solve (int test)
{
	int it = 0;
	int curx = 0, cury = 0;
	int maxInCol = 0;
	
	printf("Case #%d: ", test + 1);
	
	vector <pair <pt, int> > pl;
	
	while (it < n)
	{
		assert(curx <= w && cury <= h);
		
		//printf("%d %d ", curx, cury);
		pl.pb(mp(mp(curx, cury), r[it].sc));
		
		maxInCol = max(maxInCol, r[it].ft);
		cury += r[it].ft;
		it++;
		if (it == n) break;
		
		cury += r[it].ft;
		
		if (cury > h)
		{
			curx += maxInCol + r[it].ft;
			cury = 0;
			maxInCol = 0;
		}
	}
	
	//forn(i, sz(pl))
	//	forn(j, i)
	//		assert(dist(pl[i], pl[j]) + EPS > r[i] + r[j]);
	
	sort(all(pl), cmp);
	
	forn(i, sz(pl))
		printf("%d %d ", pl[i].ft.ft, pl[i].ft.sc);
		
	puts("");
}

void read ()
{
	scanf("%d%d%d", &n, &w, &h);
	
	forn(i, n)
		scanf("%d", &r[i].ft), r[i].sc = i;
		
	sort(r, r + n);
	reverse(r, r + n);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		read();
		solve(test);
	}

	return 0;
}
























































