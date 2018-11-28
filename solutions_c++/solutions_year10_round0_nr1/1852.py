#include<stdio.h>

int teste, n, k, t;

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	scanf("%d", &teste);

	for (int test = 1; test <= teste; test ++){
		scanf("%d%d", &n, &k);

		k ++;
		t = 1 << n;

		if (k % t == 0)
			printf("Case #%d: ON\n", test);
		else
			printf("Case #%d: OFF\n", test);
	}

	return 0;
}

