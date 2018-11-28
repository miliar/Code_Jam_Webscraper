#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

void solve() {
	int n, k;
	scanf("%d %d", &n, &k);
	k %= (1 << n);
	if (k == (1 << n) - 1) {
		printf("ON\n");
	} else {
		printf("OFF\n");
	}
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}