#include <stdio.h>
int n;
int main()
{
	int ri=1,i,repeat,sum,Min,a,total;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		sum=0;
		Min=1<<30;
		total=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a);
			if( Min >a) Min=a;

			total^=a;
			sum+=a;
		}
		printf("Case #%d: ",ri++);
		if( total )
		{
			puts("NO");
		}
		else printf("%d\n",sum-Min);
	}
	return 0;
}
