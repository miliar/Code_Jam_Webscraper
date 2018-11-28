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

int n;
int next[5000];
ll h[5000];
bool broken = false;

void fix(int a, int b, int diff)
{
	if (a == b) return;
	int c = next[a];
	if (c > b) {
		broken = true;
		return;
	}
	if (a >= b - 1) return;
	if (broken) return;
	for (int i = c - 1; i >= a + 1; i--) {
		h[i] = h[i + 1] - diff;
		if (h[i] < 0) {
			broken = true;
			return;
		}
	}
	fix(a + 1, c, diff + 1);
	fix(c, b, diff + 1);
}

void solve(void)
{
	broken = false;
	FOR(i, n) h[i] = 1000000000;
	fix(0, n - 1, 1);
	ll mi = h[0];
	FOR(i, n) mi = min(h[i], mi);
	if (mi < 0) broken = true;
	if (!broken) {
		FOR(i, n) {
			if (i) printf(" ");
			printf("%lld", h[i] - mi);
		}
		printf("\n");
	} else {
		printf("Impossible\n");
	}
}

int main(int argc, char ** argv)
{
	int T;
// 	freopen("/home/vesko/gcj/c.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d", &n);
		FOR(i, n-1) {
			scanf("%d", &next[i]);
			next[i]--;
		}
		printf("Case #%d: ", tc);
		solve();
	}
	
	return 0;
}
