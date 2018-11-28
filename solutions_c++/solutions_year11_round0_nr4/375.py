#include <stdio.h>
#include <stdlib.h>

#define FOR(i, N)	for (int i=0; i<N; ++i)

namespace
{
	const int cMaxN = 1000;
}

bool fix_combination(int N, int* list, bool* list_fixed)
{
	FOR (i, N)
	{
		if (list_fixed[i]) continue;

		int a = list[i];
		int b = list[a - 1];

		if (i == b - 1)
		{
			list_fixed[i] = true;
			list_fixed[a - 1] = true;
			return true;
		}
	}
	return false;
}

float solve(int N, int* list)
{
	int remains = N;
	float result = 0.f;

	bool list_fixed[cMaxN];
	FOR (i, N) list_fixed[i] = false;

	// solve initial correct

	FOR (i, N) if (i+1 == list[i]) {--remains; list_fixed[i] = true;}
	if (remains == 0) return 0.f;

	// solve all combination

	while (fix_combination(N, list, list_fixed))
	{
		result += 2.f;
		remains -= 2;
	}

	// solve remains

	if (remains > 1)
	{
#if 0
		while (remains >= 2)
		{
			result += remains;
			--remains;
		}
#endif
		result += remains;
	}

	return result;
}

int main()
{
#if 1
	int T = 0; scanf("%d", &T);

	FOR (t, T)
	{
		int list[cMaxN];

		int N = 0; scanf("%d", &N);
		FOR (i, N) scanf("%d", &list[i]);

		printf("Case #%d: %.6f\n", t+1, solve(N, list));
	}
#else
	double result = 0.f;
	int base = 2;
	FOR (i, 50)
	{
//		result += (float)(i+1) * 1.f / (float)base;
//		base *= 2;

		FOR (ones, i+1)
		{
			double p = 1.f;

			FOR (test, i+1-1)
			{
				if (test < ones) p *= 1.f / 2.f;
				else p *= 1.f / 3.f; 
			}

			if (ones > 0) p *= 1.f / 2.f;
			else p *= 1.f / 6.f;

			result += (double)(i+1) * p;
		}

	}
	printf("test: %.6f\n", result);
#endif
}
