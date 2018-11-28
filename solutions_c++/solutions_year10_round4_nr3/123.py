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

char simulate[2][128][128];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int r, x1, y1, x2, y2;
		scanf("%d", &r);
		memset(simulate[0], 0, sizeof(simulate[0]));
		for (int i=0; i<r; ++i) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int ii=x1; ii<=x2; ++ii)
				for (int jj=y1; jj<=y2; ++jj)
					simulate[0][ii][jj] = 1;
		}
		int sec = 0;
		int cur = 0, next = 1;
		while(true) {
			++sec;
			int stop = 1;
			for (int i=1; i<128; ++i)
				for (int j=1; j<128; ++j) {
					simulate[next][i][j] = simulate[cur][i][j] && (simulate[cur][i][j-1] || simulate[cur][i-1][j])
										|| simulate[cur][i-1][j] && simulate[cur][i][j-1];
					if (simulate[next][i][j])
						stop = 0;
				}
			if (stop)
				break;
			swap(cur, next);
		}
		printf("%d\n", sec);
	}
	return 0;
}
