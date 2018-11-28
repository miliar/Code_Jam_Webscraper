#include<stdio.h>
#include<stdlib.h>

int t,n,s,p;
int f[105]={0};

int main(void)
{
	freopen("proB.in","r",stdin);
	freopen("proB.out","w",stdout);
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		scanf("%d%d%d",&n,&s,&p);
		int ans=0;
		for (int j=1;j<=n;j++)
		{
			scanf("%d",&f[j]);
			int tmp=f[j]/3;
			if( tmp>=p )
			{	
				ans++;
				continue;
			}
			if( tmp==p-1 )
			{
				if( f[j]%3!=0 )
				{
					ans++;
					continue;
				}
				else if( s>0 && f[j] >= 2 )
				{
					s--;
					ans++;
					continue;
				}
			}
			if( tmp+2<p ) continue;
			else
			{
				if(s>0 && f[j]%3==2)
				{
					ans++;
					s--;
				}
			}
			f[j]=0;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
