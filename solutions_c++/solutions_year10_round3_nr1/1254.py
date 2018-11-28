#include<stdio.h>

struct Point
{
	int x;
	int y;
}mypoint[2000];


int is_intersect(int x1,int y1,int x2,int y2)
{
	if((x1-x2)>0 && (y1-y2)<0)
		return 1;
	if((x1-x2)<0 && (y1-y2)>0)
		return 1;
	return 0;
}

int main(void)
{
	
	
	int n,t,i,j,incount,k;
	
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d",&t);

	
	
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%d %d",&mypoint[j].x,&mypoint[j].y);
		}
		incount = 0;
		
		for (j=0;j<n-1;j++)
		{
			for (k=j+1;k<n;k++)
			{
				if(is_intersect(mypoint[j].x,mypoint[j].y,mypoint[k].x,mypoint[k].y)==1)
					incount++;
			}
		}
		printf("Case #%d: %d\n",i,incount);
	}

	
	
	return 0;
}
