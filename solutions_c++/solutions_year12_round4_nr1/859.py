#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
using namespace std;

map<int, int> t;
int d[10000 + 3];
int l[10000 + 3];
queue<int> Q;
set<int> S;

bool solve() {
	while (!Q.empty())
		Q.pop();

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", &d[i], &l[i]);
	int D;
	scanf("%d", &D);

	t.clear();
	S.empty();

	t[d[0]] = d[0];
	Q.push(d[0]);
	S.insert(d[0]);
	while (!Q.empty()) {
		int x = Q.front();
		//cout << x << endl;
		Q.pop();
		S.erase(x);
		int xdo = x + t[x];
		if (xdo >= D)
			return true;
		int li = lower_bound(d, d + n, x + 1) - d;
		int ui = upper_bound(d, d + n, xdo) - d;
		for (int i = li; i < ui; i++) {
			int cnt = t.count(d[i]);
			t[d[i]] = max(cnt > 0 ? t[d[i]] : -1, min(d[i] - x, l[i]));
			if (S.count(d[i]) == 0) {
				Q.push(d[i]);
				S.insert(d[i]);
			}
		}
	}
	return false;
}

int main() {
	int ilz;
	scanf("%d", &ilz);
	for (int xz = 1; xz <= ilz; xz++) {
		printf("Case #%d: ", xz);
		if (solve())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
