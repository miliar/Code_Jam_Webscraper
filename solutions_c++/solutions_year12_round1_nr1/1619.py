#include <stdio.h>
#include <memory.h>


int main() {
	freopen("A-small-attempt0.in", "r" ,stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int cases, A, B, d;
	double m[8];
	double k[3];
	double ans, temp;
	scanf("%d", &cases);
	for (int p = 1; p <= cases; p++) {
		ans = 0;
		scanf("%d%d", &A, &B);
		for (int i = A-1; i >= 0; i--)
			scanf("%lf", &k[i]);
		d = 1;
		for (int i = 1; i <= A; i++) d *= 2;

		for (int i = 0; i < d; i++) {
			m[i] = 1.0;
			for (int j = 0; j < A; j++)
                m[i] *= (i & (1 << j))? (1.0-k[j]): k[j];//, printf("%lf ", m[i]);;
//			printf("\n%d %lf\n", i, m[i]);
		}

		for (int i = 0; i < d; i++) {
			if (i == 0) ans += m[i] * (B-A+1);
			else ans += m[i] * (B-A+2 + B);
	//		printf("%lf\n", ans);
		}
	//	printf("%lf\n", ans);
		if (ans > B+2) ans = B+2;
	//	printf("%lf\n", ans);

		for (int j = 1; j <= A; j++) {
            temp = 0;
			for (int i = 0; i < d; i++) {
				if (j == 1)
					temp += ((i & 6) == 0)? m[i] * (B-A+3) : m[i] * (B-A+4+B);
				else if (j == 2)
					temp += ((i & 4) == 0)? m[i] * (B-A+5) : m[i] * (B-A+6+B);
				else
					temp += m[i] * (B-A+7);
			}
			if (temp < ans ) ans = temp;
	//		printf("%d %lf\n", j, temp);
		}
		printf("Case #%d: %.6lf\n", p, ans);
	}
	return 0;
}
