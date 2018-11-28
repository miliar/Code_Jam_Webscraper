#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

int g[105];
bool f[105];
int n, surprises, points, ans;

bool canBeSurprise (int p) {
	int temp = p - points;
	return (temp >= 0 && temp >= max((points - 2) * 2, 0));
}

void solve () {
	int i, cur;

	scanf("%d%d%d", &n, &surprises, &points);
	for (i = 0;i < n;i++) {
		scanf("%d", &g[i]);
	}

	memset(f, false, sizeof(f));

	ans = 0;

	for (i = 0;i < n;i++) {
		cur = g[i] / 3;
		if (g[i] % 3)
			cur++;
		if (cur >= points) {
			f[i] = true;
			ans++;
		}
	}

	int cnt = 0;
	for (i = 0;i < n;i++) {
		if (!f[i] && canBeSurprise(g[i]))
			cnt++;
	}

	ans += min(cnt, surprises);

	printf("%d", ans);
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0;t < test;t++) {
		if (t)
			printf("\n");
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}