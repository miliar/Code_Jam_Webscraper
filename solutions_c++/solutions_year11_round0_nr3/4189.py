#include "stdio.h"

#define f(i,a,b) for(i=a;i<b;i++)
#define fe(i,a,b) for (i=a;i<=b;i++)

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out","w", stdout);
	register int i,j;
	int t,n,c,minv,s,sum;
	scanf("%d", &t);
	fe(i,1,t)
	{
		minv = 99999999;
		s = 0;
		sum = 0;
		scanf("%d", &n);
		while(n--)
		{
			scanf("%d", &c);
			if (c<minv) minv = c;
			s ^= c;
			sum += c;
		}
		if (s==0)
		{
			printf("Case #%d: %d\n", i, sum-minv);
		}
		else
		{
			printf("Case #%d: NO\n", i);
		}
	}
}