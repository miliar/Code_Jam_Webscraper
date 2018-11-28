#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char frase[] = "welcome to code jam";
int PD[600][50];
char s[600];

int main() {
	int _42 = 1, T;
	int Tam = strlen(frase);
	gets(s);
	sscanf(s, " %d", &T);
	while (T--) {
		gets(s);
		int N = strlen(s);
		memset(PD, 0, sizeof(PD));
		for (int i=0;i<N;i++) {
			if (s[i] == 'm') {
				PD[i][Tam - 1] = 1;
			}
		}
		for (int i = N-2;i >= 0;i--) {
			for (int j=0;j<Tam-1;j++) {
				if (s[i] == frase[j]) {
					for (int k=i+1;k<N;k++) {
						PD[i][j] += PD[k][j+1];
					}
				}
				PD[i][j] = PD[i][j] % 10000;
			}
		}
		int ans = 0;
		for (int i=0;i<N;i++) {
			ans += PD[i][0];
			ans = ans % 10000;
		}
		printf("Case #%d: %04d\n", _42++, ans);
	}
	return 0;
}
