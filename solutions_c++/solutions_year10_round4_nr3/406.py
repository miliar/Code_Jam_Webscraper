#include <stdio.h>
#include <string.h>


int tc() {
	int R; 
	scanf("%d", &R);

	int A[500][500];
	memset(A, 0, sizeof(int)*500*500);
	int bc = 0;
	while (R--) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for(int x=x1; x<=x2; ++x)
			for(int y=y1; y<=y2; ++y) {
				A[x][y] = 1;
				bc++;
			}
	}

	int res = 0;
	while (bc) {
		bc = 0;

/*
		printf("> %d\n", res);
		for (int x=0; x<11; ++x) {
			for (int y=0; y<11; ++y) {
				printf("%d", A[x][y]);
			}
			printf("\n");
		}
*/

		for(int x=400; x>0; --x)
			for(int y=400; y>0; --y) {
				if (A[x][y]) {
					if (!A[x-1][y] && !A[x][y-1])
						A[x][y] = 0;
					else
						bc++;
				} else {
					if (A[x-1][y] && A[x][y-1]) {
						A[x][y] = 1;
						bc++;
					}
				}
			}

		res++;
	}

	return res;
}



int main() {
	int C;
	scanf("%d", &C);
	for(int i=1; i<=C; ++i) {
		printf("Case #%d: %d\n", i, tc());
	}

	return 0;
}

