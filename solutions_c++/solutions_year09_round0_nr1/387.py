
	#include <cstdio>
	#include <cstdlib>
	#include <algorithm>

	using namespace std;
	
	int l, d, n, list[5005][20], possible[20][5005];

	int main()
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		scanf("%d%d%d\n", &l, &d, &n);
		for (int i = 0; i < d; i ++)
		{
			for (int j = 0; j < l; j ++)
				list[i][j] = getchar();
//			for (int j = 0; j < l; j ++)
//				putchar(list[i][j]);
//			putchar('\n');
			char c;
			c = getchar();
			if (c != '\n')	printf("!!!");
		}
		for (int i = 0; i < n; i ++)
		{
			memset(possible, 0, sizeof(possible));
			char c;
			for (int j = 0; j < l; j ++)
			{
				c = getchar();
				if (c == '(')
				{
					while (c = getchar(), c != ')')
					{
						possible[j][c] = 1;
						//printf("	%d %c\n", j, c);
					}
				}
				else
				{
					possible[j][c] = 1;
					//printf("	%d %c\n", j, c);
				}
			}
			c = getchar();
			if (c != '\n')	printf("!_!");
			int ans = 0;
			for (int j = 0; j < d; j ++)
			{
				int flag = 1;
				for (int k = 0; k < l; k ++)
					if (possible[k][list[j][k]] == 0)
					{
						flag = 0;
						//printf("		%d %c\n", k, list[j][k]);
					}
				if (flag == 1)	ans ++;
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
		return 0;
	}
