#include<stdio.h>
#include<string.h>
int d[100000],l[100000],c[100000];
int main()
{
	int t,tt,n,i,j,x,y,D;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%d %d",d+i,l+i);
		scanf("%d",&D);
		d[n]=D;
		l[n]=1;
		n++;
		printf("Case #%d: ",tt);
		memset(c,-1,sizeof(c));
		c[0]=d[0];
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++)
			{
				if (d[i]+c[i]<d[j])
					break;
				if (l[j]>=d[j]-d[i])
					x=d[j]-d[i];
				else
					x=l[j];
				if (x>c[j])
					c[j]=x;
			}
		}
		if (c[n-1]==-1)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}