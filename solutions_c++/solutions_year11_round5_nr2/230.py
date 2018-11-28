#pragma comment(linker, "/STACK:512000000")

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef long double ld;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> Edge;
typedef vector<vector<Edge> > Graph;

void init()
{
	freopen("input.txt", "rt", stdin);
}

int ans;
VI p[20];
VI a;
int n;

void rec(int idx, int m)
{
	if (idx == n) {
		int localAns = n;
		forn(i, m) localAns = min(localAns, (int)p[i].size());
		ans = max(ans, localAns);
		return;
	}
	forn(i, m) {
		if (a[idx] == p[i].back() + 1) {
			p[i].pb(a[idx]);
			rec(idx + 1, m);
			p[i].pop_back();
		}
	}
	p[m].pb(a[idx]);
	rec(idx + 1, m + 1);
	p[m].pop_back();
}

int main()
{
	int tc; cin >> tc;
	forn(it, tc) {
		cin >> n;
		a.assign(n, 0);
		forn(i, n) cin >> a[i];
		forn(i, n) p[i].clear();
		sort(all(a));
		ans = 1;
		rec(0, 0);
		if (n == 0) ans = 0;
		cout << "Case #" << it + 1 << ": " << ans << endl;
	}

	return 0;
}
