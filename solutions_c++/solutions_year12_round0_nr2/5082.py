#include<stdio.h>
#include<string.h>
int main()
{
	freopen("inb.txt","rt",stdin);
    freopen("outb.txt","wt",stdout);
	int tc;
	scanf("%d", &tc);
	//getchar();	
	for(int j=1;j<=tc;j++)
	{
		long n,s,p,c=0;
		scanf("%ld%ld%ld",&n,&s,&p);
		for(int i = 0; i < n; i++)
		{
			long x;
			scanf("%ld", &x);
			if(x == 0 && p > 0)
				continue;
			int d = x/3;
			int r = x%3;
			if(r == 0)
			{
				if(d >= p)
					c++;
				else if(s > 0 && d+1 >= p)
				{
					s--;
					c++;
				}
			}
			else if(r == 1)
			{
				if(d+1 >= p)
					c++;
			}
			else
			{
				if(d+1 >= p)
					c++;
				else if(s > 0 && d+2 >= p)
				{
					s--;
					c++;
				}
			}
		}
		printf("Case #%d: %d\n",j,c);
	}
	return 0;
}
