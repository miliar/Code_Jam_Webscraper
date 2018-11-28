#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#define min(a, b) ((a) < (b) ? (a) : (b))
using namespace std;

const int N = 10005;
int T;
int d[N], l[N];
int f[N];
int n, m;

void work()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &d[i], &l[i]);
		//printf("%d %d a\n", d[i], l[i]);
	}
	memset(f, 0, sizeof(f));
	scanf("%d", &m);
	f[0] = d[0];
	bool can = false;
	for (int i = 0; i < n; ++i) {
		l[i] = min(l[i], d[i]);
		for (int j = i + 1; j < n; ++j) {
			if (d[j] - d[i] <= f[i]) {
				f[j] = max(f[j], d[j] - d[i]);
				f[j] = min(f[j], l[j]);
			}
		}
		if (m - d[i] <= f[i]) { can = true; break; }
	}
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	if (can) printf("YES\n"); else printf("NO\n");
}

int main()
{
	scanf("%d", &T);
	while (T--) work();
}