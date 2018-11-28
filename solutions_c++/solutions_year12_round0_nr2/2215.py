#include <cstdio>
int t, n, s, p, tt, suma;
int main()
{
	scanf("%d", &t);
	for(int i=1; i<=t; i++)
	{
		scanf("%d%d%d", &n, &s, &p);
		
		while(n--)
		{
			scanf("%d", &tt);
			if(tt%3==0)
			{
				if(tt/3>=p){suma++;continue;}
				if(tt/3>=p-1 && s>0 && tt>1){s--; suma++;}
			}
			if(tt%3==1)
			{
				if(tt/3+1>=p){suma++;continue;}
			}
			if(tt%3==2)
			{
				if(tt/3+1>=p){suma++;continue;}
				if(tt/3+1>=p-1 && s>0 && tt>1){s--; suma++;}
			}
		}
		printf("Case #%d: %d\n", i, suma);
		n=0;suma=0;tt=0;s=0;p=0;
	}
	
	return 0;
}
