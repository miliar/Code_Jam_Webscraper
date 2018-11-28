#include <stdio.h>
#include <string.h>

bool a[120][120];
int main(void)
{
	int t, r, x1, y1, x2, y2, i, j, ans, sum, test = 0;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d", &r);
		memset(a, false, sizeof(a));
		while(r --)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

			for(i = x1;i <= x2;i ++)
				for(j = y1;j <= y2;j ++)
					a[i][j] = true;
		}
		ans = 0;
		sum = 0;
		for(i = 1;i < 101;i ++)
			for(j = 1;j < 101;j ++)
				if(a[i][j])
					sum ++;
		while(sum > 0)
		{
			for(i = 101;i > 0;i --)
			{
				for(j = 101;j > 0;j --)
				{
					if(a[i][j])
					{
						if(!a[i - 1][j] && !a[i][j - 1])
						{
							a[i][j] = false;
							sum --;
						}
					}
					else
					{
						if(a[i - 1][j] && a[i][j - 1])
						{
							a[i][j] = true;
							sum ++;
						}
					}
				}
			}
			ans ++;
		}
		printf("Case #%d: %d\n", ++test, ans);
	}
	return 0;
}