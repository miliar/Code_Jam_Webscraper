#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair <int, int> PII;

int T, n;
int a[10000];

bool gao(int pm) {
	priority_queue <PII, vector <PII>, greater <PII> > q;
	q.push(make_pair(a[0], 1));
	for (int i = 1; i < n; ++i) {
		while (!q.empty() && q.top().first + 1 < a[i]) {
			if (q.top().second < pm) {
				return false;
			}
			q.pop();
		}
		if (q.empty()) {
			q.push(make_pair(a[i], 1));
		} else {
			pair <int, int> p = q.top();
			if (p.first + 1 == a[i]) {
				q.pop();
				++p.first;
				++p.second;
				q.push(p);
			} else {
				q.push(make_pair(a[i], 1));
			}
		}
	}
	while (!q.empty()) {
		if (q.top().second < pm) {
			return false;
		}
		q.pop();
	}
	return true;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}
		sort(a, a + n);
		int pl = 0, pr = n + 1;
		while (pl + 1 < pr) {
			int pm = pl + (pr - pl) / 2;
			if (gao(pm)) {
				pl = pm;
			} else {
				pr = pm;
			}
		}
		printf("Case #%d: %d\n", caseNum, pl);
	}
	return 0;
}
