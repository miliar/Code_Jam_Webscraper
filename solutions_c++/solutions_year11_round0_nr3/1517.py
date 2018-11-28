#include<cstdio>

int main()
{
	//freopen("D:\\data\\A-large.in","r",stdin);
	//freopen("D:\\data\\A-large.out","w",stdout);
	int t=0,tt;
	scanf("%d",&tt);
	while(tt--)
	{
		int n,m=-1u>>1,i,s=0,sum=0,a[1005];
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",a+i);
			if(a[i]<m)
				m=a[i];
			sum+=a[i];
			s^=a[i];
		}
		printf("Case #%d: ",++t);
		if(s)
			puts("NO");
		else
		{
			printf("%d\n",sum-m);
		}
	}
}
