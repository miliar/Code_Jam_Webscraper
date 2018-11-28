#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int testcase = 0; testcase < T; ++testcase)
	{
		int C, N;
		scanf("%d%d", &C, &N);
		double r = 1.0;
		double comb = 1.0;
		double ans = 0.0;
		double sgn = 1.0;
		for (int j = 1; j <= C; ++j)
		{
			r *= C - N + 1 - j;
			r /= C - j + 1;
			comb *= C - j + 1;
			comb /= j;
			double term = sgn * comb * 1 / (1 - r);
			// fprintf(stderr, "j=%d, r=%f, comb=%f, term=%f\n", j, r, comb, term);
			ans += term;
			sgn = -sgn;
		}
		printf("Case #%d: %.10f\n", testcase + 1, ans);
	}
	return 0;
}
