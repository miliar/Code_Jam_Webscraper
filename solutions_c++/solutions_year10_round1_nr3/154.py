#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		int A1, A2, B1, B2;
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);

		int n = 0;
		for (int a = A1; a <= A2; ++a)
			for (int b = B1; b <= B2; ++b)
			{
				int cw = 0;
				int A = a, B = b;
				for (;;)
				{
					if (A <= 0 || B <= 0) break;
					if (A < B) swap(A, B);
					if (A > 2 * B) break;
					A -= B;
					cw ^= 1;
				}

				if (!cw)
					++n;
			}

		printf("Case #%d: %d\n", tc + 1, n); 
	}

	return 0;
}
