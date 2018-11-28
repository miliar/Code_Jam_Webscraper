#include <cstdio>
#include <iostream>

using namespace std;

struct Node
{
	int x, y;
};
Node N[1024];
int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	long long T, i, j, n, X, Y,x0, y0, M, t = 1, ans, xx, yy, k, A, B, C, D;
	scanf("%lld", &T);
	while (T --)
	{
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n, &A, &B, &C, &D, &x0, &y0, &M);
		N[0].x = x0;
		N[0].y = y0;
		for (i = 1; i < n; i ++)
		{
			N[i].x = (A*N[i-1].x + B) % M;
			N[i].y = (C*N[i-1].y + D) % M;
		}
		ans = 0;
		for (i = 0; i < n; i ++)
		{
			for (j = i + 1; j < n; j ++)
			{
				for (k = j + 1; k < n; k ++)
				{
					xx = N[i].x + N[j].x + N[k].x;
					yy = N[i].y + N[j].y + N[k].y;
					if (xx % 3 == 0 && yy % 3 == 0)
						ans ++;
				}
			}
		}
		printf("Case #%lld: %lld\n", t ++, ans);
	}
	return 0;
}