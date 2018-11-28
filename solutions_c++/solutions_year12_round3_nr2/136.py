﻿// универсальный код!!!!111
// sieg!! sieg!! 1488
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>
using namespace std;

#define sz size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define sqr(x) ((x)*(x))


bool fl;
vector<bool> u;
int st;
vector<vector<int> > g;

void dfs(int v) {
	if(v != st && u[v]) {
		fl = true;
		return;
	}
	u[v] = true;
	for(int i =0; i < g[v].sz; i++) {
		dfs(g[v][i]);
	}
}

void solve() {
	int n, k;
	cin >> n;
	g.assign(n, vector<int> ());
	for(int i = 0; i < n; i++) {
		cin >> k;
		g[i].resize(k);
		for(int j =0; j < k; j++) {
			cin >> g[i][j];
			g[i][j]--;
		}
	}
	fl = false;
	for(int i = 0; i < n; i++) {
		st = i;
		u.assign(n, false);
		u[st] = true;
		dfs(i);
		if(fl) {
			puts("Yes");
			return;
		}
	}
	puts("No");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ",i );
		solve();
	}
	return 0;
}
 