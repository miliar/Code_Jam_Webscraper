#include<stdio.h>

int main()
{
	int supScore,thikScore;
	int supCount,thikCount;
	int n,db[120],p,s,t;
	int m=0;
	scanf("%d",&t);
	
	while(t--)
	{
		m++;
		scanf("%d %d %d",&n,&s,&p);
		
		for(int i=0;i<n;i++)
			scanf("%d",&db[i]);
			
		if(p>1)
		{
			supScore=3*p-4;
			thikScore=3*p-2;
		}
		else if(p==1)
		{
			supScore=1;
			thikScore=1;
		}
		else if(p==0)
		{
			supScore=0;
			thikScore=0;
		}
		
		thikCount=0;
		supCount=0;
		for(int i=0;i<n;i++)
		{
			if(db[i]>=thikScore)
				thikCount++;
			else if(db[i]>=supScore)
				supCount++;
		}	
		
		int count=0;
		if(p>1)
		{
			if(supCount>s)
				count=thikCount+s;
			else
				count=thikCount+supCount;
		}
		else
			count=thikCount;
			
		printf("Case #%d: %d\n",m,count);
	}
}