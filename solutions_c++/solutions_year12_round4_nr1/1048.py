#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxl 10100

struct node {
	int d, l;
}
E[maxl];

int f[maxl], n, D;

bool cmp(node i, node j) {
	return i.d < j.d;
}

bool clac() {
	sort(E + 1, E + 1 + n, cmp);
	if(E[1].l < E[1].d) return 0;
	memset(f, 0x80, sizeof f);
	f[1] = 2 * E[1].d;

	for(int i=2; i<=n; ++i) {
		for(int j=1; j<i; ++j) {
			if(f[j] < E[i].d) continue;

			int x = min(E[i].d - E[j].d, E[i].l);
			int tmp = E[i].d + x;

			f[i] = max(f[i], tmp);
		}
	}

	for(int i=1; i<=n; ++i) if(f[i] >= D) return 1;
	return 0;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d", &n);
		for(int i=1; i<=n; ++i) {
			scanf("%d%d", &E[i].d, &E[i].l);
		}
		scanf("%d", &D);
		printf("Case #%d: ", q);
		puts(clac() ? "YES" : "NO");
	}
	return 0;
}

