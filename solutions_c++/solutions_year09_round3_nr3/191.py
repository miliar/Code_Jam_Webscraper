#include <stdio.h>

int rlist[12000] = {0};


int main() {
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++) {
		int mic[110][110] = {0};
		int ans = 0;

		int P, Q;
		scanf("%d %d", &P, &Q);
		for (int i = 1; i <= Q; i++)
			scanf("%d", &rlist[i]);
		rlist[Q + 1] = P + 1;

		for (int i = 1; i <= Q; i++) mic[i][i] = rlist[i + 1] - rlist[i - 1] - 2;
		
		//for (int a = 1; a <= Q; a++) { for (int b = 1; b <= Q; b++) printf("%d ", mic[a][b]); printf("\n"); } printf("\n\n");
		
		for (int k = 2; k <= Q; k++) {
			for (int i = 1; i <= Q - k + 1; i++) {
				int j = i + k - 1;
				int min = -1;
				for (int p = i; p <= j; p++) {
					int cost = mic[i][p - 1] + mic[p + 1][j];
					if (min == -1 || cost < min) min = cost;
				}
				mic[i][j] = min + rlist[j + 1] - rlist[i - 1] - 2;
			}
			
			//for (int a = 1; a <= Q; a++) { for (int b = 1; b <= Q; b++) printf("%d ", mic[a][b]); printf("\n"); } printf("\n\n");
		}

		printf("Case #%d: %d\n", z, mic[1][Q]);
	}
	return 0;
}
