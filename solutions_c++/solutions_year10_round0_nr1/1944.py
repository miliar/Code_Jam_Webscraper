#include <cstdio>
#include <cmath>

void testCase(int number)
{
	int N, K;
	bool result = false;

	// input
	scanf("%d %d", &N, &K);

	int cycleLength = (int) pow(2, N);

	result = ((K + 1) % cycleLength) == 0;

	// output
	printf("Case #%d: %s\n", number, (result ? "ON" : "OFF"));
}

int main()
{
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		testCase(i+1);
	}

	return 0;
}
