#include<stdio.h>
#include<stdlib.h>

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	long i,r,k,n,g[15],t,count,temp,c=1,s,tc;
	scanf("%ld",&t);
	while(t--)
	{
		scanf("%ld %ld %ld",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%ld",&g[i]);
		count=0;
		i=0;
		while(r--)
		{
			temp=0;
			s=i;
			tc=0;
			while(1)
			{
				if(s==i)
					tc++;
				if(tc==2)
					break;
				if(temp+g[i] <= k)
				{
					temp = temp+g[i];
					i++;
					if(i==n)
						i=0;
				}
				else
					break;
			}
			count = count+temp;
		}
		printf("Case #%ld: %ld\n",c,count);
		c++;
	}
	return 0;
}