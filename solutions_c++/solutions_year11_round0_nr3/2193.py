#include<stdio.h>

int n;
int main()
{
	int test,val;
	//freopen("c0.in","r",stdin);
	//freopen("c0.txt","w",stdout);
	scanf("%d",&test);
	for (int cas=1;cas<=test;cas++)
	{
		scanf("%d",&n);
		int x = 0;
		int minv = 999999999;
		int sum = 0;
		for (int i=0;i<n;i++)
		{
			scanf("%d",&val);
			x ^= val;
			sum += val;
			if (val < minv)
				minv = val;
		}
		printf("Case #%d: ",cas);
		if (x == 0)
			printf("%d\n",sum - minv);
		else
			printf("NO\n");
	}
}
