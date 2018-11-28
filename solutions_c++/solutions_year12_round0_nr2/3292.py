#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int f[101];

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		int n, s, p;
		memset(f, -1, sizeof(f));
		f[0] = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; i++) {
			int x;
			int maxi1, maxi2;
			scanf("%d", &x);
						if (x % 3 == 0) {
				maxi1 = x / 3;
				maxi2 = x / 3 + 1;
			} else {
				maxi1 = x / 3 + 1;
				if (x % 3 == 1) {
					maxi2 = x / 3 + 1;
				} else {
					maxi2 = x / 3 + 2;
				}
			}
			for (int j = s; j >= 0; j--) {
				if (f[j] >= 0 && maxi1 >= p) {
					f[j]++;
				}
				if (j > 0 && f[j - 1] >= 0 && x >= 2) {
					int k;
					if (maxi2 >= p)
						k = 1;
					else
						k = 0;
					f[j] = max(f[j], f[j - 1] + k);
				}
			}
		}
		printf("Case #%d: %d\n", t, f[s]);
	}
}