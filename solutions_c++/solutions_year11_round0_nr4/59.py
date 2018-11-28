#include<stdio.h>
int n,a[1000],b[1000];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,i,j,c,T=1;
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			a[i]--;
			b[i]=0;
		}
		double ans=0;
		for(i=0;i<n;i++)
		{
			if(b[i]==0)
			{
				c=0;
				j=i;
				do
				{
					b[j]=1;
					c++;
					j=a[j];
				}while(j!=i);
				if(c>1)
				{
					ans+=c;
				}
			}
		}
		printf("Case #%d: %lf\n",T++,ans);
	}
	return 0;
}
