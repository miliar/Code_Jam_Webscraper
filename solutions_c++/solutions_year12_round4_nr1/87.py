#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

int n;

int l[10010], d[10010];
int dx;
bool found;
set<pair<int, int> > seen;

bool bt(int i, int y)
{
	if (i == n) {
		found = true;
		return true;
	}
	//
	if (seen.find(make_pair(i, y)) != seen.end()) return false;
	seen.insert(make_pair(i, y));
	for (int j = i + 1; j <= n; j++) {
		if (d[j] - d[i] > y) break;
		if (bt(j, min(l[j], d[j] - d[i]))) return true;
	}
	return false;
}

bool solve(void)
{
	seen.clear();
	found = false;
	return bt(0, d[0]);
}

int main(void)
{
	int T;
// 	freopen("/home/vesko/gcj/a.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d", &n);
		FOR(i, n) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &dx);
		d[n] = dx;
		l[n] = 1000000001;
		printf("Case #%d: %s\n", tc, solve() ? "YES" : "NO");
	}
	
	return 0;
}
