#include <stdio.h>

int main()
{
	int n,i=1,k;
	scanf("%d",&n);
	while (scanf("%d %d",&n,&k)==2) {
		printf("Case #%d: %s\n",i,((k+1)%(1<<n))==0?"ON":"OFF");
		++i;
	}
}