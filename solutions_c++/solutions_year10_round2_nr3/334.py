#include <stdio.h>
#include <set>
using namespace std;
int i, j, k, t, tt, n, r;
int q[500];

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d", &n);

		n--;

		int cnt = 0;
		for (r = 1; r < (1 << n); r++) {
			k = 0;
			for (j = 0; j < n; j++) {
				if ((1<<j) & r) {
					q[k++] = j + 2;
				}
			}
			j = k;
			bool ok = true;
			if (q[k-1] != n+1) {ok = false; j = 1;}
			while (j != 1) {
				for (i = 0; i < k; i++) if (q[i] == j) {
					j = i + 1; break;
				}
				if (i == k) {
					ok = false; break;
				}
			}
			if (ok) {
//				for (i = 0; i < k; i++) printf("%d ", q[i]);printf("\n");
				cnt++;
			}
		}

		printf("%d\n", cnt % 100003);
	}
	return 0;
}

