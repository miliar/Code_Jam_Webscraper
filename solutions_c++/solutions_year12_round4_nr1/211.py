#include <cstdio>
#include <map>

using namespace std;

const int maxn = 10100, inf = 1234567890;

int cache[maxn];
int d[maxn], l[maxn], t, n, tar;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		scanf("%d", &n);
		for (int i=0; i<n; i++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &tar);
		d[n] = tar;
		l[n] = 1;
		cache[n] = 0;
		bool good = false;
		for (int i=n-1; i>=0; i--) {
			cache[i] = inf;
			for (int j=n; j>i; j--) {
				if (d[j]-d[i] <= l[i] && d[j]-d[i] >= cache[j]) {
					cache[i] = d[j]-d[i];
				}
			}
			//printf("at %d is the shortest: %d\n", i, cache[i]);
		}
		printf("Case #%d: ", ti+1);
		if (cache[0] <= d[0]) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	return 0;
}