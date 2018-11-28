#include <cstdio>
#include <cstring>

int T, N, K;
int seq[101];

int main()
{
	scanf("%d", &T);
	for (int cas=1; cas <= T; ++cas)
	{
		scanf("%d", &N);
		for (int i=1; i <= N; ++i) scanf("%d", &seq[i]);		
		K = 0;
		for (int i=1; i <= N; ++i) K += seq[i] != i;
		printf("Case #%d: %lf\n", cas, (double) K);
	}
	return 0;
}