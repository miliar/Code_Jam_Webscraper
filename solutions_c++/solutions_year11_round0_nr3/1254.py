#include <cstdio>
#include <algorithm>

int T, N, X;
int seq[1000];

int main()
{
	scanf("%d", &T);
	for (int cas=1; cas <= T; ++cas)
	{
		scanf("%d", &N);
		for (int i=0; i < N; ++i) scanf("%d", &seq[i]);
		X = 0;
		for (int i=0; i < N; ++i) X ^= seq[i];
		if (X)
		{
			printf("Case #%d: NO\n", cas);
		}
		else
		{
			X = 0;
			for (int i=0; i < N; ++i) X += seq[i];
			X -= *std::min_element(seq, seq + N);
			printf("Case #%d: %d\n", cas, X);
		}
	}
	return 0;
}