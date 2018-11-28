#include <stdio.h>
#include <string.h>

int N, size;
int data[105][105];

bool check(int x, int y)
{
	for (int i = 1; i <= size; ++i)
		for (int j = 1; j <= size; ++j) if (data[i][j] >= 0)
		{

			// h
			int jj = 2 * y - j;
			if (1 <= jj && jj <= size)
				if (data[i][jj] >= 0 && data[i][jj] != data[i][j]) 
				{
//					printf("i = %d j = %d\n", i, j);
					return false;
				}

			// v
			int ii = 2 * x - i;
			if (1 <= ii && ii <= size)
				if (data[ii][j] >= 0 && data[ii][j] != data[i][j]) 
				{
//					printf("i = %d j = %d\n", i, j);
					return false;
				}
		}

	return true;
}

int absval(int x)
{
	return x < 0 ? -x : x;
}

int calcD(int x, int y)
{
	int maxD = 0;

	for (int i = 1; i <= size; ++i)
		for (int j = 1; j <= size; ++j)
			if (data[i][j] >= 0)
			{
				int d = absval(i - x) + absval(j - y);
				if (d > maxD)
					maxD = d;
			}
	
	return maxD + 1;
}

int main()
{
//	freopen("A.in", "r", stdin);

	int C;
	scanf("%d", &C);

	for (int cas = 0; cas < C; ++cas)
	{
		scanf("%d", &N);
		size = 2 * N - 1;

		memset(data, -1, sizeof(data));
		for (int i = 1; i <= N; ++i)
		{
			int k = i;
			for (int j = N - k + 1, l = 0; l < i; ++l, j += 2)
			{
		//		printf("i = %d j = %d\n", i, j);
			
				scanf("%d", &data[i][j]);
			}
		}
		for (int i = N + 1; i < 2 * N; ++i)
		{
			int k = 2 * N - i;
			for (int j = N - k + 1, l = 0; l < 2 * N - i; ++l, j += 2)
				scanf("%d", &data[i][j]);
		}

//		for (int i = 1; i <= size; ++i)
//		{
//			for (int j = 1; j <= size; ++j)
//				printf("%d ", data[i][j]);
//			printf("\n");
//		}

		int answer = 1000000000;

		if (N == 1)
			answer = 1;
		else
		{
			for (int i = 1; i <= size; ++i)
				for (int j = 1; j <= size; ++j)
				{
//					if (i == 3 && j == 4)
//						printf("%d\n", check(i, j));

					if (check(i, j))
					{
						int k = calcD(i, j);

//						printf("i = %d j = %d k = %d\n", i, j, k);

						if (k < answer)
							answer = k;
					}
				}
		}

		printf("Case #%d: %d\n", cas + 1, answer * answer - N * N);
	}

	return 0;
}
