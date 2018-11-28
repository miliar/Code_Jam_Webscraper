#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

const int MaxN = 11111;

int n;
pii p[MaxN];
int f[MaxN];

void work() {
	memset(f, 0, sizeof(f));

	scanf("%d", &n);
	for (int i = 0; i < n; ++ i) {
		scanf("%d%d", &p[i].first, &p[i].second);
	}
	scanf("%d", &p[n].first);
	p[n].second = 0x7FFFFFFF;

	f[0] = p[0].second >= p[0].first ? p[0].first : 0;
	for (int i = 0; i < n; ++ i) {
		for (int j = i + 1; j <= n && p[i].first + f[i] >= p[j].first; ++ j) {
			f[j] = max(f[j], min(p[j].second, p[j].first - p[i].first));
		}
	}

	if (f[n] > 0) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
}

int main() {
	int tn;
	scanf("%d", &tn);
	for (int t = 1; t <= tn; ++ t) {
		printf("Case #%d: ", t);
		work();
	}
	return 0;
}
