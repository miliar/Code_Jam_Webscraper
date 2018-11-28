#include<stdio.h>
#define inf 0x3f3f3f3f

int a[1500];
int main()
{
	int t,n,i,cas=1,ans;
	int Sum,min;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		Sum=0;ans=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			Sum+=a[i];
			ans^=a[i];
		}
		printf("Case #%d: ",cas++);
		if(ans!=0)
		{
			printf("NO\n");
			continue;
		}
		min=inf;
		for(i=1;i<=n;i++)
			if(a[i]<min)
				min=a[i];
		printf("%d\n",Sum-min);
	}
	return 0;
}