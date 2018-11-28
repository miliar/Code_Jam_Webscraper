#include <stdio.h>

int main(void)
{
	int T, cs, n, k;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		scanf("%d%d",&n,&k);
		int w = (1<<n);
		printf("Case #%d: ", cs);
		if(k%w == w-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
