#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

char c[200]; int p[200];

int main() {
	int n;
	scanf("%d", &n);
	for (int ct = 1; ct <= n; ct++) {
		int t; scanf("%d", &t);
		for (int i = 0; i < t; i++) scanf(" %c %d", &c[i], &p[i]);
		int to = 0, tb = 0, po = 1, pb = 1;
		if (c[0] == 'O') {
			to = abs(po-p[0]) + 1;
			po = p[0];
		} else {
			tb = abs(pb-p[0]) + 1;
			pb = p[0];
		}
		for (int i = 1; i < t; i++) {
			if (c[i] == 'O') {
				if (to + abs(po-p[i]) + 1 <= tb)
					to = tb + 1;
				else
					to += abs(po-p[i]) + 1;
				po = p[i];
			} else {
				if (tb + abs(pb-p[i]) + 1 <= to)
					tb = to + 1;
				else
					tb += abs(pb-p[i]) + 1;
				pb = p[i];
			}
		}
		printf("Case #%d: %d\n", ct, max(to, tb));
	}
	return 0;
}
