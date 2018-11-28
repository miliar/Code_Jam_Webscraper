#include <cstdio>
#include <algorithm>
using namespace std;

int A[21] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
int candies[1001];

bool check(int n)
{
	for (int p = 0; p < 20; p++)
	{
		int s = 0;
		for (int i = 0; i < n; i++)
			if (A[p] & candies[i]) s++;
		if (s % 2 == 1) return false;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", candies + i);
		if (!check(N))
		{
			printf("Case #%d: NO\n", Ti);
			continue;
		}
		int smallest = 200000001;
		for (int i = 0; i < N; i++)
			smallest = min(smallest, candies[i]);
		int sum = 0;
		for (int i = 0; i < N; i++)
			sum += candies[i];
		sum -= smallest;
		printf("Case #%d: %d\n", Ti, sum);
	}
	return 0;
}
