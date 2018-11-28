#include<stdio.h>
int a[20];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		int best=-1;
		for(int i=1;i<(1<<n)-1;i++)
		{
			int cnt=0;
			int v1=0,v2=0;
			for(int j=0;j<n;j++)
			{
				if((1<<j)&i)
				{
					v1^=a[j];
					cnt+=a[j];
				}
				else
				{
					v2^=a[j];
				}
			}
			if(v1==v2 && best<cnt) best=cnt;
		}
		printf("Case #%d: ",t);
		if(best==-1) printf("NO\n");
		else printf("%d\n",best);
	}
	return 0;
}
