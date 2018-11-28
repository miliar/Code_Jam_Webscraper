#include<stdio.h>

int main()
{
	int N,i=0;
	scanf("%d",&N);
	while(i!=N)
	{
		i++;
		int s,p,n;
		scanf("%d%d%d",&n,&s,&p);
		int j;
		int ans=0;
		for(j=0;j<n;j++)
		{
			int a;
			scanf("%d",&a);
			if(a==0)
			{
				if(p==0)
				ans++;
				continue;
			}
			else if(a==1 )
			{
				if(p<=1)
				ans++;
				continue;
			}
			else if(a==2)
			{
				if(p==2 && s>0)
				{
					ans++;
					s--;
				}
				if(p<2)
				{
					ans++;
				}
				continue;
			}
			else
			{
				int q=a/3;
				int r=a%3;
				if(q>=p)
				{
					ans++;
				}
				else
				{
					if(r==0 &&(q+1>=p) && s>0)
					{
							ans++;
							s--;
							continue;
					}
					if(r!=0 && q+1>=p)
					{
						ans++;
						continue;
					}
					if(r==2 && q+2>=p && s>0)
					{
						ans++;
						s--;
					}
					
				}

			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
