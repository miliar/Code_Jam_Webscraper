#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	int n, m, i, j, T, t = 1, xx1, xx2, yy1, yy2, A, flag;
	//freopen("B-large.in","r",stdin);
	//freopen("B.out","w",stdout);
	scanf("%d", &T);
	while (T --)
	{
		scanf("%d%d%d", &n, &m, &A);
		flag = 0;
		printf("Case #%d:", t ++);
		for (xx1 = 0; xx1 <= n; xx1 ++)
		{
			for (xx2 = 0; xx2 <= n; xx2 ++)
			{
				for (yy1 = 0; yy1 <= m; yy1 ++)
				{
					for (yy2 = 0; yy2 <= m; yy2 ++)
					{
						if (abs(xx1 * yy2 - xx2 * yy1) == A)
						{
							flag = 1;
							printf(" 0 0 %d %d %d %d\n", xx1, yy1, xx2, yy2);
							break;
						}
					}
					if (flag == 1)
						break;
				}
				if (flag == 1)
					break;
			}
			if (flag == 1)
				break;
		}
		if (flag == 0)
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}