//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 1000000000;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, N, ans = 0, M, V;
int g[10000], c[10000];
int l[10000];
int d[10000][2];
int t[10000];

int get(int v, int w) {
	if (v >= (M - 1) / 2) {
		if (l[v - (M - 1) / 2] == w) return 0;
		return INF;
	}
	if (d[v][w] != -1) return d[v][w];
	if (t[v] == w) {
		d[v][w] = 0;
		return 0;
	}

	int ans = INF;
	int l = (v << 1) + 1, r = (v << 1) + 2;
	if (w == 1) {
		if (g[v] == 0) {
			ans = min(ans, get(l, 1) + get(r, 1));
			ans = min(ans, get(l, 0) + get(r, 1));
			ans = min(ans, get(l, 1) + get(r, 0));
		}
		if (g[v] == 0 && c[v])
			ans = min(ans, get(l, 1) + get(r, 1) + 1);
		if (g[v] == 1)
			ans = min(ans, get(l, 1) + get(r, 1));
		if (g[v] == 1 && c[v]) {
			ans = min(ans, get(l, 1) + get(r, 1) + 1);
			ans = min(ans, get(l, 0) + get(r, 1) + 1);
			ans = min(ans, get(l, 1) + get(r, 0) + 1);
		}
	} else {
		if (g[v] == 1) {
			ans = min(ans, get(l, 0) + get(r, 0));
			ans = min(ans, get(l, 0) + get(r, 1));
			ans = min(ans, get(l, 1) + get(r, 0));
		}
		if (g[v] == 1 && c[v])
			ans = min(ans, get(l, 0) + get(r, 0) + 1);
		
		if (g[v] == 0)
			ans = min(ans, get(l, 0) + get(r, 0));
		if (g[v] == 0 && c[v]) {
			ans = min(ans, get(l, 0) + get(r, 0) + 1);
			ans = min(ans, get(l, 0) + get(r, 1) + 1);
			ans = min(ans, get(l, 1) + get(r, 0) + 1);
		}
	}
	d[v][w] = ans;
	return ans;
}

void makeTree(int v) {
	if (v >= (M - 1) / 2) {
		t[v] = l[v - (M - 1) / 2];
		return;
	}
	makeTree((v << 1) + 1);
	makeTree((v << 1) + 2);
	if (g[v] == 1) t[v] =  t[(v << 1) + 1] & t[(v << 1) + 2]; else
	t[v] =  t[(v << 1) + 1] | t[(v << 1) + 2];
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> N;
	forn(test, N) {
		memset(d, 255, sizeof(d));
		cin >> M >> V;
		forn(i, (M - 1) / 2)
			scanf("%d%d", &g[i], &c[i]);
		forn(i, (M + 1) / 2)
			scanf("%d", &l[i]);
		makeTree(0);
		ans = get(0, V);
		if (ans == INF) printf("Case #%d: IMPOSSIBLE\n", test + 1);else
		printf("Case #%d: %d\n", test + 1, ans);
	}
	

	return 0;
}

 
