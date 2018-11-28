#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int i,j,k,cases,_case;
int M, V, n;
int type[100000];
int chable[100000];
vector<int> p;
int val[100000];
int cnt, best;

int main() {
	scanf("%d", &cases);
	for (_case = 1; _case <= cases; _case++) {
		printf("Case #%d: ", _case);

		scanf("%d%d", &M, &V);
		p.clear();
		for (i = 0; i < (M - 1) / 2; i++) {
			scanf("%d%d", &type[i], &chable[i]);
			if (chable[i] == 1) p.push_back(i);
		}

		for (i = 0; i < (M + 1) / 2; i++) {
			scanf("%d", &val[i + (M - 1) / 2]);
		}

		n = p.size();
		best = 12345678;
		for (i = 0; i < (1 << n); i++) {
			cnt = 0;
			for (j = 0; j < n; j++) {
				if (i & (1 << j)) {
					type[p[j]] = 1 - type[p[j]];
					cnt++;
				}
			}

			for (j = (M - 1) / 2 - 1; j >= 0; j--) {
				if (type[j] == 1) {
					val[j] = (val[(j + 1) * 2 - 1] && val[(j + 1) * 2]);
				} else {
					val[j] = (val[(j + 1) * 2 - 1] || val[(j + 1) * 2]);
				}
			}

			if (val[0] == V) {
				if (best == -1 || cnt < best) best = cnt;
			}

			for (j = 0; j < n; j++) {
				if (i & (1 << j)) type[p[j]] = 1 - type[p[j]];
			}
		}
		
		if (best == 12345678) printf("IMPOSSIBLE");
		else printf("%d", best);
		printf("\n");
	}
	return 0;
}

