#include <stdio.h>

int main(int argc, char const* argv[])
{
	int tc, n, k, v;
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", ti + 1);
		v = (1 << n) - 1;
		puts ( ((k & v) == v) ? "ON" : "OFF");
	}
	return 0;
}
