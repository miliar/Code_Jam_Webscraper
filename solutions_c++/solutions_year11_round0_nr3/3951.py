/*


*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	int T;
	int casen = 1;

	freopen("C-small-attempt0.in.txt", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);

	scanf("%ld", &T);
	while (T--)
	{
		int n, c[15];
		int i, j;
		int ans, cs, cp, rs, rp;

		scanf("%d", &n);
		for (i=0; i<n; i++)
			scanf("%d", c+i);

		// Process_data(c, n);  //优化1(去掉相同的数,一定给S).对于n=15,做不做无所谓了……
		ans = -1;
		for (i=(1<<n)-2; i>0; i--) //枚举，产生所有子集
		{
			cs = cp = 0;
			rs = rp = 0;
			for (j=0; j<n; j++)
				if ( ((1<<j)&i) != 0) //判断i的第j位是不是1,如果是,表示该糖果给S
				{
					cs ^= c[j];
					rs += c[j];
				}
				else
				{
					cp ^= c[j];
					rp += c[j];
				}

			if (cs == cp)   // 优化2（利用对称性，其实循环只需要到i>=( 1<<(n-1) )即可），只是下面比较的时候加rp即可
				ans = rs > ans ? rs : ans;
		}

		if (ans == -1) printf("Case #%d: NO\n", casen++);
		else printf("Case #%d: %d\n", casen++, ans);
	}

	return 0;
}

/*
Input:

2
5
1 2 3 4 5
3
3 5 6

*/