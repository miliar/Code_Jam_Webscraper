#include <cstdio>

int main()
{
	int T, N, K;
	scanf("%d", &T);
	int testCase, idx;
	char states[][4] = {"OFF", "ON"};
	int isFound;
	for (testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d", &N);
		scanf("%d", &K);
		isFound = 0;
		idx = 0;
		while (idx < N)
		{
			if (K % 2 != 1)
				break;
			K /= 2;
			idx++;
		}
		if (idx == N) isFound = 1;
		printf("Case #%d: %s\n", testCase, states[isFound]);
	}
	return 0;
}
