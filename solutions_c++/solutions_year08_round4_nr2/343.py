#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int area, t, x2, x3, y2, y3, n, m;

void work()
{
	printf("Case #%d: ", t);
	scanf("%d%d%d", &n, &m, &area);
	for (x2=0;x2<=n;++x2)
		for (x3=0;x3<=n;++x3)
			for (y2=0;y2<=m;++y2)
				for (y3=0;y3<=m;++y3)
					if (abs(x2*y3 - x3*y2) == area)
					{
						printf("0 0 %d %d %d %d\n", x2, y2, x3, y3);
						return;
					}
	printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d", &test);
	for (t=1;t<=test;++t)
		work();
}
