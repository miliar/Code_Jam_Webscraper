#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 1005;

lint n, m;
int d[MAXN];
int id[MAXN];
int a[MAXN];

lint solvea()
{
	__(d);
	_(id, -1);
	int i, j;
	int res = 0;
	for (i = 0; i < n; ++ i) {
		int v = a[i];
		int add = 0;
		if (i == 0 && v == 1) {
			add = 1;
		}
		for (j = 2; j * j <= v; ++ j)
		{
			int c = 0;
			while (v % j == 0) {
				++ c;
				v /= j;
			}
			if (d[j] < c) {
				d[j] = c;
				add = 1;
				id[j] = a[i];
			}
		}
		if (v > 1) {
			int c = 1;
			if (d[v] < c) {
				d[v] = c;
				add = 1;
				id[v] = a[i];
			}			
		}
		res += add;
	}
	return res;
}

void solve() {
	int i, j, k;
	cin >> n;
	for (i = 0; i < n; ++ i) {
		a[i] = i + 1;
	}
	lint p1 = solvea();
	set<int> bb, aa = set<int>(a, a + n);
	for (i = 1; i <= n; ++ i) {
		if (id[i] >= 0) {
			bb.insert(id[i]);
			aa.erase(id[i]);
		}
	}
	VI vb(all(bb));
	VI va(all(aa));
	for (i = 0; i < sz(vb); ++ i) {
		a[i] = vb[i];  
	}
	for (j = 0; j < sz(va); ++ j) {
		a[i++] = va[j];  
	}
	assert(i == n);
	lint p2 = solvea();
	cout << p1 - p2 << endl;
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}