#include <cstdio>
#include <climits>
#include <algorithm>

using namespace std;

int d[10000];
int l[10000];
int r[10000];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d%d", d + i, l + i);
		}
		
		r[0] = d[0];
		for (int i = 1; i < n; i++) {
			r[i] = INT_MIN;
			for (int j = 0; j < i; j++) {
				if (d[i] - d[j] <= r[j]) {
					r[i] = max(r[i], d[i] - d[j]);
				}
			}
			r[i] = min(r[i], l[i]);
			//printf("%d\n", r[i]);
		}
		
		int D;
		scanf("%d", &D);
		
		bool doseze = false;
		for (int i = 0; i < n; i++) {
			if (D - d[i] <= r[i]) {
				doseze = true;
			}
		}
		
		if (doseze) {
			printf("Case #%d: YES\n", t + 1);
		} else {
			printf("Case #%d: NO\n", t + 1);
		}
	}
}
