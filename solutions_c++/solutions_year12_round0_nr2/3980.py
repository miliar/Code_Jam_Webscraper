#include<stdio.h>
int main()
{
	int t,tt;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n,m,k;
		int ans=0;
		scanf("%d %d %d",&n,&m,&k);
		for(int i=0;i<n;i++)
		{
			int a,b,c;
			scanf("%d",&a);
			b=(a+1)/3;
			c=b+(a%3==1);
			if(c>=k) ans++;
			else if(b>0 && b+1>=k && m>0)
			{
				ans++;
				m--;
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
