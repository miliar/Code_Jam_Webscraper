#include<stdio.h>

int n, m, k, T, C;

int main(void)
{
	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	for(scanf("%d",&T);T>=1;T--)
	{
		C++;
		scanf("%d %d",&n,&m);
		k = (1 << n) - 1;
		printf("Case #%d: %s\n",C,(k == (m&k))?"ON":"OFF");
	}
	return 0;
}