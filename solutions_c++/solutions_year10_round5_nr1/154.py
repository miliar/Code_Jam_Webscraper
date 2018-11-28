#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>

using namespace std;

int isPrime[10001];

int main()
{
	for (int i = 2; i <= 10000; ++i)
	{
		if (isPrime[i] == 0)
		{
			for (int j = i * i; j <= 10000; j += i)
				isPrime[j] = 1;
		}
	}

	int T;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		printf("Case #%d: ", qn);
		int D, K;
		scanf("%d %d", &D, &K);
		vector<int> a(K);

		int P = 1;
		for (int i = 0; i < D; ++i)
			P *= 10;
		int small = -1;
		for (int i = 0; i < K; ++i)
		{
			scanf("%d", &a[i]);
			if (small  < a[i]) small = a[i];
		}

		if (K == 1)
		{
			printf("I don't know.\n");
			continue;
		}

		int result = -1;
		bool donno = false;

		for (int p = small + 1; p <= P; ++p)
		{
			if (isPrime[p] == 1) continue;

			for (int A = 0; A < p; ++A)
			{
				if (donno) break;
				bool isok = true;
				int B = -1;

				for (int i = 1; i < K; ++i)
				{
					int S = a[i - 1];
					int S2 = a[i];
					int diff = A * S - S2;
					if (i == 1) 
					{
						B = (p - diff % p) % p;
					}
					else
					{
						if ((p - diff % p) % p != B)
						{
							isok = false;
							break;
						}
					}
				}
				if (isok)
				{
					int S = a[K - 1];
//					printf("%d, %d, %d, %d\n", S, A, B, (A * S + B) % p);
					if (result == -1)
					{
						result = (A * S + B) % p;
					}
					else
					{
						if (result != (A * S + B) % p) donno = true;
					}
				}
			}
		}
//		printf("result = %d\n", result);
		if (donno || result == -1)
		{
			printf("I don't know.\n");
		}
		else
		{
			printf("%d\n", result);
		}
	}
}

