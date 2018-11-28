#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char S[1010], novo[1010];

int main() {
	int N, k, tam, i, j, ans, cont, teste=1;
	int seq[10];
	scanf("%d", &N);
	while (N--) {
		scanf("%d", &k);
		scanf("%s", S);
		tam = strlen(S);
		for (i=0;i<k;i++) seq[i] = i;
		ans = tam;
		do {
			for (i=0;i<tam;i+=k) {
				for (j=0;j<k;j++) {
					novo[i+j] = S[i+seq[j]];
				}
			}
			cont = 1;
			for (i=1;i<tam;i++) {
				if (novo[i] != novo[i-1]) cont++;
			}
			if (cont < ans) ans = cont;
		} while (next_permutation(seq, seq+k));
		printf("Case #%d: %d\n", teste++, ans);
	}
	return 0;
}
