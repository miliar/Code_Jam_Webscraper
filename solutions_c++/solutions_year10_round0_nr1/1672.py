//by shuangYY

#include <cstdio>

int main()
{
	int t, n, k;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &t);
	for(int i=1; i<=t; i++){
		scanf("%d%d", &n, &k);

		n = 1 << n;
		if((k % n) == (n-1))
			printf("Case #%d: ON\n", i);
		else
			printf("Case #%d: OFF\n", i);
	}

	return 0;
}