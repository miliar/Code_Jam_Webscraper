#include <stdio.h>
#include <algorithm>

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		int n, c, R[40];
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++, getchar())
		{
			R[i] = 0;
			for (int j = 0; j < n; j++)
				if (getchar() == '1')
					R[i] = j;

		}
		c = 0;
		for (int i = 0, j; i < n; i++)
		{
			for (j = i; R[j] > i; j++);
			c += j - i;
			for (; j > i; j--)
				std::swap(R[j], R[j - 1]);
		}
		printf("Case #%d: %d\n", t, c);
	}
	return 0;
}