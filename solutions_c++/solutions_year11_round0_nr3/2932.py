#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXX = 1000;
int candy[MAXX+1];

int main()
{
	int T, N;
	int i, j;
	unsigned int sum;
	int xor;
	freopen("Cl.in", "r", stdin);
	freopen("Cl.out", "w", stdout);
    while (scanf("%d", &T) != EOF)
	{
		for (i=0; i<T; i++)
		{
			scanf("%d", &N);
			for (j=0; j<N; j++)
				scanf("%d", &candy[j]);
			sort(candy, candy+N);
			xor = 0;
			sum = 0;
			for (j=N-1; j>=0; j--)
			{
				sum += candy[j];
				xor = xor ^ candy[j];
			}
			if (xor != 0)
				printf("Case #%d: NO\n", i+1);
			else
			    printf("Case #%d: %d\n", i+1, sum-candy[0]);
		}
	}
	return 0;
}
