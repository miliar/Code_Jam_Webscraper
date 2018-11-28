#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; ++t) {
		printf("Case #%d: ", t);

		int n;
		scanf("%d", &n);
		int d[n], l[n];
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", &d[i], &l[i]);
		}
		int D;
		scanf("%d", &D);

		int hi[n];
		memset(hi, -1, sizeof(hi));
		hi[0] = d[0];

		for (int i = 0; i < n; ++i) {
			if (d[i] + hi[i] >= D) {
				printf("YES\n");
				goto end;
			}
			int j = i+1;
			while (d[i] + hi[i] >= d[j]) {
				hi[j] = max(hi[j], d[j]-d[i]);
				hi[j] = min(hi[j], l[j]);
				++j;
			}
		}

		printf("NO\n");
		end: ;
	}
}
