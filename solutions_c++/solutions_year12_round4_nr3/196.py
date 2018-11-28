#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long lld;

const int maxn=2020;

bool fail = false;
vector<lld> from[maxn];
lld l[maxn];
int before[maxn];

void expand(int at, int last) {
	if (fail) return;
	int lim = 0;
	lld x1, y1, x2, y2;
	x1 = at-last;
	y1 = l[at]-l[last];
	for (int i=0; i<from[at].size(); i++) {
		int to = from[at][i];
		if (to < before[at]) {
			fail = true;
			break;
		}
		lld low = 0, high = 1000000001;
		x2 = to-at;
		while (high-low > 1) {
			lld mid = (high+low)/2;
			y2 = mid - l[at];
			if (x1*y2 - x2*y1 < lim) {
				high = mid;
			}
			else {
				low = mid;
			}
		}
		y2 = low - l[at];
		if (x1*y2-x2*y1 >= lim) {
			// good
			l[to] = max(min(y2+l[at], 1000000000ll), 0ll);
			lim = 1;
			x1 = to-at;
			y1 = l[to]-l[at];
			if (i) {
				before[to] = from[at][i-1];
			}
			else {
				before[to] = before[at];
			}
			expand(to, at);
		}
		else {
			fail = true;
		}
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=1; ti<=t; ti++) {
		for (int i=0; i<maxn; i++) {
			from[i].clear();
		}
		fail = false;
		int n;
		scanf("%d", &n);
		l[n+1] = -2000000000;
		for (int i=1; i<n; i++) {
			int to;
			scanf("%d", &to);
			from[to].push_back(i);
		}
		l[n] = 1000000000/2;
		before[n] = 0;
		expand(n, n+1);
		printf("Case #%d: ", ti);
		if (!fail) {
			for (int i=1; i<=n; i++) {
				printf("%lld%s", l[i], (i!=(n))?" ":"\n");
			}
		}
		else {
			printf("Impossible\n");
		}
	}
	return 0;
}