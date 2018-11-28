// Adrian Kügel
#include <stdio.h>
#include <string.h>
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
typedef pair<short, int> PCI;

char diam[300][301];

int main() {
	int n, tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d", &n);
		gets(diam[0]);
		memset(diam, 0, sizeof(diam));
		for (int i=0; i<2*n-1; ++i) {
			gets(diam[i]);
			for (int j=0; j<2*n-1; ++j)
				if (diam[i][j] == ' ')
					diam[i][j] = 0;
		}
		int best = INT_MAX;
		for (int mx=-10; mx<2*n+10; ++mx)
			for (int my=-10; my<2*n+10; ++my) {
				bool valid = true;
				int dist = 0;
				for (int i=0; i<2*n-1 && valid; ++i)
					for (int j=0; j<2*n-1 && valid; ++j) {
						if (diam[i][j] == 0)
							continue;
						// calculate positions which should match
						// first mirror at x
						int tx = i + 2 * (mx - i);
						if (tx >= 0 && tx < 2*n-1 && diam[tx][j] && diam[tx][j] != diam[i][j]) {
							valid = false;
							break;
						}
						int ty = j + 2 * (my - j);
						if (ty >= 0 && ty < 2*n-1 && diam[i][ty] && diam[i][ty] != diam[i][j]) {
							valid = false;
							break;
						}
						int t = 1 + abs(i-mx) + abs(j-my);
						dist = max(dist, t);
					}
				if (valid)
					best = min(best, dist*dist - n * n);
			}
		printf("%d\n", best);
	}
	return 0;
}
