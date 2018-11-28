#include <stdio.h>
int main()
{
	int a[1024],b[1024];
	int t,n,c;
	int i,j,k;
	freopen("A-large (1).in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d%d",&a[i],&b[i]);
		}
		c=0;
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++)
			{
				if ((a[i]-a[j])*(b[i]-b[j])<0)
				{
					c++;
				}
			}
		}

		printf("Case #%d: %d\n",k,c);
	}
}