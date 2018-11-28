#include <stdio.h>

int main()
{
	int T, cas, k, n;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);	
	scanf("%d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", cas);
		if (k%(1<<n)==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
