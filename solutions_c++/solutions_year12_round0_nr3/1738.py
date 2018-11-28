#include <iostream>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
int A, B;
long long count;

int main()
{
	fscanf(f, "%d", &T);

	for (int k = 0; k < T; ++k)
	{
		fscanf(f, "%d %d", &A, &B);
		int y = A;
		int n = 1;
		count = 0;
		while (y != 0)
		{
			n = n * 10;
			y = y / 10;
		}
		n = n / 10;
		for (int i = A; i <= B; ++i)
		{
			int x = i;
			do
			{
				int r = x % 10;
				x = (x / 10) + r * n;
				if ((x <= B) && (x != i) && (x >= A) && (x < i))
				{
					count++; 
				}
			}
			while (x != i);
		}

		fprintf(g, "Case #%d: %lld\n", k + 1, count);
	}

	return 0;
}