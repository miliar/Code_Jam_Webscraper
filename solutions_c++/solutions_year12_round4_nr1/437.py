#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <deque>

using namespace std;

#define maxn (100000)

int d[maxn], l[maxn];
int n, m;

void work() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &m);
	
	l[0] = d[0];
	for (int i = 1, k = 0; i < n; ++i) {
		while (k < i && d[k] + l[k] < d[i]) k++;
		if (k >= i) l[i] = -2000000000;
		else l[i] = min(l[i], d[i] - d[k]);
	}
	
	bool flag = false;
	for (int i = 0; i < n; ++i) if (d[i] + l[i] >= m) flag = true;
	
	if (flag) puts("YES"); else puts("NO");
}

int main() {
	int T; scanf("%d", &T);
	
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}
