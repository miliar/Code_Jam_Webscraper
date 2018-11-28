#include <stdio.h>
#include <string.h>
#include <stdlib.h>
__int64 number[41];
__int64 req[41];
__int64 temp;
int n, t;
char st[100];
int ans,l ;

int compare(const void *p1, const void *p2)
{
	return (*(__int64 *)p1) - (*(__int64 *)p2);
}

int main()
{
	req[1] = 2; 
	for (int i = 2; i <= 40; ++i) req[i] = req[i - 1] * 2;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d\n",&n);
		ans = 0;
		for (int j = 1; j <= n; ++j)
		{
			gets(st);
			number[j] = 0;
			for (int k = strlen(st) - 1; k >= 0; --k)
			{
				number[j] = number[j] * 2 + st[k] - '0';			
			}
		}

		for (int j = 1; j <= n; ++j)
			if (number[j] >= req[j])
			{
				for (int k = j + 1; k <=n; ++k)
					if (number[k] < req[j])
					{
						l = k;
						while (l > j)
						{
							temp = number[l-1];
							number[l-1] = number[l];
							number[l] = temp;
							ans++;
							l--;
						}
						break;
					}

			}
		printf("Case #%d: %d\n", i, ans );
	}
	return 0;
}
