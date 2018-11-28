#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXL = 1 << 10;

int K, L;
char str[MAXL];
char permuted[MAXL];

int main () {
	int tc;
	scanf ("%d", &tc);
	
	for (int ctc = 1; ctc <= tc; ++ctc) {
		scanf ("%d", &K);
		scanf ("%s", str);
		L = strlen(str);
	
		int perm[] = {0, 1, 2, 3, 4};
		int res = L;
		permuted[L] = 0;
		do {
			for (int i = 0; i < L; ++i) {
				//printf ("%d <- %d\n", perm[i % K] + i - i % K, i);
				permuted[perm[i % K] + i - i % K] = str[i];
			}
/*			for (int i = 0; i < K; ++i)
				printf ("%d ", perm[i]);
			printf (" %s %s\n", str, permuted);
	*/		res = std::min(res, std::unique(permuted, permuted + L) - permuted);
		} while (std::next_permutation(perm, perm + K));
		printf ("Case #%d: %d\n", ctc, res);
	}

	return 0;
}
