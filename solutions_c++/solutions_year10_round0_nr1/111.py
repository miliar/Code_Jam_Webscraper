#include <cstdio>

char *run()
{
	int n, k;
	scanf("%d %d", &n, &k);
	n = 1 << n;
	++k;
	if (k % n == 0) return "ON";
	else return "OFF";
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Aout2.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %s\n", i, run());
	}
	return 0;
}
