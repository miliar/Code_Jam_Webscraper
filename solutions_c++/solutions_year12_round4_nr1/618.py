#include <iostream>
#include <cstdio>
using namespace std;
const int inf = 2000000000;
int f[100000], d[100000], l[100000];
bool flag;
int n, tp, tmp;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; ++tt) {
		scanf("%d", &n);
		for (int i = 1; i <= n ; ++i)
			scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &d[n + 1]);
		for (int i = 1; i <= n ; ++i) 
			l[i] = min(l[i], d[i]);
		for (int i = n; i >= 1; --i) {
			tmp = l[i] + 1;
			if (d[n + 1] - d[i] < tmp) tmp = d[n + 1] - d[i];
			for (int j = i + 1; j <= n ; ++j) {
				tp = d[j] - d[i];
				if (f[j] == -1 || tp > l[i] || tp < f[j]) continue;
				if (tp < tmp ) tmp = tp;
				break;
			}
			if (tmp > l[i]) f[i] = -1; else f[i] = tmp;
		}
		if (f[1] != -1) printf("Case #%d: YES\n", tt);
		else printf("Case #%d: NO\n", tt);
	}
	return 0;
}