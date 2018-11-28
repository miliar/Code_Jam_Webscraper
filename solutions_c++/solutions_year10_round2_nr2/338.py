#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int x[101];
int v[101];
int good[101];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large-output.out", "w", stdout);

	int C;
	scanf("%d", &C);
	for(int test = 1; test <= C; ++test)
	{
		int N, K, B, T;
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for(int i = 0; i < N; ++i)
			scanf("%d", &x[i]);
		for(int i = 0; i < N; ++i)
			scanf("%d", &v[i]);
		memset(good, 0, sizeof(good));
		int howmany = 0;
		for(int i = 0; i < N; ++i)
			if(v[i] * T >= B - x[i])
			{
				howmany++;
				good[i] = true;
			}
		printf("Case #%d: ", test);
		if(howmany < K)
			printf("IMPOSSIBLE\n");
		else
		{
			int found = 0;
			int res = 0;
			for(int i = N - 1; i >= 0 && found < K; --i)
			{
				if(good[i])
				{
					++found;
					for(int j = i + 1; j < N; ++j)
						if(!good[j]) ++res;
				}
			}
			printf("%d\n", res);
		}
	}

	return 0;
}