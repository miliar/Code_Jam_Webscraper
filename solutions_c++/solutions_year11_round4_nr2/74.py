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

int w[600][600]; // actual 0-indexed grid
int cw[600][600]; // sum of w of everything strictly up-left
int cxw[600][600];
int cyw[600][600];

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		// clean c arrays
		for (int i = 0; i < 600; i++) {
			for (int j = 0; j < 600; j++) {
				cw[i][j] = cxw[i][j] = cyw[i][j] = 0;
			}
		}
		
		int R, C, D;
		scanf("%d%d%d ",&R,&C,&D);
		int w[R][C];
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				char c;
				scanf("%c",&c);
				w[i][j] = c-'0';
				cw[i+1][j+1] = cw[i+1][j] + cw[i][j+1] + w[i][j] - cw[i][j];
				cxw[i+1][j+1] = cxw[i+1][j] + cxw[i][j+1] + i*w[i][j] - cxw[i][j];
				cyw[i+1][j+1] = cyw[i+1][j] + cyw[i][j+1] + j*w[i][j] - cyw[i][j];
			}
			scanf(" ");
		}

		int best = -1;
		for (int K = min(R,C); K >= 3; K--) {
			bool possible=0;
			for (int i = 0; i+K <= R; i++) {
			for (int j = 0; j+K <= C; j++) {
				long long xsum = cxw[i+K][j+K] - cxw[i+K][j] - cxw[i][j+K] + cxw[i][j];
				xsum -= i*(w[i][j]+w[i][j+K-1]);
				xsum -= (i+K-1)*(w[i+K-1][j]+w[i+K-1][j+K-1]);
				long long ysum = cyw[i+K][j+K] - cyw[i+K][j] - cyw[i][j+K] + cyw[i][j];
				ysum -= j*(w[i][j]+w[i+K-1][j]);
				ysum -= (j+K-1)*(w[i][j+K-1]+w[i+K-1][j+K-1]);

				long long wsum = cw[i+K][j+K] - cw[i+K][j] - cw[i][j+K] + cw[i][j];
				wsum -= w[i][j] + w[i][j+K-1] + w[i+K-1][j] + w[i+K-1][j+K-1];

				if (xsum*2 != wsum*(2*i+K-1)) continue;
				if (ysum*2 != wsum*(2*j+K-1)) continue;
				possible=1;
			}
			}
			if (possible) {
				best = K;
				break;
			}
		}
		
		if (best == -1) {
			printf("Case #%d: IMPOSSIBLE\n",test);
		} else {
			printf("Case #%d: %d\n",test,best);
		}
	}
}
