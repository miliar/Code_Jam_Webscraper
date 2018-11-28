#include <stdio.h>
#include <string.h>

int note[105];

int harm(int a, int b)
{
	if (a % b == 0)
		return 1;
	else if (b % a == 0)
		return 1;
	return 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		memset(note, 0, sizeof (note));
		for (int j = 0; j < n; ++j)
			scanf("%d", &note[j]);
		int j;
		for (j = l; j <= h; ++j)
		{
			int k;
			for (k = 0; k < n; ++k)
			{
				if (!harm(j, note[k]))
					break;
			}
			if (k == n)
			{
				printf("Case #%d: %d\n", i, j);
				break;
			}
		}
		if (j > h)
			printf("Case #%d: NO\n", i);
	}
	return 0;
}