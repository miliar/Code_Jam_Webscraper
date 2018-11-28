#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char S0[] = "welcome to code jam";
const char LenS0 = 19;

int T, N;
int Dp[505][20];
char S[505];

int main(void){
	int tc = 1;
	for (scanf("%d", &T); T; T --){
		fgets(S, 505, stdin);
		N = strlen(S);
		if (N == 1){
			T ++;
			continue;
		}
		N --;
		S[N] = 0;
		memset(Dp, 0, sizeof(Dp));
		for (int i = 0; i < N; i ++) Dp[i][0] = 1;
		for (int i = 0; i < N; i ++){
			for (int j = 0; j <= LenS0; j ++){
				if (j < LenS0)
					if (S[i] == S0[j]) Dp[i + 1][j + 1] = (Dp[i + 1][j + 1] + Dp[i][j]) % 10000;
				if (j) Dp[i + 1][j] = (Dp[i + 1][j] + Dp[i][j]) % 10000;
			}
		}
		printf("Case #%d: %04d\n", tc ++, Dp[N][LenS0]);
	}
	return 0;
}
