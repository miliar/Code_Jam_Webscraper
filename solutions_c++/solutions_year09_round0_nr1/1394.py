#include <stdlib.h>
#include <stdio.h>
#include <string.h>

bool poss[20][30];
char s[2000];
char dicionario[5010][20];

int main() {
	int L, D, N, _42 = 1;
	scanf(" %d %d %d", &L, &D, &N);
	for (int i=0;i<D;i++) {
		scanf(" %s", dicionario[i]);
	}
	for (int i=0;i < N;i++) {
		scanf(" %s", s);
		int tam = strlen(s);
		bool aberto = false;
		int cont = 0;
		memset(poss, 0, sizeof(poss));
		for (int j=0;j<tam;j++) {
			if (s[j] == '(') {
				aberto = true;
			}
			else if (s[j] == ')') {
				cont++;
				aberto = false;
			}
			else {
				poss[cont][s[j] - 'a'] = true;
				if (!aberto) cont++;
			}
		}
		int ans = 0;
		for (int j=0;j < D;j++) {
			bool pode = true;
			for (int k=0;k < L;k++) {
				if (!poss[k][dicionario[j][k] - 'a']) pode = false;
			}
			if (pode) ans++;
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
	return 0;
}

