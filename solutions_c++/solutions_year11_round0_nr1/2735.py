#include<stdio.h>
int abs(int x)
{
	if(x<0)return -x;
	return x;
}
main()
{
	int abc,i,j,m,n,t,ans,now[2],la[2];
	char c;
	freopen("A-large.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&abc);
	for(int k=0;k<abc;k++)
	{
		ans=0;la[0]=3;la[1]=0;now[0]=1;now[1]=1;
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf(" %c %d",&c,&t);
			if(c=='O')
			{
				if(la[0]==1)
				{
					if(abs(now[0]-t)-la[1]>0)
					{
						ans+=abs(now[0]-t)-la[1]+1;
						la[1]=abs(now[0]-t)-la[1]+1;
					}
					else
					{
						ans+=1;
						la[1]=1;
					}
					la[0]=0;
					now[0]=t;
				}
				else
				{
					ans+=abs(now[0]-t)+1;
					la[0]=0;
					la[1]+=abs(now[0]-t)+1;
					now[0]=t;
				}
			}
			else
				if(la[0]==0)
				{
					if(abs(now[1]-t)-la[1]>0)
					{
						ans+=abs(now[1]-t)-la[1]+1;
						la[1]=abs(now[1]-t)-la[1]+1;
					}
					else
					{
						ans+=1;
						la[1]=1;
					}
					la[0]=1;
					now[1]=t;
				}
				else
				{
					ans+=abs(now[1]-t)+1;
					la[0]=1;
					la[1]+=abs(now[1]-t)+1;
					now[1]=t;
				}
		}
		printf("Case #%d: %d\n",k+1,ans);
	}
	//scanf(" ");
}
/*
3
2 B 2 B 1
*/
