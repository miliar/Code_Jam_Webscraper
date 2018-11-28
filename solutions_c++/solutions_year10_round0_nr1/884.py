#include <stdio.h>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		int temp = 1 << n;
		printf("Case #%d: ", i + 1);
		if (!((k + 1) % temp)) printf("ON"); else printf("OFF");
		printf("\n");
	}
}