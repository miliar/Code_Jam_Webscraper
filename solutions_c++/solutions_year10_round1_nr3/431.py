#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int main()
{
	char* temp = NULL;
	size_t size = 0;
	size_t len = getline(&temp, &size, stdin);
	int cases = atoi(temp);

	int test;
	for (test = 0; test < cases; test++)
	{
		len = getline(&temp, &size, stdin);
		char* t = temp;
		int a1 = atoi(strsep(&t, " "));
		int a2 = atoi(strsep(&t, " "));
		int b1 = atoi(strsep(&t, " "));
		int b2 = atoi(t);

		unsigned long long total = 0;
		int a, b;
		for (a = a1; a <= a2; a++)
		{
			for (b = b1; b <= b2; b++)
			{
				int steps = 0;
				int min = (a < b ? a : b);
				int max = (a > b ? a : b);
				while (min != 0 && floor(max / min) == 1)
				{
					int temp = min;
					min = max % min;
					max = temp;
					steps++;
				}
				if (steps % 2 == 0) total++;
				//printf("(%i, %i) %i %i %i\n", a, b, min, max, steps);
				//printf("(%i, %i) TOTAL: %llu\n", a, b, total);
			}
		}

		printf("Case #%i: %llu\n", test+1, total);
	}
}
