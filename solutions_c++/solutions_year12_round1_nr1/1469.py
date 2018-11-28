#include <cstdio>
#include <cmath>

const long double p_one = static_cast<long double>(1.0);

long double p[100000];
long double pp[100000]; // pp = p[i] * pp[i-1]
long double ps[100000];

long double p_min;

int main() {
	int T, A, B, x_max;
	long double p_cur;

	scanf("%d", &T);
	for (int case_i = 1; case_i <= T; ++case_i)
	{
		scanf("%d%d", &A, &B);
		for (int i = 0; i < A; ++i)
		{
			scanf("%Lf", &p[i]);
		}
		p_min = B + 2;
		x_max = (2 + A) / 2;

		pp[A] = 1;
		for (int i = 0; i < A; ++i)
			pp[A - i - 1] = pp[A - i] * p[i];

		ps[0] = pp[0];
		
		for (int x = 0; x <= x_max; ++x) {
			if (x>0) {
				ps[x] = ps[x-1] + pp[x]*(p_one - p[A - x]);
				if (ps[x] > p_one)
					ps[x] = p_one;
			}
			p_cur = ps[x] * (2*x + B - A + 1) + (1 - ps[x]) * (2*(x+B+1) - A);
			if (p_min > p_cur)
				p_min = p_cur;
		}
		printf("Case #%d: %.6Lf\n", case_i, p_min);
	}
	return 0;
}

