#include <stdio.h>

int n, k;

int main()
{
	int i, t, mask;
	//freopen("test.in", "r", stdin);
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d %d", &n, &k);
		mask = (1<<n) - 1;
		if((k & mask) == mask) {
			printf("Case #%d: ON\n", i + 1);
		} else {
			printf("Case #%d: OFF\n", i + 1);
		}
	}
	return 0;
}