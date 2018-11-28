#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

bool occ[150][150];

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		int R; scanf("%d",&R);
		for (int i = 0; i < 150; i++) {
		for (int j = 0; j < 150; j++) {
			occ[i][j] = 0;
		}
		}
		bool anything = 0;
		int ans=0;
		for (int i = 0; i < R; i++) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int x = x1; x <= x2; x++) {
			for (int y = y1; y <= y2; y++) {
				occ[x][y] = 1;
				anything = 1;
			}
			}
		}
		while (anything) {
			anything = 0;
			ans++;
			for (int y = 130; y >= 1; y--) {
			for (int x = 130; x >= 1; x--) {
				if (occ[x-1][y] && occ[x][y-1]) {
					occ[x][y] = 1;
				}
				if (!occ[x-1][y] && !occ[x][y-1]) {
					occ[x][y] = 0;
				}
				if (occ[x][y]) anything = 1;
			}
			}
		}
		
		printf("Case #%d: %d\n",test,ans);
	}
}
