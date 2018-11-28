#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i != (b); ++i)

int price[20][30];
int cross[20][20];

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		int N, K;
		scanf(" %d %d", &N, &K);
		for (int i=0; i < N; i++) {
			for (int j=0; j < K; j++) {
				scanf(" %d", &price[i][j]);
			}
		}

		memset(cross, 0, sizeof(cross));
		for (int i=0; i < N; i++) {
			for (int j=i+1; j < N; j++) {
				bool crossed = false;
				for (int k=0; k+1 < K; k++) {
					if (price[i][k] == price[j][k]) crossed = true;
					else if (price[i][k+1] == price[j][k+1]) crossed = true;
					else if (price[i][k] > price[j][k] && price[i][k+1] < price[j][k+1]) crossed = true;
					else if (price[i][k] < price[j][k] && price[i][k+1] > price[j][k+1]) crossed = true;
				}
				if (crossed) cross[i][j] = cross[j][i] = 1;
			}
		}

		int ans = 1;
		FOR(i,0,N) {
			for (int b=1; b < (1<<N); b++) {
				int adj = b;
				FOR(j,0,N) if ((1 << j) & b) {
					int tmp = 0x0;
					FOR(k,0,N) if (j == k || cross[j][k]) tmp |= (1 << k);
					adj &= tmp;
				}
				if (adj == b) ans = max(ans, __builtin_popcount(adj));
			}
		}
		printf("Case #%d: %d\n", _42, ans);
	}

	return 0;
}
