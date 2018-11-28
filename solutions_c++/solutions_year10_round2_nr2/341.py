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

struct data {
	int x, v;
}p[60];

void solve() {
	int N, K, B, T;
	scanf("%d %d %d %d", &N, &K, &B, &T);
	for (int i = 0; i < N; i++) {
		scanf("%d", &p[i].x);
	}
	for (int i = 0; i < N; i++) {
		scanf("%d", &p[i].v);
	}

	int ans = 0, sum = 0;
	for (int i = N - 1; i >= 0; i--) {
		if (sum == K) {
			break;
		}
		if ((B - p[i].x) > T * p[i].v) {
			ans += K - sum;
		} else {
			sum++;
		}
	}
	if (sum == K) {
		printf("%d\n", ans);
	} else {
		printf("IMPOSSIBLE\n");
	}
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}