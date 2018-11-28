#include <iostream>
#include <stdio.h>
#define INF 10000000
int main()
{
	int T,n,Case=1;
	int a,sum,odd,min;
	//freopen("C-large.in","r",stdin);
	//freopen("ans.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		odd=0;
		min=INF;
		sum=0;
		while(n--)
		{
			scanf("%d",&a);
			sum+=a;
			odd^=a;
			if(min>a) min=a;
		}
		printf("Case #%d: ",Case++);
		if(odd==0)
		{
			printf("%d\n",sum-min);
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}