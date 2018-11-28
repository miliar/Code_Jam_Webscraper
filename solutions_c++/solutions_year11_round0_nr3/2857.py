#include<stdio.h>

int a[1001];

int main()
{
	freopen("outputC.txt","w",stdout);
	int T,n,i,t;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&n);
		int s=0,y=0,mina=10000000;
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			if (mina>a[i]) mina=a[i];
			s^=a[i];
			y+=a[i];
		}
		printf("Case #%d: ",t);
		if (s!=0)
			printf("NO\n");
		else
			printf("%d\n",y-mina);
	}
}
