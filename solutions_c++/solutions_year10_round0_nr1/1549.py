#include <stdio.h>

int t, n, k;

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		scanf(" %d %d", &n, &k);
		if ((k&((1<<n)-1))==((1<<n)-1))
			printf("Case #%d: ON\n", cs);
		else
			printf("Case #%d: OFF\n", cs);
	}
	return 0;
}
