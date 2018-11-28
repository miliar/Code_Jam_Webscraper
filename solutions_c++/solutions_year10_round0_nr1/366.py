#include <stdio.h>
#define N 110
int main()
{
	int n, k, t, ts;
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		scanf("%d%d", &n, &k);
		if(k%(1<<n)==(1<<n)-1) printf("Case #%d: ON\n", t+1);
		else printf("Case #%d: OFF\n", t+1);
	}
	return 0;
}