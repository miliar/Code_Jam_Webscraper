#include<stdio.h>
#include<memory>
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int c,o,n,now,our,x,i,m;
	int z[5000+16];
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d",&n);
		memset(z,0,sizeof(z));
		now=1;
		for(i=1;;i++)
		{
			x=(i-1)%(n-i+1)+1;
			our=1;
			while(our!=x)
			{
				now++;
				if(now==n+1)
					now=1;
				while(z[now])
				{
					now++;
					if(now==n+1)
						now=1;
				}
				our++;
			}
			z[now]=i;
			if(i==n)
				break;
			now++;
			if(now==n+1)
				now=1;
			while(z[now])
			{
				now++;
				if(now==n+1)
					now=1;
			}
		}
		scanf("%d",&m);
		printf("Case #%d:",o);
		while(m--)
		{
			scanf("%d",&x);
			printf(" %d",z[x]);
		}
		printf("\n");
	}
	return 0;
}


