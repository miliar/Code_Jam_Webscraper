#include <cstdio>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MAXN = 110;
const int oo = INT_MAX / 2;
int a[MAXN];

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		int D, I, M, N;	
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &a[i]);

		int old[266], nold[266];

		int *o = old, *n = nold;

		for (int j = 0; j < 256; ++j)
		{
			o[j] = +oo;
			o[j] = min(o[j], D + I);
			o[j] = min(o[j], abs(a[0] - j));
		}
		for (int i = 1; i < N; ++i)
		{
			for (int j = 0; j < 256; ++j)
				n[j] = oo;
			for (int j = 0; j < 256; ++j)
			{
				n[j] = min(n[j], D * i + D + I);
				n[j] = min(n[j], D * i + abs(a[i] - j));
			}

			for (int j = 0; j < 256; ++j)
				for (int k = 0; k < 256; ++k)
					if (abs(j - k) <= M)
					{
						if (j == k)
							n[k] = min(n[k], o[k] + D);
						n[k] = min(n[k], o[j] + abs(a[i] - k));
						n[k] = min(n[k], o[j] + D + I);
					}
					else if (M != 0)
					{
						n[k] = min(n[k], o[j] + I * ((abs(k - j) - 1) / M + 1) + D);
						n[k] = min(n[k], o[j] + I * ((abs(k - j) - 1) / M) + abs(a[i] - k));
					}

			int *t = o;
			o = n;
			n = t;
		}

		int minCost = D * N;
		for (int i = 0; i < 256; ++i)
			if (o[i] < minCost)
				minCost = o[i];
		printf("Case #%d: %d\n", tc + 1, minCost);
	}

	return 0;
}
