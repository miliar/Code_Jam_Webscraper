#include <cstdio>

int T;
int main()
{
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		long long N, K;
		scanf("%lld%lld", &N, &K);
		printf("Case #%d: %s\n", i, (K & ((1LL<<N)-1)) == (1LL<<N)-1 ? "ON" : "OFF");
	}
}
