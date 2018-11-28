#include <stdio.h>
#include <math.h>

int i,j,k,cases,_case;
int N, M, A;
long long x1, Y1, x2, y2, x3, y3;
long long a;
long long sa, sb, sc, s, S, all, all1, all2, all3;

inline double mabs(double a) {
	if (a < 0) return -a;
	return a;
}

int main() {
	scanf("%d", &cases);
	for (_case = 1; _case <= cases; _case++) {
		printf("Case #%d: ", _case);

		scanf("%d%d%d", &N, &M, &A);
		a = A;
		
		all = (M+1) * (N+1);

		for (all1 = 0; all1 < all/2; all1++) {
			x1 = all1 / (M+1);
			Y1 = all1 % (M+1);
			for (all2 = all1 + 1; all2 < all; all2++) {
				x2 = all2 / (M+1);
				y2 = all2 % (M+1);
					if (x1 == x2) continue;
						for (x3 = 0; x3 <= N; x3++) {
//							for (y3 = 0; y3 <= M; y3++) {
								y3 = (-a - x2 * Y1 + x3 * Y1 + x1*y2 - x3*y2) / (x1 - x2);
								S = (x2 - x1)*(y3-Y1) - (y2 - Y1)*(x3-x1);
								if (y3 >= 0 && y3 <= M && (S == a || S == -a)) goto end;
								y3 = (a - x2 * Y1 + x3 * Y1 + x1*y2 - x3*y2) / (x1 - x2);
								S = (x2 - x1)*(y3-Y1) - (y2 - Y1)*(x3-x1);
								if (y3 >= 0 && y3 <= M && (S == a || S == -a)) goto end;
//							}
						}
					}
		}
end:
		if (all1 >= all/2) printf("IMPOSSIBLE");
		else printf("%lld %lld %lld %lld %lld %lld", x1, Y1, x2, y2, x3, y3);

		printf("\n");
	}
	return 0;
}


