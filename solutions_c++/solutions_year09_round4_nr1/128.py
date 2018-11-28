#include<stdio.h>
#include<algorithm>
using namespace std;

int n, r[50];
char b[50][50];

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", b[i]);
			r[i] = -1;
			for (int x = n-1; x >= 0; x--)
			{
				if (b[i][x] == '1')
				{
					r[i] = x;
					break;
				}
			}
		}

		int ans = 0, tmp, flag;
		for (int i = 0; i < n; i++)
		{
			flag = 0;
			if (r[i] > i)
			{
				flag = 1;
				for (int j = i+1; j < n; j++)
				{
					if (r[j] <= i)
					{
						tmp = j;
						break;
					}
				}
			}
			if (!flag)
				continue;
			for (int j = tmp; j > i; j--)
			{
				ans++;
				swap(r[j], r[j - 1]);
			}
		}
		
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
