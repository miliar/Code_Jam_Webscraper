#include <cstdio>
#include <math.h>

void sort(int x[], int n)
{
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			if (x[i] > x[j])
			{
				int t = x[i];
				x[i] = x[j];
				x[j] = t;
			}
}

int main(int argc, char* argv[])
{
	int count;
	scanf("%d\n", &count);

	for (int a = 0; a < count; a++)
	{
		int n;
		scanf("%d\n", &n);

		int x[800];
		int y[800];

		for (int i = 0; i < n; i++)
			scanf("%d", x + i);

		for (int i = 0; i < n; i++)
			scanf("%d", y + i);

		sort(x, n);
		sort(y, n);

		int r = 0;
		for (int i = 0; i < n; i++)
			r += x[i] * y[n - 1 - i];

		printf("Case #%d: %d\n", a + 1, r);
	}

	return 0;
}
