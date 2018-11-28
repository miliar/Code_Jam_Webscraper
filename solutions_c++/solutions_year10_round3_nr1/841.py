#include <cstdio>

int main()
{
	int T, N;
	int i, j, k, resp;
	int A[1000];
	int B[1000];

	scanf("%d", &T);
	for (i = 1 ; i <= T ; i++)
	{
		scanf("%d", &N);
		for (j = 0 ; j < N; j++)
		{
			scanf("%d", &A[j]);
			scanf("%d", &B[j]);
		}

		resp = 0;
		for (j = 0 ; j < N ; j++)
		{
			for (k = j + 1 ; k < N ; k++)
			{
				if ((A[j] > A[k] && B[j] < B[k]) ||
					(A[j] < A[k] && B[j] > B[k]))
				{
					resp++;
				}
			}
		}

		printf("Case #%d: %d\n", i, resp);
	}

	return 0;
}
