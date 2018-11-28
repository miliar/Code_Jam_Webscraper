#include <stdio.h>

int size;
int einfo[110][110];
int coorr[11111];
int coorc[11111];
int many;

int abs(int n) {
	if ( n < 0)
		return -n;
	return n;
}

void maxx(int &a, int b) {
	if (b > a)
		a = b;
}

void minn(int &a, int b) {
	if (b < a)
		a = b;
}

bool test2(int d, int r, int c) {
	if (r < 0 || r >= size || c < 0 || c >= size)
		return true;
	else if (einfo[r][c] == -1)
		return true;
	else
		return (d == einfo[r][c]);
}

int test(int r, int c) {
	int i;
	int re = 0;
	for (i = 0; i < many; i++) {
		int nr = coorr[i];
		int nc = coorc[i];
		int dr = nr - r;
		int dc = nc - c;
		if ( test2(einfo[nr][nc], nr, nc - 2 * dc) == false)
			return -1;
		if ( test2(einfo[nr][nc], nr - 2 * dr, nc) == false)
			return -1;
		if ( test2(einfo[nr][nc], nr - 2 * dr, nc - 2 * dc) == false)
			return -1;
		maxx(re, abs(dr) + abs(dc) + 1);
	}
	return re;
}

int main() {
	int ecase;
	int ecount;
	int i,j, k,l;
	int en;
	int asize;
	scanf("%d",&ecase);
	for(ecount = 1; ecount<=ecase;ecount++) {
		scanf("%d", &en);
		for (i = 0; i < 110; i++)
			for (j = 0; j < 110; j++)
				einfo[i][j] = -1;
		many =0;
		for (i = 0; i < en; i++)
			for (j = 0; j <=i; j++) {
				int r = i;
				int c = en - 1 - i + 2 * j;
				scanf("%d", &einfo[r][c]);
				coorr[many] = r;
				coorc[many] = c;
				many++;
			}
		for (i = en - 2; i>= 0; i--)
			for (j = 0; j <= i; j++) {
				int r = 2 * en - 2 - i;
				int c = en - i - 1 + 2 * j;
				scanf("%d", &einfo[r][c]);
				coorr[many] = r;
				coorc[many] = c;
				many++;
			}
		size = en * 2 - 1;
		/*for (i = 0; i < size; i++) {
			for (j = 0; j < size; j++) {
				if (einfo[i][j] == -1)
					printf("x ");
				else
					printf("%d ", einfo[i][j]);
			}
			printf("\n");
		}*/
		asize = size * 20;
		int re;
		for (i = 0; i < size; i++)
			for (j = 0; j < size ;j++) {
				re = test(i, j);
				if (re != -1) {
					//fprintf(stderr, "(%d, %d) -> aisze=%d\n", i, j, re);
					minn(asize, re);
				}
			}
		printf("Case #%d: %d\n", ecount, asize * asize - en * en);
	}
	return 0;

}
