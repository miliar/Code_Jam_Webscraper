#include <stdio.h>
#include <algorithm>
using namespace std;

int S, N, p;
int t[120];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int cases, a;
	int be, ed, ans;
	scanf("%d", &cases);
	for (int o = 1; o <= cases; o++) {
		scanf("%d%d%d", &N, &S, &p);
		ans = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &a);
			be = (0 > a / 3 - 2)? 0: a / 3 - 2;
			ed = (a / 3 + 2 > 10)? 10: a / 3 + 2;
			int j, k, t;
			bool ok1 = 0, ok = 0;
            for (j = be; j <= ed; j++) {
				if (ok) break;
				for (k = be; k <=  ed; k++) {
					if (ok) break;
                    for (t = be; t <= ed; t++) {
						if (ok) break;
						if (j + k + t == a && max(j, max(k, t)) >=  p) {
							 if (max(j, max(k, t)) - min(j, min(k, t)) < 2) ok = 1;
							 else if  (max(j, max(k, t)) - min(j, min(k, t)) == 2) ok1 = 1;
						}
					}
				}
			}
			if (ok || ok1) {                    
                ans++;
				if (!ok) S--;
			}
        }
		if (S < 0) ans += S;
		printf("Case #%d: %d\n", o, ans);
	}
	return 0;
}
