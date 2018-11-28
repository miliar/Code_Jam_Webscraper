#include <stdio.h>
#include <stdlib.h>

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=0; i<t; i++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", i+1, (k&((1<<n)-1))==(1<<n)-1 ? "ON" : "OFF");
	}
}
