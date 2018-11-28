#include <stdio.h>

int T, n, k;

int main()
{
	int t;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d", &n, &k);
		int m = (1 << n) - 1;
		printf("Case #%d: %s\n", t, ((k & m) == m)?"ON":"OFF");
	}
	return 0;
}
