#include <cstdio>
#include <string>
#include <cstring>
#include <set>

using namespace std;

int now[100];
int v[100];

int dd()
{
	int n, k, b, t;
	scanf("%d %d %d %d", &n, &k, &b, &t);
	for (int i = 0; i < n; ++i) {
		scanf("%d", now + i);
	}
	for (int i = 0; i < n; ++i) {
		scanf("%d", v + i);
	}
	if (k == 0) return 0;
	int cur = 0;
	int ret = 0;
	int done = 0;
	for (int i = n - 1; i >= 0; --i) {
		int ddd = v[i] * t;
		if (ddd >= b - now[i]) {
			++done;
			ret += cur;
			if (done == k) return ret;
		}
		else {
			++cur;
		}
	}
	return -1;
}

int main()
{
	freopen("BB.in", "r", stdin);
	freopen("BB.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int res = dd();
		if (res != -1) printf("Case #%d: %d\n", i, res);
		else printf("Case #%d: IMPOSSIBLE\n", i);
	}
	return 0;
}