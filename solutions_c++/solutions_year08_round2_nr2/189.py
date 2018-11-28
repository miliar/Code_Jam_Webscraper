#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int d[3000];

bool ok(int a, int b, int p) {
	set<int> s;
	while (a != 1) {
		s.insert(d[a]);
		a /= d[a];
	}
	while (b != 1) {
		if (d[b] >= p && s.find(d[b]) != s.end())
			return true;
		b /= d[b];
	}
	return false;
}


vector<int> adj[3000];
int color[3000];

void dfs(int v) {
	color[v] = 1;
	for (int i = 0; i < adj[v].size(); i++) {
		int u = adj[v][i];
		if (!color[u])
			dfs(u);
	}
}

long long solve() {
	int a, b, p;
	cin >> a >> b >> p;	

	for (int i = a; i <= b; i++) adj[i].clear();

	for (int i = a; i <= b; i++)
		for (int j = i + 1; j <= b; j++)
			if (ok(i, j, p)) {
				adj[i].pb(j);
				adj[j].pb(i);
			}
	long long res = 0;
	memset(color, 0, sizeof(color));
	for (int i = a; i <= b; i++) {
		if (!color[i]) {
			dfs(i);
			res++;
		}
	}
	return res;
}

void sieve() {
	int n = 2000;
	d[1] = 1;
	for (int i = 2; i <= n; i++) {
		if (d[i] == 0) {
			for (int j = i + i; j <= n; j += i)
				d[j] = i;
			d[i] = i;
		}
	}
}

int main () {
	freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
	sieve();
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %lld\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
