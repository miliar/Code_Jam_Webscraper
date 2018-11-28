#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void main()
{
	int C;
	scanf("%d", &C);

	for(int c = 1; c <= C; c++)
	{
		int N, M, A;

		scanf("%d %d %d", &N, &M, &A);

		if(A == 1)
		{
			printf("Case #%d: 0 0 1 0 0 1\n", c);
		}
		else if(A > M * N)
		{
			printf("Case #%d: IMPOSSIBLE\n", c);
		}
		else
		{
			bool bFlag = false;

			for(int i = 1; i <= N; i++)
			{
				if(A % i == 0)
				{
					if(A / i <= M)
					{
						printf("Case #%d: 0 0 %d 0 0 %d\n", c, i, A / i);
						bFlag = true;
					}
				}
				if(bFlag)
					break;
			}
			if(!bFlag)
			{
				for(int i = 1; i <= N; i++)
				{
					for(int j = 1; j <= M; j++)
					{
						for(int k = i; k <= N; k++)
						{
							if(j == M && k == i)
								continue;
							if(A == 2 * M * N - i * M - (2 * N - i - k) * (M - j) - (2 * N - k) * j)
							{
								printf("Case #%d: 0 0 %d %d %d %d\n", c, i, M, k, j);
								bFlag = true;
							}
							if(bFlag)
								break;
						}
						if(bFlag)
							break;
					}
					if(bFlag)
						break;
				}
			}



			if(!bFlag)
			{
				printf("Case #%d: IMPOSSIBLE\n", c);
			}
		}
	}
}
