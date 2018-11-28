#include<stdio.h>

main()
{
	int t,n,s,p;
	int c = 1;
	scanf("%d",&t);
	while(t--)
	{	int i;
		int count = 0;
		scanf("%d",&n);
		scanf("%d",&s);
		scanf("%d",&p);
		int val;
		for(i=0;i<n;i++)
		{
			scanf("%d",&val);
			if(val == 0){if(val>=p)count++;continue;} 
			int r = val%3;
			int d = val/3;
			if(r==0)
			{	
				if(d>=p)
				count++;
				else if(s>0)
				{
					if(d+1>=p)
					{
						count++;
						s--;
					}
				}
			}
			else if(r==1)
			{

				if(d+1>=p)
				count++;
				
			}
			else if(r==2)
			{
				if(d+1>=p)
				count++;
				else if(s>0)
				{
					if(d+2>=p)
					{
						count++;
						s--;
					}
				}
			}
			
				
		
		}
		printf("Case #%d: %d\n",c,count);
		c++;
	}	
}
