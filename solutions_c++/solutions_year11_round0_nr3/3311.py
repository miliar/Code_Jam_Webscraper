#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

int a[1000];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	scanf("%d", &T);
	forn(t, T) {
		int n;
		scanf("%d", &n);
		forn(i, n) scanf("%d", &a[i]);	
		
		int best_answer = -1;
		for (int mask = 1; mask < (1 << n) - 1; mask++) {
			int x = 0, y = 0, z = 0;
			forn(i, n) {
				if (mask & (1 << i)) {
					x = x ^ a[i];
					z += a[i];
				} else {
					y = y ^ a[i];
				}
			}
			if (x == y) {
				best_answer = max(best_answer, z);
			}
		}
		
		printf("Case #%d: ", t + 1);
		if (best_answer == -1) {
			printf("NO\n");
		} else {
			printf("%d\n", best_answer);
		}
	}

	return 0;
}
