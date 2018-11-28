#include<cstdio>
int p[1001];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out1","w",stdout);
	int ans;
	int i,j,k,n,t,tt,ct;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		ans=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d",&p[i]);
		for(i=1;i<=n;i++)
			if(p[i])
			{
				ct=0;
				for(j=i;p[j];)
				{
					ct++;
					k=p[j];
					p[j]=0;
					j=k;
//					printf("%d ",j);
				}
//				printf("\n");
				if(ct!=1)ans+=ct;
			}
		printf("Case #%d: %d.000000\n",tt,ans);
	}
	return 0;
}