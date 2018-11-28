#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef long long LL;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("small.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int kk=1; kk<=t; kk++){
		int n, k;
		scanf("%d%d", &n, &k);
		n = (1<<n)-1;
		printf("Case #%d: ", kk);
		if((k&n) == n) puts("ON");
		else puts("OFF");
	}
	return 0;
}