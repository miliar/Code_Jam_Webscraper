#include <cstdio>
#define dif(a,b) (((a) > (b)) ? ((a)-(b)) : ((b)-(a)))

int main () {
	int i, j, nO, nB, n, t, elaps, cO, cB, pB, pO, x;
	char R[102];
	int P[102], B[102], O[102];
	FILE *p = fopen("A-large.in","r");

	fscanf(p, "%d", &t);
	for (i = 0; i != t; i++) {
		nB = nO = elaps = cO = cB = 0;
		pB = pO = 1;
		fscanf(p, "%d", &n);
		for (j = 0; j != n; j++) {
			fscanf(p, " %c %d", &R[j], &P[j]);
			if (R[j] == 'O') O[nO++] = P[j];
			else B[nB++] = P[j];
		}
		for (j = 0; j != n; j++) {
		//	printf("j=%d, pB = %d, pO = %d, tupla=(%c,%d)\n", j, pB, pO, R[j], P[j]);
			if (R[j] == 'O') {
				cO++;
				x = (dif(pO, P[j])+1);
				elaps += x;
				pO = P[j];
				if (cB < nB) {
					if ( dif(pB, B[cB]) < x)
						pB = B[cB];
					else if (pB > B[cB]) pB -= x;
					else pB += x;
				}
			}
			else {
				cB++;
				x = (dif(pB, P[j])+1);
				pB = P[j];
				elaps += x;
				if (cO < nO) {
					if ( dif(pO, O[cO]) < x)
						pO = O[cO];
					else if (pO > O[cO]) pO -= x;
					else pO += x;
				}
			}
		//	printf("elaped += %d => %d\n\n", x, elaps);
		}
		printf("Case #%d: %d\n", i+1, elaps);
	}

	return 0;
}
