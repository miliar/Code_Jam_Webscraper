/**
 * Google code jam 2010 Round 1
 * B. 
 *
 * singleheart@gmail.com
 */

#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	int C;
	scanf("%d\n", &C);

	for (int x=1; x <= C; ++x)
	{
		int N, K, B, T;
		scanf("%d %d %d %d\n", &N, &K, &B, &T);

		int position[N];
		for (int i=0; i < N; ++i)
			scanf("%d", &position[i]);

		int speed[N];
		for (int i=0; i < N; ++i)
			scanf("%d", &speed[i]);

		float remainingTime[N];
		for (int i=0; i < N; ++i)
			remainingTime[i] = static_cast<float>(B - position[i]) / speed[i];

		int possibleCount = 0;
		for (int i=0; i < N; ++i)
			if (remainingTime[i] <= T)
				possibleCount++;

		printf("Case #%d: ", x);
		if (possibleCount < K)
			puts("IMPOSSIBLE");
		else
		{
			int swap = 0;
			int goodChicken = 0;
			for (int i=N-1; i >= 0; --i)
			{
				if (remainingTime[i] > T)
					continue;

				goodChicken++;

				for (int j=i+1; j < N; ++j)
					if ((speed[j] < speed[i]) && remainingTime[j] > T)
						swap++;

				if (goodChicken >= K)
					break;
			}

			printf("%d\n", swap);
		}
	}

	return 0;
}
