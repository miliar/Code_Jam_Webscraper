#include<stdio.h>
main()
{
	int T,i,abc,j,s,n,p,t,ans;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(abc=1;abc<=T;abc++)
	{
		ans=0;
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			if(t==0 || t==1)
			{	if(t>=p)ans++;}
			else
			{
				for(j=10;j>=0;j--)
				{
					if(j+j+j==t)
					{
						if(j>=p)ans++;
						else if((j+1==p)&& s>0)
						{
							s--;
							ans++;
						}
						break;
					}
					if(j+j+j==t+1)
					{
						if(j>=p)ans++;
						else if((j+1==p)&& s>0)
						{
							s--;
							ans++;
						}
						break;
					}
					if(j+j+j==t+2)
					{
						if(j>=p)ans++;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",abc,ans);
	}
}
