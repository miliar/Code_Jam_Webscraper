#include <stdio.h>
#include <string.h>

int main()
{
	int t,len,i,j,n,p,s,a,d;
	scanf("%d",&t);
	for(j = 1;j <=t ;j++)
	{
		printf("Case #%d: ",j);
		scanf("%d %d %d",&n,&s,&p);
		int tot = 0;
		int valid = 0;
		int validdone = 0;
		for(i = 0;i < n;i++)
		{
			scanf("%d",&a);
			if(a == 0)
			{
				if(p == 0)
					tot+=1;
			}
			else if(a == 1)
			{
				if(p<=1)
					tot+=1;
			}
			else if(a%3==0)
			{
				d = a/3;
				if(p<=d)
				{
					valid += 1;
					tot+=1;
				}
				else if(d == p-1)
				{
					if(validdone < s)
					{
						tot+=1;
						validdone+=1;
					}
				}
			}
			else if(a%3 == 1)
			{
				d = a/3;
				if(p<=d+1)
				{
					tot+=1;
					valid+=1;
				}
			}
			else
			{
				d = a/3;
				if(p<=d+1)
				{
					tot+=1;
					valid+=1;
				}
				else if(p == d+2)
				{
					if(validdone < s)
					{
						tot+=1;
						validdone+=1;
					}
				}
				
			}
		}
		printf("%d\n",tot);
	}
	return 0;
}