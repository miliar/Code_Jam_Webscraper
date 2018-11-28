#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
#include <bitset>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

char s[6000];
int k, Z, n;

int g[40][40];
int indegree[40], outdegree[40];
int loop[40];
int alt[256];
int mp[256];
char rmap[256];

bool todo(void)
{
	FOR(i, 40) if (indegree[i] || outdegree[i]) return true;
	return false;
}

void solve(void)
{
	scanf("%d%s", &k, s);
	memset(g, 0, sizeof(g));
	n = (int) strlen(s);
	FOR(i, n - 1) {
		char a = s[i];
		char b = s[i + 1];
		g[mp[a]][mp[b]] = 1;
		if (alt[a])
			g[mp[alt[a]]][mp[b]] = 1;
		if (alt[b])
			g[mp[a]][mp[alt[b]]] = 1;
		if (alt[a] && alt[b])
			g[mp[alt[a]]][mp[alt[b]]] = 1;
	}
	memset(indegree, 0, sizeof(indegree));
	memset(outdegree, 0, sizeof(outdegree));
	memset(loop, 0, sizeof(loop));
	FOR(i, 40) FOR(j, 40) if (g[i][j]) {
		outdegree[i]++;
		indegree[j]++;
		if (i == j) loop[i] = 1;
	}
	/*
	int rlen = 0;
	while (todo()) {
		int i = 0;
		int mindeg = 0;
		FOR(j, 40) {
			if (outdegree[j] > mindeg) {
				mindeg = outdegree[j];
				i = j;
			}
		}
		rlen++;
		vector<int> verts;
		while (1) {
			verts.push_back(i);
			int j = 0;
			while (j < 40 && !g[i][j]) j++;
			if (j < 40) {
				g[i][j] = 0;
				outdegree[i]--;
				indegree[j]--;
				i = j;
				rlen++;
			} else break;
		}
	}
	printf("%d\n", rlen);
	*/
	int minans = 999666111;
	int inputs = 0, outputs = 0;
	FOR(start, 40) if (outdegree[start]) {
		int totale = 0;
		FOR (i, 40) {
			totale += outdegree[i]*2;
			totale -= min(indegree[i], outdegree[i] - (start == i));
		}
		minans = min(minans, totale);
	}
	printf("%d\n", minans);
}

int main(void)
{
	alt['o'] = '0';
	alt['i'] = '1';
	alt['e'] = '3';
	alt['a'] = '4';
	alt['s'] = '5';
	alt['t'] = '7';
	alt['b'] = '8';
	alt['g'] = '9';
	Z = 0;
	memset(mp, 0xff, sizeof(mp));
	for (char c = 'a'; c <= 'z'; c++) {
		mp[c] = Z;
		rmap[Z] = c;
		Z++;
	}
	for (char c = 'a'; c <= 'z'; c++) {
		if (!alt[c]) continue;
		char ca = alt[c];
		mp[ca] = Z;
		rmap[Z] = ca;
		Z++;
	}
	int T;
// 	freopen("/home/vesko/gcj/d.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
