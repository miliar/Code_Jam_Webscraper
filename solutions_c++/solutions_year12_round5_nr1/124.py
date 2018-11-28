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

struct Level {
	int idx;
	int p, len;
};

vector<Level> a;
ll eval(int idx[], int n)
{
	ll sum = 0;
	ll xcost = 0;
	for (int i = 0; i < n; i++) {
		xcost += sum * a[idx[i]].p;
		sum += a[idx[i]].len;
	}
	return xcost;
}

void solve(void)
{
	a.clear();
	int n;
	scanf("%d", &n);
	a.resize(n);
	FOR(i, n) scanf("%d", &a[i].len);
	FOR(i, n) {
		scanf("%d", &a[i].p);
	}
	FOR(i, n) a[i].idx = i;
	/*
	sort(a.rbegin(), a.rend());
	FOR(i, n) {
		if (i) printf(" ");
		printf("%d", a[i].idx);
	}
	printf("\n");
	*/
	int indices[1024], best[1024];
	indices[0] = 0;
	for (int i = 1; i < n; i++) {
		ll minCost = 0x3333ffff3333ffffLL;
		for (int j = 0; j <= i; j++) {
			int nindices[1024];
			for (int k = 0; k < j; k++)
				nindices[k] = indices[k];
			nindices[j] = i;
			for (int k = j + 1; k <= i; k++)
				nindices[k] = indices[k - 1];
			ll cost = eval(nindices, i + 1);
			if (cost <= minCost) {
				minCost = cost;
				memcpy(best, nindices, (i + 1) * 4);
			}
		}
		memcpy(indices, best, sizeof(indices));
	}
	FOR(i, n) {
		if (i) printf(" ");
		printf("%d", indices[i]);
	}
	printf("\n");
}

int main(void)
{
	int T;
// 	freopen("/home/vesko/gcj/a.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
