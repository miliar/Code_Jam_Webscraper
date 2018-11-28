#include <cstdio>
#include <memory.h>

int main()
{
	int T, R, K, N, groupSize[1001];
	long long earned;
	int testCase;
	long long sum[1001];
	int len[1001];
	scanf("%d", &T);
	for (testCase = 1; testCase <= T; testCase++)
	{
		scanf("%d", &R);
		scanf("%d", &K);
		scanf("%d", &N);
		earned = 0;
		memset(sum, 0, sizeof(sum));
		memset(len, 0, sizeof(len));

		int idx;
		for (idx = 0; idx < N; idx++)
			scanf("%d", &groupSize[idx]);
		
		long long tmp = 0;
		int head;
		idx = 0;
		for (head = 0; head < N; head++)
		{
			while (tmp <= K && idx < N)
			{
				tmp += groupSize[(head + idx) % N];
				idx ++;
			}
			if (idx == N && tmp <= K)
			{
				sum[head] = tmp;
				len[head] = idx;
			}
			else 
			{
				idx--;
				len[head] = idx;
				sum[head] = tmp - groupSize[(head + idx) % N];
				tmp = tmp - groupSize[head];
			}
		}

		//for (idx = 0; idx < N; idx++)
		//	printf("%lld^%d \n", sum[idx], len[idx]);

		head = 0;
		for (idx = 0; idx < R; idx++)
		{
			earned += sum[head];
			head = (head + len[head]) % N;
		}

		printf("Case #%d: %lld\n", testCase, earned);
	}
	return 0;
}
	
