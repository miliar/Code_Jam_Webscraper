#include <stdio.h>

int main()
{
	int T, t;
	int n, k, base;

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	for(scanf("%d", &T), t = 1; T; --T, ++t)
	{
		scanf("%d%d", &n, &k);

		base = 1 << n;
		if((k + 1) % base != 0)
			printf("Case #%d: OFF\n", t);
		else 
			printf("Case #%d: ON\n", t);
	}

	return 0;
}