#include<cstdio>

int main()
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int n,num;
		scanf("%d",&n);
		double ans=0;
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&num);
			ans+=(num!=i);
		}
		printf("Case #%d: %.6lf\n",tc,ans);
	}
	return 0;
}
