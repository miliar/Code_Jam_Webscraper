#include<stdio.h>
int main()
{
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		unsigned int n,k;
		scanf("%u %u",&n,&k);
		
		printf("Case #%d: ",t);
		
		if(k%(1<<n)==(1<<n)-1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
