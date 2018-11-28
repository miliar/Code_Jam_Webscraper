#include <stdio.h>

void work()
{
	int n, k;
	scanf("%d %d", &n, &k);
	int div = 1 << n;
	int mod = div - 1;
	
	if( mod == (k % div))
	{
		printf("ON\n");	
	}
	else	printf("OFF\n");
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{
		printf("Case #%d: ", kase);
		work();
	}	

	return 0;
	
}
