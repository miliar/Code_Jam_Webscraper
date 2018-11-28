#include <stdio.h>
#include <stdlib.h>
#define M 10000100
int k, r, n, g[M];
int fim[M], luc[M];

int main () {
	int t, n, k;
	scanf ("%d", &t);
	
	int caso = 1;
	while (t--) {
		scanf ("%d%d%d", &r, &k, &n);
		int ini = 0;
		int soma = 0;
		for (int i = 0; i < n; ++i) {
			scanf ("%d", &g[i]);
			soma += g[i];
			while (soma > k) {
				luc[ini] = soma-g[i];
				fim[ini] = i;
				soma -= g[ini];
				ini++;
			}
		}
		int pos = 0;
		//printf ("tow no mei: %d %d\n", ini, soma);
		while (ini < n) {
			if (pos == ini) {
				//printf ("altera %d\n", ini);
				luc[ini] = soma;
				fim[ini] = pos;
				soma -= g[ini];
				ini++;
				continue;
			}
			soma += g[pos];
			while (soma > k) {
				if (ini == n) break;
				//printf ("altera %d\n", ini);
				luc[ini] = soma-g[pos];
				fim[ini] = pos;
				soma -= g[ini];
				ini++;
			}
			pos++;
		}
		long long total = 0;
		pos = 0;
		for (int i = 0; i < r; ++i) {
			total += luc[pos];
			pos = fim[pos];
		}
		printf ("Case #%d: %lld\n", caso++, total);
	}
	return 0;
}

