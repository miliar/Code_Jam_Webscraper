#include<stdio.h>
int main()
{
	int T,i,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		int n,s,p,t,mo,num=0;
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			mo=t%3;
			t/=3;
			if(t>=p)
				num++;
			else
			{
				if(mo==0 && t+1==p && s>0 && t>0)
				{
					s--;
					num++;
				}
				if(mo==1 && t+1==p)
					num++;
				if(mo==2)
				{
					if(t+1==p)
						num++;
					if(s>0 && t+2==p)
					{
						s--;
						num++;
					}
				}
			}
		}
		printf("Case #%d: %d\n",++cas,num);
	}
	return 0;
}