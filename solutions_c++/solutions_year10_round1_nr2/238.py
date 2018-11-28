#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))

int PD[110][300];
int val[110];

int main() {
	int T, _42=0;
	scanf(" %d", &T);
	while (T--) {
		int D, I, M, N;
		scanf(" %d %d %d %d", &D, &I, &M, &N);

		for (int i=1; i <= N; i++) scanf(" %d", &val[i]);

		memset(PD, 0, sizeof(PD));
		for (int i=1; i <= N; i++) {
			for (int j=0; j <= 255; j++) {
				PD[i][j] = PD[i-1][j] + D;

				int change = abs(j - val[i]);
				if (M) {
					for (int k=0; k <= 255; k++) {
						int teto = (abs(j-k) + M - 1) / M;
						int ins = max(0, (teto-1) * I);
						PRINT("k=%d teto=%d ins=%d change=%d PD[i-1][k]=%d\n", k, teto, ins, change, PD[i-1][k]);
						PD[i][j] = min(PD[i][j], PD[i-1][k] + ins + change);
					}
				}
				else {
					PD[i][j] = min(PD[i][j], PD[i-1][j] + change);
				}
				PRINT("PD[%d][%d] = %d\n", i, j, PD[i][j]);
			}
		}

		int best = PD[N][0];
		for (int j=0; j <= 255; j++) {
			PRINT("PD[N][%d] = %d\n", j, PD[N][j]);
			best = min(best, PD[N][j]);
		}
		printf("Case #%d: %d\n", ++_42, best);
	}

	return 0;
}
