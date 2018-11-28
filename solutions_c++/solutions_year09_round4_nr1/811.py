#include <cstdio>

int tests, n, val[50];
char tmp[50];

int main()
{
	scanf("%d", &tests);
	for (int t = 0; t < tests; t++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", &tmp);
			
			int last = -1;
			for (int j = 0; j < n; j++)
				if (tmp[j] == '1')
					last = j;
			
			val[i] = last;
		}
		
		int ans = 0;
		for (int i = 0; i < n; i++)
		{
			if (val[i] > i)
			{
				for (int j = i + 1; j < n; j++)
					if (val[j] <= i)
					{
						int tm = val[j];
						for (int k = j - 1; k >= i; k--)
							val[k + 1] = val[k];
						ans += j - i;
						val[i] = tm;
						break;
					}
			}
		}
		
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}