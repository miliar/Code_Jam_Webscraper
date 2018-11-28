#include <cstdio>

int t, n, s, p, res, val;

int main()
{
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)
	{
		res=0;
		scanf("%d%d%d",&n,&s,&p);
		while(n--)
		{
			scanf("%d",&val);
			if(val/3 >= p || (val%3 && val/3+1 >= p))
				res++;
			else if(s>0 && ((val>0 && val/3+1 >= p) || (val%3 == 2 && val/3+2 >= p)))
				res++,s--;
		}
		printf("Case #%d: %d\n",i,res);
	}
}

