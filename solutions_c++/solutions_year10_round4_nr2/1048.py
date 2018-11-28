#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int p;
int cost[15][4000] = {{}};
int visits[4000] = {};

int tree(int round, int a, int b, int seen, int magic) {
//	printf("tree(%d %d %d %d %d)\n", round, a, b, seen, magic); fflush(stdout);
	if (round == p) {
		assert(a == b);
		return visits[a] < seen? 0 : (1 << 29);
	}

	int buy, defer;

	buy =	tree(round+1, a, (a+b)/2, seen+1, magic*2) +
			tree(round+1, (a+b)/2+1, b, seen+1, magic*2+1) +
			cost[round][magic];
	defer = tree(round+1, a, (a+b)/2, seen, magic*2) +
			tree(round+1, (a+b)/2+1, b, seen, magic*2+1);

	buy = buy > (1 << 29) ? (1 << 29) : buy;
	defer = defer > (1 << 29) ? (1 << 29) : defer;

	return min(buy, defer);
}

void solve() {
	scanf("%d", &p);

	for (int i = 0; i < (1 << p); i++) {
		scanf("%d", &visits[i]);
		visits[i] = p-1-visits[i];
	}
	
	for (int i = 0; i < p; i++) {
		for (int k = 0; k < 1 << (p-i-1); k++) {
			scanf("%d", &cost[p-1-i][k]);
		}
	}

	int res = tree(0, 0, (1 << p)-1, 0, 0);
	printf("%d\n", res);
}

int main() {
	freopen("cup.in", "r", stdin);
#ifndef DEBUG
	freopen("cup.out", "w", stdout);
#endif
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i+1);
		solve();
	}
	
	return 0;
}
