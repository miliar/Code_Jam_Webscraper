#include <stdio.h>
#include <map>
using namespace std;

int C, N, M, A;
map<int, pair<int, int> > Q;

// a = xy
int makeable(int a) {
	for (int i = (a + N - 1) / N; i <= M; i++)
	 if (a % i == 0) return i;
	return 0;
}

int main() {
	scanf("%d", &C);
	for (int case_x = 1; case_x <= C; case_x++) {
		scanf("%d%d%d", &N, &M, &A);
		int x2, y2, x3, y3 = 0;
		for (int i = 0; i <= N * M - A; i++) {
			if ((i == 0 || (y2 = makeable(i))) &&
			 (y3 = makeable(i + A))) {
				if (i) x3 = i / y2;
				else x3 = y2 = 0;
				x2 = (i + A) / y3;
				break;
			}
		}
		if (y3 && abs(x2 * y3 - x3 * y2) != A) {
			fprintf(stderr, "%d * %d - %d * %d != %d", x2, y3, x3, y2, A);
			fprintf(stderr, "ERROR\n");
		}
		if (y3 && (N < x2 || N < x3 || M < y2 || M < y3)) {
			fprintf(stderr, "CERROR\n");
		}
		if (y3) printf("Case #%d: 0 0 %d %d %d %d\n", case_x, x2, y2, x3, y3);
		 else printf("Case #%d: IMPOSSIBLE\n", case_x);
	}
	return 0;
}
