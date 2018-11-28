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
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int N = 13;

int n, m;
vector <int> g[N];
int ansPerm[N], ans;
int used[N][N], u = 0;
int minCyc;
int a[N], b[N];
int bit[30];

void clearData ()
{
}

void go (int v, int i, int cnt)
{
	if (used[v][i] == u)
	{
		minCyc = min(minCyc, cnt);
		return;
	}

	used[v][i] = u;
	
	int idx = -1;
	int to = g[v][i];
	forn(j, sz(g[to]))
		if (g[to][j] == v)
			idx = j;
			
	assert(idx != -1);
	
	idx = (idx + 1) % sz(g[to]);
	go(to, idx, cnt + 1);
}

vector <int> vs;

int perm[N];

void goo (int v, int i)
{
	if (used[v][i] == u)
		return;
		
	used[v][i] = u;
	
	vs.pb(v);
	
	int idx = -1;
	int to = g[v][i];
	
	forn(j, sz(g[to]))
		if (g[to][j] == v)
			idx = j;
			
	assert(idx != -1);
	
	idx = (idx + 1) % sz(g[to]);
	
	goo(to, idx);
}

bool check ()
{
	forn(i, n)
		forn(j, sz(g[i]))
		{
			vs.clear();
			u++;
			goo(i, j);
			
			int mask = 0;
			forn(k, sz(vs))
				mask |= bit[perm[vs[k]]];
				
			if (mask != bit[minCyc] - 1)
				return false;
		}
		
	return true;
}

bool rec (int pos, int mask)
{
	if (pos == n)
	{
		if (mask == bit[minCyc] - 1)
		{
			if (!check())
				return false;
			
			ans = minCyc;
			forn(i, n)
				ansPerm[i] = perm[i];
				
			return true;
		}
			
		return false;
	}
		
	forn(i, minCyc)
	{
		perm[pos] = i;
		
		if (rec(pos + 1, mask | bit[i]))
			return true;
	}
	
	return false;
} 

void solve ()
{
	forn(i, n)
	{
		g[i].pb((i + 1) % n);
		g[(i + 1) % n].pb(i);
	}

	forn(i, n)
		sort(all(g[i]));

	ans = 0;
	memset(ansPerm, 0, sizeof(ansPerm));
	minCyc = n;
	
	u++;
	
	forn(i, n)
		forn(j, sz(g[i]))
			if (used[i][j] != u)
				go(i, j, 0);
				
	assert(rec(0, 0));
	assert(ans == minCyc);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	forn(i, 30)
		bit[i] = (1 << i);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		cin >> n >> m;
		
		clearData();
		
		forn(i, n)
			g[i].clear();
		
		forn(i, m)
			scanf("%d", &a[i]), a[i]--;
			
		forn(i, m)
			scanf("%d", &b[i]), b[i]--;
			
		forn(i, m)
		{
			g[a[i]].pb(b[i]);
			g[b[i]].pb(a[i]);
		}
		
		solve();
		
		printf("Case #%d: %d\n", test + 1, ans);
		
		forn(i, n)
			printf("%d ", ansPerm[i] + 1);
			
		puts("");
	}

	return 0;
}
























































