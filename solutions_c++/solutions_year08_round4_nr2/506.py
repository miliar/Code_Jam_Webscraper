#include <cstdio>

int n, m, A;
int area[3000][6];

int findIt()
{
	int ax, ay, bx, by, cx, cy;

	ax = ay = 0;
	for(bx = 0; bx <= n; ++bx)
		for(by = 0; by <= m; ++by)
			for(cx = 0;cx <= n; ++cx)
				for(cy = 0; cy <= m; ++cy)
				{
					int s = (ax * by + bx * cy + cx * ay) - (ay * bx + by * cx + cy * ax);
					if(s < 0) s *= -1;
					if(s == A){ printf("%d %d %d %d %d %d\n", ax, ay, bx, by, cx, cy); return 1; }
				}
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i;
    int r, cs = 0;
	scanf("%d", &r);
	while(r--)
	{
		printf("Case #%d: ", ++cs);
		scanf("%d %d %d", &n, &m, &A);
		for(i = 1; i <= A; ++i) area[i][0] = -1;
		if(!findIt()) printf("IMPOSSIBLE\n");

	}
	return 0;
}