#include <cstdio>

int Test, last[100];
void work()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		char s[100];
		scanf("%s", s);
		last[i] = 0;
		for (int j = n - 1; j + 1; --j)
			if (s[j] == '1')
			{
				last[i] = j;
				break;
			}
	}
	int cnt = 0;
	for (int i = 0; i < n; ++i)
	{
		if (last[i] > i)
		{
			for (int j = i + 1; j < n; ++j)
			{
				if (last[j] <= i)
				{
					for (int k = j - 1; k >= i; --k)
					{
						int t = last[k]; last[k] = last[k + 1]; last[k + 1] = t;
						++cnt;
					}
					break;
				}
			}
		}
	}
	printf("Case #%d: %d\n", ++Test, cnt);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
