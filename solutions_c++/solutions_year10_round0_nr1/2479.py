#include <stdio.h>
#include <string.h>

int main(void)
{
	int n, k, t, m, test = 0;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	while(t --)
	{
		scanf("%d %d", &n, &k);
		m = 1 << n;
		k %= m;
		printf("Case #%d: ", ++ test);
		if(k + 1 == m)
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}
	
