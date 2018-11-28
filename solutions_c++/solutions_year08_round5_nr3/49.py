// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

#define MAXN 10

char grid[MAXN][MAXN+1];

int best[2][1<<MAXN];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		int n, m;
		printf("Case #%d: ", scen);
		scanf("%d %d",&n,&m);
		memset(best, -1, sizeof(best));
		int cur = 0, next = 1;
		best[0][0] = 0;
		int res = 0;
		for (int i=0; i<n; ++i) {
			scanf("%s", &grid[i]);
			memset(best[next], -1, sizeof(best[next]));
			for (int ii=0; ii<(1<<m); ++ii) {
				if (best[cur][ii] < 0)
					continue;
				for (int mask=0; mask<(1<<m); ++mask) {
					if (mask & ii)
						continue;
					bool valid = true;
					int nmask = 0, cnt = 0;
					for (int j=0; j<m; ++j) {
						if (mask & (1<<j)) {
							if (grid[i][j] == 'x') {
								valid = false;
								break;
							}
							++cnt;
							if (j && (mask&(1<<(j-1)))) {
								valid = false;
								break;
							}
							if (j)
								nmask |= (1<<(j-1));
							if (j+1 < m)
								nmask |= (1<<(j+1));
						}
					}
					if (valid) {
						best[next][nmask] = max(best[next][nmask], best[cur][ii] + cnt);
						res = max(best[next][nmask], res);
					}
				}
			}
			cur = next;
			next = !cur;
		}
		printf("%d\n", res);
	}
	return 0;
}
