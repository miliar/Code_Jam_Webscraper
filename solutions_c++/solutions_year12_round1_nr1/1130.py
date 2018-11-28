#include <algorithm>
#include <cstdio>

using namespace std;

const int A = 99999;

int main()
{
	//
	int t, a, b, i, j, k;
	double p[A], e, r, m;

	scanf("%d", &t);
	for (i = 1; i <= t ; ++i)
	{
		scanf("%d %d", &a, &b);

		for (j = 0; j < a; ++j)
			scanf("%lf", &p[j]);	
		
		m = b + 2;

		r = 1;
		for (j = a; j >= 0; --j)
		{
			k = a - j - 1;
			if (k >= 0)
				r *= p[k];
			e = (j + j + b - a + 1) * r + (j + j + b - a + 1 + b + 1) * (1 - r);
			if (e < m)
				m = e;
		}
		printf("Case #%d: %.6f\n", i, m);
	}

	//
	return 0;
}

