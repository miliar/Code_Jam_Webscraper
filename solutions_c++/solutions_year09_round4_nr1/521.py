#include <stdio.h>
#include <string.h>

char str[40][50];
int t, n;
char strt[50];

int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%s", str+j);
			int r = n - 1;
			while (r >= 0 && str[j][r] == '0')
			{
				str[j][r] = 0;
				r--;
			}
		}
		int res = 0;
		for (int j = 0; j < n; j++)
		{
			if (strlen(str[j]) > j+1)
			{
				int k = j+1;
				for (; k < n; k++)
				{
					if (strlen(str[k]) <= j + 1)
					{
						break;
					}
				}
				res += k - j;
				for (k--; k >= j; k--)
				{
					strcpy(str[k+1], str[k]);
				}
			}
		}
		printf("Case #%d: %d\n", i+1, res);
	}
}
