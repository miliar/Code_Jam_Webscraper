#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>

using namespace std;

#define maxn (200000)
#define A first
#define B second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef pair<int, int> PII;

double f[maxn], g[maxn];
int n, m;
double ans;

void work() {
	memset(f, 0, sizeof(f));
	memset(g, 0, sizeof(g));

	scanf("%d%d", &m, &n);
	for (int i = 1; i <= m; ++i) scanf("%lf", &g[i]);
	f[0] = 1.; ans = (double) (n + 2);
	for (int i = 1; i <= m; ++i) {
		f[i] = f[i - 1] * g[i];
		ans = min(ans, f[i] * ((double) (m - i + n - i + 1)) + (1. - f[i]) * ((double) (m - i + n - i + 1 + n + 1)));
	}

	printf("%.10f", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
		puts("");
	}

	return 0;
}
