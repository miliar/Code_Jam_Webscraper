#include<stdio.h>
int n,a[1000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,i,s,ans,min,T=1;
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&n);
		s=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			s^=a[i];
		}
		printf("Case #%d: ",T++);
		if(s!=0)
		{
			printf("NO\n");
			continue;
		}
		ans=0;
		min=1000000;
		for(i=0;i<n;i++)
		{
			ans+=a[i];
			if(min>a[i])min=a[i];
		}
		ans-=min;
		printf("%d\n",ans);
	}
	return 0;
}
