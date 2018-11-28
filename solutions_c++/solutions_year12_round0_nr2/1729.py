#include<cstdio>

int T,n,s,p,lim,lim2,tt,sum1,sum2,ans;

int main()
{
	scanf("%d",&T);
	for(int I = 1;I <= T;I++)
	{
		scanf("%d%d%d",&n,&s,&p);
		if (p >= 1) lim = p * 3 - 2; else lim = 0;
		if (p >= 2) lim2 = p*3 - 4; else lim2 = p;
		sum1 = sum2 = 0;
		for(int i = 0;i < n;i++)
		{
			scanf("%d",&tt);
			//printf("%d\n",tt);
			if (tt >= lim2) sum1++;
			if (tt >= lim) sum2++;
		}
		if (sum1 - sum2 >= s) ans = sum2+s; else ans = sum1;
		printf("Case #%d: %d\n",I,ans);
		//printf("%d %d\n",sum1,sum2);
	}
	return 0;
}
