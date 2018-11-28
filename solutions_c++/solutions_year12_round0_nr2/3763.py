#include<stdio.h>


int can(int val,int p)
{
	int ave=val/3,res=val%3;
	if(res==0)
	{
		if(ave>=p)
			return 1;
		else if(ave+1>=p&&ave!=0)
			return 0;
		else return -1;
	}
	else if(res==1)
	{
		if(ave+1>=p)
			return 1;
		else return -1;
	}
	else
	{
		if(ave+1>=p)
			return 1;
		else if(ave+2>=p)
			return 0;
		else return -1;
	}
}
int main()
{
	int t,n,s,p,i,j,r,c;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		c=0;
		scanf("%d%d%d",&n,&s,&p);
		for(j=0;j<n;j++)
		{
			scanf("%d",&r);
			r=can(r,p);
			if(r==1)
				c++;
			else if(r==0&&s>0)
			{
				s--;
				c++;
			}
		}
		printf("Case #%d: %d\n",i,c);
	}
}