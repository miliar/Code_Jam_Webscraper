#include <stdio.h>
#include <string.h>

int main() {
	int step, inf = 1<<30;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &step);
	for(int round = 0; round < step; round++) {
		int S, Q;
		int mic[100][1001], T[100], P[100];
		char Sl[100][101], Ql[1000][101];
		memset(mic, 0, sizeof mic);
		memset(P, 0, sizeof P);
		scanf("%d\n", &S);
		for(int i = 0; i < S; i++) gets(Sl[i]);
		scanf("%d\n", &Q);
		for(int i = 0; i < Q; i++) gets(Ql[i]);
		for(int s = 1; s <= Q; s++) {
			for(int i = 0; i < S; i++) {
				if( strcmp(Sl[i], Ql[s-1]) == 0 ) {
					mic[i][s] = inf;
					continue;
				}
				int d = inf - 10;
				for(int j = 0; j < S; j++) {
					int c = i == j ? 0 : 1;
					if( c + mic[j][s-1] < d ) {
						d = c + mic[j][s-1];
					}
				}
				mic[i][s] = d;
				//printf("%d %d %d\n", d, i, s);
			}
		}
		int min = inf;
		for(int i = 0; i < S; i++) if( mic[i][Q] < min ) min = mic[i][Q];
		printf("Case #%d: %d\n", round + 1, min);
	}
	//while(1);
	return 0;
}
