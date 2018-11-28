#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

bool powered[35];
bool state[35];

int main() {
	FILE* fin = fopen("A.in", "r");
	FILE* fout = fopen("A.out", "w");

	int T;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; ++t) {
		int N, K;
		fscanf(fin, "%d %d", &N, &K);
		memset(powered, 0, sizeof(powered));
		memset(state, 0, sizeof(state));
		powered[0] = 1;
//		printf("Test %d:\n", t);
		for(int k = 0; k < K; ++k) {
			for(int n = 0; n < N; ++n) {
				if(powered[n]) {
					state[n] ^= 1;
				}
			}
			if(state[0])
			for(int n = 1; n < N; ++n) {
				if(state[n-1] && powered[n-1]) powered[n] = 1;
				else break;
			}
			else
			for(int n = 1; n < N; ++n) {
				powered[n] = 0;
			}
//			printf("p: ");
//			for(int n = 0; n < N; ++n) printf("%d ", powered[n]);
//			printf("\ns: ");
//			for(int n = 0; n < N; ++n) printf("%d ", state[n]);
//			printf("\n\n");
		}
		if(powered[N-1] && state[N-1]) {
			fprintf(fout, "Case #%d: ON\n", t);
			printf("Case #%d: ON\n", t);
		}
		else {
			fprintf(fout, "Case #%d: OFF\n", t);
			printf("Case #%d: OFF\n", t);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

