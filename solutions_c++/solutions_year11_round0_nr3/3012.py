#include <stdio.h>
int main()
{
	int t,l=1;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int k,i,n,sum,min,zj;
		scanf("%d",&n);
		scanf("%d",&k);
		min=zj=sum=k;
		for(i=1;i<n;i++)
		{
			scanf("%d",&k);
			if(k<min)
				min=k;
			sum+=k;
			zj^=k;
		}
		if(zj!=0)
			printf("Case #%d: NO\n",l++);
		else
			printf("Case #%d: %d\n",l++,sum-min);
	}
	return 0;
}