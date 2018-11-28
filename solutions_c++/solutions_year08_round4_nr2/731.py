#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int N, M , t, A, i;
	int x1, x2, y1, y2, Case;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d", &Case);
	for (i = 1; i <= Case; i ++)
	{
		scanf("%d%d%d", &N, &M, &A);
		t = 0;
		printf("Case #%d:", i);
		for (x1 = 0; x1 <= N; x1 ++)
		{
			for (x2 = 0; x2 <= N; x2 ++)
			{
				for (y1 = 0; y1 <= M; y1 ++)
				{
					for (y2 = 0; y2 <= M; y2 ++)
					{
						if (abs(x1 * y2 - x2 * y1) == A)
						{
							t = 1;
							printf(" 0 0 %d %d %d %d\n", x1, y1, x2, y2);
							break;
						}
					}
					if (t == 1)
						break;
				}
				if (t == 1)
					break;
			}
			if (t == 1)
				break;
		}
		if (!t)
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}