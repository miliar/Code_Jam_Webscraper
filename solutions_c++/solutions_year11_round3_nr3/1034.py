#include<cstdio>
int main()
{
	int t,n,l,h,i,j,fl;
	int a[200],ca=0;
	scanf("%d",&t);
	while(t--)
	{
		ca++;
		scanf("%d%d%d",&n,&l,&h);
		for (i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=l;i<=h;i++)
		{
			fl = 0;
			for (j=0;j<n;j++)
			{
				if (a[j]%i!=0 && i%a[j]!=0)
				{
					fl = 1;
					break;
				}
			}
			if (fl==1)
				continue;
			else
				break;
		}
		if (fl==1)
			printf("Case #%d: NO\n",ca);
		else
			printf("Case #%d: %d\n",ca,i);
	}
	return 0;
}
