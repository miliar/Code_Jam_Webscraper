#include<stdio.h>
int g[1005];
struct node
{
	int index;
	__int64 money;
}begin[1005];
int main()
{
	int r,k,n,i,j,cas,ii,front,cnt,_loop;
	__int64 money,sum,tmp;
	bool flag;
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			begin[i].index=-1;
		for(i=0;i<n;i++)
			scanf("%d",&g[i]);
		money=0;front=0;
		flag=false;
		for(j=1;j<=r;j++)
		{
			sum=0;cnt=0;
			if(begin[front].index==-1)
			{
				begin[front].index=j;
				begin[front].money=money;
				while(1)
				{
					sum+=g[front];
					cnt++;
					if(cnt>n||sum>k)
					{
						sum-=g[front];
						break;
					}
					front++;
					if(front==n)
						front=0;
				}
				money+=sum;
			}
			else
			{
				tmp=money-begin[front].money;
				_loop=j-begin[front].index;
				money+=(r-j+1)/_loop*tmp;
				r=(r-j+1)%_loop;
				flag=true;
				break;
			}
		}
		if(flag)
		{
			while(r--)
			{
				sum=0;cnt=0;
				while(1)
				{
					sum+=g[front];
					cnt++;
					if(cnt>n||sum>k)
					{
						sum-=g[front];
						break;
					}
					front++;
					if(front==n)
						front=0;
				}
				money+=sum;
			}
		}
		printf("Case #%d: %I64d\n",ii,money);
	}
	return 0;
}
