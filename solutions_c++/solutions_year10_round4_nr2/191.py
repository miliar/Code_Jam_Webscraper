#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
using namespace std;
#define FOR(i, n) for (int i = 0; i < (int) (n); i++)

#define MAXN 1024
#define MAXP 10
#define INF 1025000000

int n, p;

int nmiss[MAXP+1][MAXN];
int dp[MAXP+1][MAXP+1][MAXN];
int costs[MAXP+1][MAXN];

int f(int lev, int i, int decr)
{
	if (lev == p) return 0;
	int& d = dp[lev][decr][i];
	if (d != -1) return d;
	d = INF;
	if (nmiss[lev][i] > decr)
		d = f(lev + 1, i * 2, decr + 1) + f(lev + 1, i * 2 + 1, decr + 1);
	d = min(d, costs[lev][i] + f(lev + 1, i * 2, decr) + f(lev + 1, i * 2 + 1, decr));
	return d;
}

int solve(void)
{
	memset(nmiss, 0, sizeof(nmiss));
	memset(dp, 0xff, sizeof(dp));
	memset(costs, 0, sizeof(costs));
	scanf("%d", &p);
	n = 1 << p;
	for (int i = 0; i < n; i++)
		scanf("%d", &nmiss[p][i]);
	for (int j = p - 1; j >= 0; j--) {
		for (int i = 0; i < (1 << j); i++) {
			scanf("%d", &costs[j][i]);
			nmiss[j][i] = min(nmiss[j + 1][2 * i], nmiss[j + 1][2 * i + 1]);
		}
	}
	//
	return f(0, 0, 0);
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %d\n", tc, solve());
	}
	return 0;
}
