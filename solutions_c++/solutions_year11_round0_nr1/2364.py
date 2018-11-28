#include <stdio.h>
#include <math.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,i,j;
	char ch[150][2];
	int  dis[150];
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for (j=1;j<=n;j++)
		{
			scanf("%s%d",&ch[j],&dis[j]);
		}
		int bd,od,bt,ot;
		int ans=0;
		bd=od=1;
		bt=ot=0;
		for (j=1;j<=n;j++)
		{
			if (ch[j][0]=='B')
			{
				if (bt+abs(dis[j]-bd)+1>ans)
				{
					ans=bt+abs(dis[j]-bd)+1;
					bd=dis[j];
					bt=ans;
				}
				else 
				{
					ans++;
					bd=dis[j];
					bt=ans;
				}				
			}
			else if (ch[j][0]=='O')
			{
				if (ot+abs(dis[j]-od)+1>ans)
				{
					ans=ot+abs(dis[j]-od)+1;
					od=dis[j];
					ot=ans;
				}
				else
				{
					ans++;
					od=dis[j];
					ot=ans;
				}
				
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}