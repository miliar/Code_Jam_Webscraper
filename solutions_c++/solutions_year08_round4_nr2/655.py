#include <stdio.h>
#include <memory.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	long long N, M, A;
	for (int t = 0; t < T; t++)
	{
		scanf("%lld%lld%lld", &N, &M, &A);
		
		long long x1, x2, y1, y2;
		x2 = -1;
		y1 = -1;

		for (x1 = 0; x1 <= N; x1++)
			for (y2 = 0; y2 <= M; y2++)
			{

				long long B = A + x1 * y2;
				for (long long z = 1; z * z <= B && z <= N; z++)
					if (B % z == 0 && B / z <= M)
					{
						x2 = z;
						y1 = B / z;
						goto lbl;
					}
				for (long long z = 1; z * z <= B && z <= M; z++)
					if (B % z == 0 && B / z <= N)
					{
						x2 = B / z;
						y1 = z;
						goto lbl;
					}
			}
lbl:

		if (x2 == -1)
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else
			printf("Case #%d: 0 0 %lld %lld %lld %lld\n", t+1, x1, y1, x2, y2);
	}


	fclose(stdin);
	fclose(stdout);

	return 0;
}