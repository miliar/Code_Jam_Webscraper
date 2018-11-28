#include <stdio.h>
#include <math.h>

int a[510][510] = {0};

int main()
{
	int cas;
	freopen("B-small-attempt0.in" , "r" , stdin);
	freopen("B-small-attempt0.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		int r , c , d;
		scanf("%d %d %d" , &r , &c , &d);
		for (int i = 0; i < r; i ++)
		{
			char s[510];
			scanf("%s" , s);
			for (int j = 0; j < c; j ++)
				a[i][j] = d + s[j]-'0';
		}
		int maxk = (r < c) ? r : c;
		int found = 0;
		int k;
		for (k = maxk; k >= 3; k --)
		{
			double mid;
			if (k % 2 == 1) mid = k>>1;
			else mid = (k>>1) - 0.5;
			for (int i = 0; i < r - k + 1; i ++)
			{
				for (int j = 0; j < c - k + 1; j ++)
				{
					double resx = 0 , resy = 0;
					
					for (int x = 0; x < k; x ++)
						for (int y = 0; y < k; y ++)
						{
							if ((x == 0 && y == 0) || (x == 0 && y == k-1) ||
								(x == k-1 && y == 0) || (x == k-1 && y == k-1)) continue;
							resx += (x-mid) * a[i+x][j+y];
							resy += (y-mid) * a[i+x][j+y];
						}
					if (fabs(resx) < 1e-7 && fabs(resy) < 1e-7)
					{ found = 1; break; }
				}
				if (found) break;
			}
			if (found) break;
		}
		if (found)
			printf("Case #%d: %d\n" , ca , k);
		else
			printf("Case #%d: IMPOSSIBLE\n" , ca);
	}
	return 0;
}