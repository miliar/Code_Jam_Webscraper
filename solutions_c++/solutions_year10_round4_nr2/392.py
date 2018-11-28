#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <memory>
#include <vector>
#include <string>
#include <set>
#include <map>

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long int64;

const int MNOGO = 0x3fffffff;

int T;

const int MAXN = 1500, MAXP = 16;

int a[MAXN*2][MAXP];
int m[MAXN*2], pr[MAXN*2];
             
int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		int p;
		scanf("%d\n", &p);
		int n = (1 << p);

		for (int i = 0; i <= 2*n; i++) {
			for (int j = 0; j <= p; j++) {
				a[i][j] = MNOGO;
			}
		}

		for (int i = n-1; i >= 0; i--) {
			scanf("%d", &m[i]);
			a[n + i][m[i]] = 0;
		}

		for (int i = n-1; i >= 1; i--) {
			scanf("%d", &pr[i]);
		}

		for (int i = n-1; i >= 1; i--) {
			int l = 2*i, r = 2*i+1;

			for (int j1 = 0; j1 <= p; j1++) {
				if (a[l][j1] == MNOGO) continue;
				for (int j2 = 0; j2 <= p; j2++) {
					if (a[r][j2] == MNOGO) continue;

					int j = min(j1, j2);

					// watch
					if (a[i][j] > a[l][j1] + a[r][j2] + pr[i]) {
						a[i][j] = a[l][j1] + a[r][j2] + pr[i];
					}

					if (j >= 0 && a[i][j-1] > a[l][j1] + a[r][j2]) {
						a[i][j-1] = a[l][j1] + a[r][j2];
					}
				}
			}
		}

		int answer = MNOGO;
		for (int j = 0; j <= p; j++) {
			answer = min(answer, a[1][j]);
		}

		printf("%d", answer);

		printf("\n");
	}

	return 0;
}

