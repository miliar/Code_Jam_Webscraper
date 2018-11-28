#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

const int NMAX = 60000;

struct Node {
	int c, g, v;
};

#define LF(v) (v * 2)
#define RG(v) (v * 2 + 1)
const int INF = 100000000;

Node tree[NMAX];

int value, n, m;

int d[2][NMAX];

void dfs(int v) {
	if (v > m) {
		d[(int)tree[v].v][v] = 0;
		return;
	}	
	dfs(LF(v));
	dfs(RG(v));
	forn(i, 2) {
		if (d[i][LF(v)] == INF) continue;
		forn(j, 2) {
			if (d[j][RG(v)] == INF) continue;
			int t;
			if (tree[v].g) {
				t = i & j;
			} else {
				t = i | j;
			}
			d[t][v] = min(d[t][v], d[i][LF(v)] + d[j][RG(v)]);
			if (!tree[v].c) {
				continue;
			}
			if (!tree[v].g) {
				t = i & j;
			} else {
				t = i | j;
			}
			d[t][v] = min(d[t][v], d[i][LF(v)] + d[j][RG(v)] + 1);
		}
	}
}


int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc; cin>> tc;
	forn(it, tc) {
		int v;
		scanf("%d %d", &n, &v);
		for1(i, n) d[0][i] = d[1][i] = INF;
		m = (n-1) / 2;
		forn(i, m) {
			int c, g; scanf("%d %d", &g, &c);
			tree[i+1].c = (c);
			tree[i+1].g = (g);
		}
		forn(i, n - m) {
			int v; scanf("%d", &v);
			tree[m + i + 1].v = (v);
		}
		dfs(1);
		printf("Case #%d: ", it+1);
		if (d[v][1] == INF) cout << "IMPOSSIBLE\n";
		else cout << d[v][1] << endl;
	}

	return 0;
}
