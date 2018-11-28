//Google Code Jam 2012 C; Recycled Numbers; 
#include <cstdio>
#include <cstdlib>
#include <cstring>

long long ans;
int t, cases, a, b, i, j, l, c[10], x, y, d;
int r[2000001];

int main()
{
//	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (cases = 1; cases <= t; ++cases)
	{
		ans = 0;
		scanf("%d%d", &a, &b);
		for (i = a; i < b; ++i)
		{
			r[i] = l = 0;
			x = i;
			d = 1;
			while (x)
			{
				c[++l] = x % 10;
				x /= 10;
				d *= 10;
			}
			d /= 10;
			for (y = i, j = 1; j < l; ++j)
			{
				y /= 10;
				y += d * c[j];
				if (y > i && y <= b && r[i] != y)
				{
					++ans;
					r[i] = y;
				}
			}
		}
		printf("Case #%d: %lld\n", cases, ans);
	}
	return 0;
}
