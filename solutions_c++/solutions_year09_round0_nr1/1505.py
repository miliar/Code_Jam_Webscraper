#include <stdio.h>

int L, D, N, DM[5000][15], SM[15]; char S[1000];

int main() {
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++) {
		scanf("%s", S);
		for (int j = 0; j < L; j++)
		 DM[i][j] = 1L << (S[j] - 'a');
	}
	for (int i = 0; i < N; i++) {
		scanf("%s", S);
		for (int j = 0, p = 0; S[j]; j++, p++) {
			SM[p] = 0;
			if (S[j] == '(') {
				for (j++; S[j] != ')'; j++)
				 SM[p] |= 1L << (S[j] - 'a');
			} else {
				SM[p] |= 1L << (S[j] - 'a');
			}
		}
		int succ = 0;
		for (int j = 0; j < D; j++) {
			int failed = 0;
			for (int k = 0; k < L; k++)
			 if (!(SM[k] & DM[j][k])) { failed = 1; break; }
			if (!failed) succ++;
		}
		printf("Case #%d: %d\n", i + 1, succ);
	}
	return 0;
}
