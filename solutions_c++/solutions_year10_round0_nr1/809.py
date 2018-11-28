#include <cstdio>

int main()
{
	int t;
	scanf("%d", &t);

	for (int tp = 1; tp <= t; ++tp)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		
		printf("Case #%d: %s\n", tp, (k % (1<<n) == ((1<<n)-1))? "ON" : "OFF");
	}
	return 0;
}
