#include <cstdio>
#include <memory.h>

int Tests, R, N, K, G[100], Total, Now, Once, Start;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases) {
		memset(G, 0, sizeof(G));
		Total = 0; Now = Start = 0;
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; ++ i) scanf("%d", &G[i]);
		for (int i = 0; i < R; ++ i) {
			Once = 0; Start = Now;
			if (G[Now] <= K) {
				Once = G[Now], ++ Now;
				if (Now == N) Now = 0;
				while (G[Now] + Once <= K && Now != Start) {
					Once += G[Now];
					++ Now;
					if (Now == N) Now = 0;
				}
				Total += Once;
			}
		}
		printf("Case #%d: %d\n", Cases, Total);
	}
}
