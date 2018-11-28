#include <iostream>
#include <string>
using namespace std;
int fabs(int number)
{
	return number<0?-number:number;
}

int main()
{
	int n, m, ca, test = 1, x1, x2, y1, y2, area, leap;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &ca);
	while (ca --)
	{
		scanf("%d %d %d", &n, &m, &area);
		leap = 0;
		for (x1 = 0; x1 <= n; x1 ++)
		{
			for (x2 = 0; x2 <= n; x2 ++)
			{
				for (y1 = 0; y1 <= m; y1 ++)
				{
					for (y2 = 0; y2 <= m; y2 ++)
					{
						if (fabs(x1 * y2 - x2 * y1) == area)
						{
							leap = 1;
							printf("Case #%d: 0 0 %d %d %d %d\n", test++, x1, y1, x2, y2);	
							goto end;
						}
					}
				}
			}
		}end:;
		if (leap == 0)
			printf("Case #%d: IMPOSSIBLE\n", test ++);
	}
	return 0;
}