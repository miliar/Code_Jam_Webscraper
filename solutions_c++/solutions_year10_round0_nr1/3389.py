#include <stdio.h>

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Case_count;
	scanf("%d",&Case_count);
	for(int Case=1;Case<=Case_count;Case++)
	{
		printf("Case #%d: ",Case);
		int n,k;
		scanf("%d%d",&n,&k);
		n=(1<<n);
		if((k%n)==n-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}