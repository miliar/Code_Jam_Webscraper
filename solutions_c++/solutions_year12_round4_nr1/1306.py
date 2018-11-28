#include <cstdio>
#include <set>
#include <utility>
#include <algorithm>

using namespace std;

int n;
int d[100], l[100];
int D;
set<pair<int, int> > hash;
bool can;

void dfs(int k, int p) {
	if (can)
		return;
	if (p >= D - d[k]) {
		//printf("%d %d\n", k, p);
		can = true;
		return;
	}
	hash.insert(make_pair(k, p));
	for (int i = 0; i < n; i++) {
		if (i != k && p >= abs(d[i] - d[k])) {
			int nk = i, np = min(abs(d[i] - d[k]), l[i]);
			if (!hash.count(make_pair(nk, np))) {
				dfs(nk, np);
			}
		}
	}
}

int main() {
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++) {
		printf("Case #%d: ", tt);
		hash.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);
		can = false;
		dfs(0, d[0]);
		if (can)
			printf("YES\n");
		else
			printf("NO\n");
	}
}