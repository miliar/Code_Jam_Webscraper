#include <cstdio>
#include <cstring>


int main()
{
	int T, N, K;

	freopen("A-large.in", "r", stdin);
	freopen("Alarge.txt", "w", stdout);
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		scanf("%d%d", &N, &K);
		bool f = false;
		if((K % (1 << N) == (1 << N) - 1))
			f = true;
		printf("Case #%d: %s\n", tt, f ? "ON" : "OFF");
	}

	return 0;
}