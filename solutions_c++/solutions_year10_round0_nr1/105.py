#include<stdio.h>
#include<string.h>

int main()
{
	int nowt;
	int t, n, k;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%d%d", &n, &k);

		printf("Case #%d: ", nowt);
		if ((k + 1) % (1<<n) == 0) {
			printf("ON\n");
		}
		else {
			printf("OFF\n");
		}
	}

	return 0;
}


