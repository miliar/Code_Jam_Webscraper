#include<stdio.h>
#include<string.h>
int a[1001];
bool d[1001];
int main()
{
	int t,tt,i,j,n,s,temp;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			scanf("%d",a+i);
		memset(d,0,sizeof(d));
		s=0;
		for (i=1;i<=n;i++)
		{
			if (d[i]==1)
				continue;
			j=i;
			temp=0;
			while (d[j]==0)
			{
				temp++;
				d[j]=1;
				j=a[j];
			}
			if (temp>=2)
				s+=temp;
		}
		printf("Case #%d: %.6lf\n",tt,(double)s);
	}
	return 0;
}