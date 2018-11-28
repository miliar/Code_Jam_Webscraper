#include <cstdio>

int main()
{
	int tests;
	std::scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		int n, k;
		std::scanf("%d%d", &n, &k);
		std::printf("Case #%d: %s\n", test, (k%(1<<n) == (1<<n)-1 ? "ON" : "OFF"));
	}

	return 0;
}
