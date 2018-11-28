#include <stdio.h>
#include <string.h>
int main()
{
	int T, n, i, j, k, num[110], tcnt = 1;
	freopen("a.in", "r", stdin);
	freopen("ans.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			char tmp[100];
			scanf("%s", tmp);
			num[i] = 0;
			for (j = n - 1; j >= 0; j--)
				if (tmp[j] == '1')
				{
					num[i] = j;
					break;
				}
		}
		//for (i = 0; i < n; i++)
		//	printf("%d ", num[i]);
	//	printf("\n");
		int ans = 0;
		for(i = 0; i < n; i++)
		{
			if(num[i] > i)
			{
				for(j = i + 1; j < n; j++)
				{
					if(num[j] <= i)
					{
						ans += j - i;
						int t = num[j];
						for(k = j; k > i; k--) 
							num[k] = num[k - 1];
						num[i] = t;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", tcnt++, ans);
	}
	return 0;
}
