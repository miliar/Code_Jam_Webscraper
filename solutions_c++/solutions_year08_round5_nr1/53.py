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

#define MAXN 6010

char grid[MAXN*2+1][MAXN*2+1];

char s[100000];
int dirs[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		memset(grid, 0, sizeof(grid));
		int l;
		scanf("%d", &l);
		int px = MAXN, py = MAXN, d = 0;
		grid[px][py] = 1;
//		printf("starting at %d %d\n", px, py);
		while(l--) {
			int cnt;
			scanf("%s %d", s, &cnt);
			while(cnt--) {
				for (int i=0; s[i]; ++i) {
					if (s[i] == 'F') {
						px += dirs[d][0];
						py += dirs[d][1];
						grid[px][py] = 1;
						px += dirs[d][0];
						py += dirs[d][1];
						grid[px][py] = 1;
					}
					else if (s[i] == 'L') {
						d = (d+3)%4;
					}
					else if (s[i] == 'R') {
						d = (d+1)%4;
					}
					else assert(0);
				}
			}
		}
//		printf("ending at %d %d\n", px, py);
		int res = 0;
		for (int i=1; i<MAXN*2; i+=2) {
			bool first = true;
			bool within = false;
			int cnt = 0, lastj = MAXN*2+1;
			for (int j=0; j<=MAXN*2; j++) {
				if (grid[i][j] == 1) {
					if (within) {
						within = false;
						lastj = j;
					}
					else {
//						if (!first) printf("here1 at %d %d with %d\n", i, j, cnt);
						res += cnt;
						within = true;
						cnt = 0;
					}
					first = false;
				}
				else if (!within && !first) {
					if (j%2 && !grid[i][j]) {
						++cnt;
						grid[i][j] = 2;
					}
				}
			}
			for (lastj++; lastj<=MAXN*2; lastj+=2) {
				assert(grid[i][lastj] == 2);
				grid[i][lastj] = 0;
			}
			assert(!within);
		}
		for (int i=1; i<MAXN*2; i+=2) {
			bool first = true;
			bool within = false;
			int cnt = 0;
			for (int j=0; j<=MAXN*2; j++) {
				if (grid[j][i] == 1) {
					if (within) {
						within = false;
					}
					else {
//						if (!first) printf("here2 at %d %d with %d\n", j, i, cnt);
						within = true;
						res += cnt;
						cnt = 0;
					}
					first = false;
				}
				else if (!within && !first && (j%2)) {
					if (!grid[j][i]) {
						++cnt;
						grid[j][i] = 2;
					}
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
