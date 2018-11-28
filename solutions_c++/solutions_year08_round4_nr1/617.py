#include "stdio.h"

int a[20000],b[20000],m,t,v,min[20000][2];

int max(int a,int b)
{
	if(a>b)
	{
		return a;
	}
	return b;
}

int mi(int a,int b)
{
	if(a>b)
	{
		return b;
	}
	return a;
}

int main()
{
	freopen("large.txt","r",stdin);
	freopen("large_out.txt","w",stdout);
	int f,ca,i,u;
	scanf("%d",&ca);
	for(f=1;f<=ca;f++)
	{
		scanf("%d%d",&m,&v);
		t=(m-1)/2;
		for(i=1;i<=t;i++)
		{
			scanf("%d%d",&b[i],&a[i]);
		}
		for(;i<=m;i++)
		{
			scanf("%d",&u);
			min[i][u]=0;
			min[i][1-u]=99999;
		}
		for(i=t;i>=1;i--)
		{
			if(i==2)
			{
				i=2;
			}
			min[i][0]=min[i][1]=99999;
			if(b[i]==1)
			{
				u=min[i*2][1]+min[i*2+1][1];
				if(u<min[i][1])
				{
					min[i][1]=u;
				}
				u=mi(min[i*2][0],min[i*2+1][0]);
				if(u<min[i][0])
				{
					min[i][0]=u;
				}
			}
			else
			{
				u=min[i*2][0]+min[i*2+1][0];
				if(u<min[i][0])
				{
					min[i][0]=u;
				}
				u=mi(min[i*2][1],min[i*2+1][1]);
				if(u<min[i][1])
				{
					min[i][1]=u;
				}
			}

			if(a[i])
			{
				if(b[i]==0)
				{
					u=min[i*2][1]+min[i*2+1][1]+1;
					if(u<min[i][1])
					{
						min[i][1]=u;
					}
					u=mi(min[i*2][0],min[i*2+1][0]);
					u=u+1;
					if(u<min[i][0])
					{
						min[i][0]=u;
					}
				}
				else
				{
					u=min[i*2][0]+min[i*2+1][0]+1;
					if(u<min[i][0])
					{
						min[i][0]=u;
					}
					u=mi(min[i*2][1],min[i*2+1][1]);
					u++;
					if(u<min[i][1])
					{
						min[i][1]=u;
					}
				}
			}
		}
		printf("Case #%d: ",f);
		if(min[1][v]<99999)
		{
			printf("%d\n",min[1][v]);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
	return 0;
}