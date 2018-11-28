#include<stdio.h>
int main()
{
	int n,k,cs,d;
	scanf("%d",&cs);
	for(d=1;d<=cs;d++)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: %s\n",d,(k+1)%((long long)1<<n)?"OFF":"ON");
	}
}
